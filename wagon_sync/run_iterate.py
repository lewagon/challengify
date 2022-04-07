
from wagon_sync.challenge_version_iterator import ChallengeVersionIterator
from wagon_sync.run_sync import run_sync

from wagon_common.helpers.git.remote import git_remote_get_probable_url

import os
import re
import glob
import yaml

from colorama import Fore, Style


def load_conf_file(source, verbose):
    """ loads conf file """

    # build conf path
    conf_path = os.path.join(
        source,
        ".challengify_iterate.yml")

    # check if conf exists
    if not os.path.isfile(conf_path):

        print(Fore.RED
              + "\nConf file does not exists 🤕"
              + Style.RESET_ALL
              + f"\nPlease verify that the path {conf_path} to the annotated challenge is correct.")

        # stop the command
        return None

    # load conf file
    with open(conf_path, "r") as file:
        iterate_conf = yaml.safe_load(file)

    loaded_conf = iterate_conf.get("iterate", None)

    if loaded_conf is None:

        print(Fore.RED
              + "\nInvalid conf file: the \"iterate\" key does not exists 🤕"
              + Style.RESET_ALL
              + f"\nPlease verify the content of {conf_path}.")

        # stop the command
        return None

    if verbose:
        print(Fore.BLUE
              + "\nLoaded conf:"
              + Style.RESET_ALL
              + f"\n{iterate_conf}")

    return loaded_conf


def read_conf(conf, verbose):

    # retrieve parameters
    source_directories = conf.get("sources", [])
    destination_directory = conf.get("destination", ".")
    versions = conf.get("versions", {})
    versioned = conf.get("versioned", {})

    only = conf.get("only", {})
    only_to = only.get("to", {}) or {}      # the yaml loader yields None
    only_for = only.get("for", {}) or {}    # if the key has no value
    only_from = only.get("from", {}) or {}

    if verbose:
        print(Fore.BLUE
              + "\nLoaded conf:"
              + Style.RESET_ALL)

        print("- source directories:")
        [print(f"  - directory {directory}") for directory in source_directories]

        print(f"- destination directory: {destination_directory}")

        print("- versions:")
        [print(f"  - version {version}: {destination}") for version, destination in versions.items()]

        print("- versioned:")
        [print(f"  - versioned {versioned}: {destination}") for versioned, destination in versioned.items()]

        print("- only to:")
        [print(f"  - version {version}: {file}") for version, files in only_to.items() for file in files]

        print("- only for:")
        [print(f"  - version {version}: {file}") for version, files in only_for.items() for file in files]

        print("- only from:")
        [print(f"  - version {version}: {file}") for version, files in only_from.items() for file in files]

    return source_directories, destination_directory, versions, versioned, only_to, only_for, only_from


def process_ignored_files(source, version, position, version_iterator, only_to, only_for, only_from, verbose):
    """
    process a list of ignored files from version number
    and list of before and after rules
    """

    pos = version_iterator.position

    # files are ignored if the challenge version is after the version of the rule
    ignored_to = [file for rule_version, files in only_to.items() for file in files if position > pos(rule_version)]

    if verbose:
        print(Fore.BLUE
              + f"\nFiles ignored by rule `only to` for version {version}:"
              + Style.RESET_ALL)
        [print(f"- {file}") for file in ignored_to]

    # files are ignored if the challenge version is not equal to the version of the rule
    ignored_for = [file for rule_version, files in only_for.items() for file in files if position != pos(rule_version)]

    if verbose:
        print(Fore.BLUE
              + f"\nFiles ignored by rule `only for` for version {version}:"
              + Style.RESET_ALL)
        [print(f"- {file}") for file in ignored_for]

    # files are ignored if the challenge version is before the version of the rule
    ignored_from = [file for rule_version, files in only_from.items() for file in files if position < pos(rule_version)]

    if verbose:
        print(Fore.BLUE
              + f"\nFiles ignored by rule `only from` for version {version}:"
              + Style.RESET_ALL)
        [print(f"- {file}") for file in ignored_from]

    # append the ignored files
    ignored = ignored_to + ignored_for + ignored_from

    # resolve globbing patterns
    ignored = [p for pattern in ignored for p in glob.glob(pattern, recursive=True)]

    # correct additional ignores relative to source path
    if source != ".":
        ignored = [os.path.join(source, path) for path in ignored]

    if verbose:
        print(Fore.BLUE
              + f"\nIgnored files for version {version}:"
              + Style.RESET_ALL)
        [print(f"- {file}") for file in ignored]

    return ignored


def write_challenge_metadata(source, version, version_destination, original_files, verbose):

    metadata_filename = ".lewagon/.challengify_generated.txt"
    metadata_path = os.path.join(version_destination, metadata_filename)

    # create metadata directory
    os.makedirs(os.path.dirname(metadata_path), exist_ok=True)

    # get probable remote url
    probable_url = git_remote_get_probable_url(source, "lewagon")

    # file header
    challengify_generated_header = f"""# generated by challengify iterate
# - source: {probable_url}
# - version: {version}
"""

    # write content
    with open(metadata_path, "w") as file:
        file.write(challengify_generated_header)
        file.write("\n".join([metadata_filename] + original_files) + "\n")

    if verbose:
        print(Fore.BLUE
              + "\nWrite metadatafile"
              + Style.RESET_ALL
              + f"\n- path: {metadata_path}")


