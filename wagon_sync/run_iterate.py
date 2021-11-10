
from wagon_sync.run_sync import run_sync

import os
import yaml

from colorama import Fore, Style


def load_conf_file(source, verbose):
    """ loads conf file """

    # build conf path
    conf_path = os.path.join(
        source,
        ".challengify_iterate.yaml")

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


def read_conf(source, conf, verbose):

    # retrieve parameters
    source_directory = conf.get("source", source)
    project_name = conf.get("project_name", "")
    destinations = conf.get("destination", {})
    ignores = conf.get("ignore", {})
    ignore_before = ignores.get("before", {})
    ignore_after = ignores.get("after", {})

    if verbose:
        print(Fore.BLUE
              + "\nLoaded conf:"
              + Style.RESET_ALL
              + f"\n- source directory: {source_directory}"
              + f"\n- project name: {project_name}")

        print("- destinations:")
        [print(f"  - version {str(v).rjust(2)}: {d}") for v, d in destinations.items()]

        print("- ignore before:")
        [print(f"  - version {str(v).rjust(2)}: {f}") for v, ff in ignore_before.items() for f in ff]

        print("- ignore after:")
        [print(f"  - version {str(v).rjust(2)}: {f}") for v, ff in ignore_after.items() for f in ff]

    return source_directory, project_name, destinations, ignore_before, ignore_after


def process_ignored_files(version, ignore_before, ignore_after, verbose):
    """
    process a list of ignored files from version number
    and list of before and after rules
    """

    # append the files ignored for because
    ignored = []

    # the current version is strictly before the version of the rule
    ignored += [f for v, ff in ignore_before.items() for f in ff if version < v]

    # the current version is strictly after the version of the rule
    ignored += [f for v, ff in ignore_after.items() for f in ff if version > v]

    if verbose:
        print(Fore.BLUE
              + f"\nIgnored files for version {version}:"
              + Style.RESET_ALL)
        [print(f"- {file}") for file in ignored]

    return ignored


def run_iterate(source, force, dry_run, verbose):

    # load conf
    conf = load_conf_file(source, verbose)

    if conf is None:

        # stop the command
        return

    # read conf
    source_directory, project_name, destinations, ignore_before, ignore_after = \
        read_conf(source, conf, verbose)

    # iterate through challenge versions
    for version, destination in destinations.items():

        ignored = process_ignored_files(version, ignore_before, ignore_after, verbose)

        # build version destination
        version_destination = os.path.join(destination, project_name)

        # build versions
        versions = min(destinations.keys()), max(destinations.keys()), version

        if verbose:
            print(Fore.BLUE
                  + f"\nProcess version {version}:"
                  + Style.RESET_ALL
                  + f"\n- source: {source_directory}"
                  + f"\n- destination: {version_destination}"
                  + f"\n- ignored: {ignored}"
                  + f"\n- versions: {versions}")

        # challengify the challenge version
        run_sync(
            [source_directory],
            version_destination,
            force,
            dry_run,
            verbose,
            test=False,
            user_autoformater=True,               # autoformat generated code
            ignore_tld=True,                      # do not append path in git directory
            additional_ignores=ignored,           # handle ignored files
            version_pre_clean=versions)           # handle version delimiters