def build_versioned_path(current_version, file_path, destination_path):
    """
    build versioned file path from destination path
    and cleaned versioned file name
    """

    # retrieve filename
    file_basename = os.path.basename(file_path)
    versioned_file_pattern = f"[0-9]*_(.*)_{current_version}(.*)"
    matches = re.findall(versioned_file_pattern, file_basename)

    if len(matches) != 1:

        print(Fore.RED
              + "\nError parsing versioned file name 😵"
              + Style.RESET_ALL
              + f"\n- version: {current_version}"
              + f"\n- path: {file_path}"
              + f"\n- destination: {destination_path}"
              + f"\n- matches: {matches}")

        exit()

    # concatenate capture groups
    filename = "".join(matches[0])

    versioned_path = os.path.relpath(os.path.join(
        destination_path,
        filename))

    return versioned_path


def process_versioned_files(versioned, current_version, verbose):
    """
    return a list of versioned files
    from files matching challenge version pattern in the conf versioned directories
    """

    custom_files = {}

    # iterate through versioned directories
    for versioned_path, destination_path in versioned.items():

        # look for versioned file for challenge version
        dot_versioned_pattern = f"[0-9]*_*_{current_version}.*"
        versioned_pattern = f"[0-9]*_*_{current_version}"  # no file extension
        dot_path_pattern = os.path.join(versioned_path, dot_versioned_pattern)
        path_pattern = os.path.join(versioned_path, versioned_pattern)

        # retrieve files matching pattern
        glob_results = glob.glob(dot_path_pattern) + glob.glob(path_pattern)

        # append destination directory
        full_results = {f: build_versioned_path(current_version, f, destination_path) for f in glob_results}

        custom_files = dict(**custom_files, **full_results)

    if verbose:
        print(Fore.BLUE
              + f"\nVersioned files for {current_version}:"
              + Style.RESET_ALL)
        {print(f"- {f} to {d}") for f, d in custom_files.items()}

    return custom_files


def run_iterate(challengify, source, min_version, max_version, force, dry_run, verbose, ignore_metadata, format):

    # load conf
    conf = load_conf_file(source, verbose)

    if conf is None:

        # stop the command
        return

    # read conf
    source_directories, destination_directory, versions, versioned, \
        only_to, only_for, only_from = read_conf(conf, verbose)

    # create iterator
    version_iterator = ChallengeVersionIterator(versions)
    version_iterator.filter(min_version, max_version)

    if verbose:
        print(Fore.BLUE
              + "\nAll challenges:"
              + Style.RESET_ALL)
        [print(f"- {c.version}") for c in version_iterator.versions]

        print(Fore.BLUE
              + "\nFiltered challenges:"
              + Style.RESET_ALL)
        [print(f"- {c.version}") for c in version_iterator]

    # iterate through challenge versions
    for challenge_version in version_iterator:

        ignored = process_ignored_files(source, challenge_version.version, challenge_version.position, version_iterator, only_to, only_for, only_from, verbose)

        # process versioned files
        custom_files = process_versioned_files(versioned, challenge_version.version, verbose)

        # build version destination
        version_destination = os.path.join(
            destination_directory, challenge_version.destination)

        if verbose:
            print(Fore.BLUE
                  + f"\nProcess version {challenge_version.version}:"
                  + Style.RESET_ALL
                  + f"\n- sources: {source_directories}"
                  + f"\n- destination: {version_destination}"
                  + f"\n- ignored: {ignored}")

        # challengify the challenge version
        original_files, processed_files = run_sync(
            challengify,
            source_directories + list(custom_files.keys()),
            version_destination,
            force,
            dry_run,
            verbose,
            test=False,
            user_autoformater=format,             # autoformat generated code
            ignore_tld=True,                      # do not append path in git directory
            iterate_yaml_path=source,             # path to iterate yaml
            additional_ignores=ignored,           # handle ignored files
            custom_files=custom_files,            # list of custom target files
            version_iterator=version_iterator,    # handle version delimiters
            version_info=challenge_version.version)  # version info

        # generate metadata
        if not dry_run and not ignore_metadata:
            write_challenge_metadata(source, challenge_version.version, version_destination, original_files, verbose)

        # list processed files
        if verbose:
            print(Fore.BLUE
                  + "\nProcessed files:"
                  + Style.RESET_ALL)
            [print(f"- {os.path.relpath(f)}") for f in processed_files]


def profile():

    from wagon_sync.challengify import Challengify

    # create challengify object
    challengify = Challengify()

    # run iteration
    run_iterate(
        challengify, source=".",
        min_version=None, max_version=None, force=True, dry_run=False,
        verbose=False, ignore_metadata=False, format=False)


if __name__ == "__main__":

    profile()
