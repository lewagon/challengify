
import os
import yaml

from colorama import Fore, Style


CMD_RUN = "run"
CMD_RUN_DESTINATION = "destination"
CMD_RUN_DESTINATION_DEFAULT = os.path.join("..", "data-challenges")
CMD_RUN_IGNORE_CWD = "ignore_cwd"
CMD_RUN_IGNORE_CWD_DEFAULT = False
CMD_RUN_FORCE = "force"
CMD_RUN_FORCE_DEFAULT = False
CMD_RUN_DRY_RUN = "dry_run"
CMD_RUN_DRY_RUN_DEFAULT = False
CMD_RUN_VERBOSE = "verbose"
CMD_RUN_VERBOSE_DEFAULT = False
CMD_RUN_ALL = "all"
CMD_RUN_ALL_DEFAULT = False
CMD_RUN_TEST = "test"
CMD_RUN_TEST_DEFAULT = False


def build_conf_path():
    """ build conf path """

    # build conf path
    conf_path = os.path.join(
        os.path.expanduser("~"),  # expanded path is required
        ".challengify.yaml")

    return conf_path


def create_home_defaults(force):
    """ create home defaults yaml conf file ~/.challengify.yaml """

    # build conf path
    home_click_defaults_conf = build_conf_path()

    # check if conf exists
    if os.path.isfile(home_click_defaults_conf) and not force:

        print(Fore.RED
              + "\nConf file already exists:"
              + Style.RESET_ALL
              + f"\nEither remove {home_click_defaults_conf} or use the --force flag.")

        # do not overwrite conf file
        return

    # build data
    run = {}
    run[CMD_RUN_DESTINATION] = CMD_RUN_DESTINATION_DEFAULT
    run[CMD_RUN_IGNORE_CWD] = CMD_RUN_IGNORE_CWD_DEFAULT
    run[CMD_RUN_FORCE] = CMD_RUN_FORCE_DEFAULT
    run[CMD_RUN_DRY_RUN] = CMD_RUN_DRY_RUN_DEFAULT
    run[CMD_RUN_VERBOSE] = CMD_RUN_VERBOSE_DEFAULT
    run[CMD_RUN_ALL] = CMD_RUN_ALL_DEFAULT
    run[CMD_RUN_TEST] = CMD_RUN_TEST_DEFAULT

    data = {}
    data[CMD_RUN] = run

    # write conf file
    with open(home_click_defaults_conf, "w") as file:
        yaml.dump(data, file)  # default_flow_style=False

    print(Fore.GREEN
          + "\nConf file generated:"
          + Style.RESET_ALL
          + f"\nLocation: {home_click_defaults_conf}")


def load_home_defaults(verbose):
    """ load home defaults yaml conf file ~/.challengify.yaml """

    # build conf path
    home_click_defaults_conf = build_conf_path()

    # check if conf exists
    if os.path.isfile(home_click_defaults_conf):

        # load conf
        with open(home_click_defaults_conf, "r") as file:
            defaults_conf = yaml.safe_load(file)

    else:

        # read conf from defaults
        defaults_conf = {}

    if verbose:
        print(Fore.BLUE
              + "\nLoaded conf:"
              + Style.RESET_ALL
              + f"\n{defaults_conf}")

    run_defaults = defaults_conf.get(CMD_RUN, {})

    run_destination_default = run_defaults.get(CMD_RUN_DESTINATION, CMD_RUN_DESTINATION_DEFAULT)
    run_ignore_cwd_default = run_defaults.get(CMD_RUN_IGNORE_CWD, CMD_RUN_IGNORE_CWD_DEFAULT)
    run_force_default = run_defaults.get(CMD_RUN_FORCE, CMD_RUN_FORCE_DEFAULT)
    run_dry_run_default = run_defaults.get(CMD_RUN_DRY_RUN, CMD_RUN_DRY_RUN_DEFAULT)
    run_verbose_default = run_defaults.get(CMD_RUN_VERBOSE, CMD_RUN_VERBOSE_DEFAULT)
    run_all_default = run_defaults.get(CMD_RUN_ALL, CMD_RUN_ALL_DEFAULT)
    run_test_default = run_defaults.get(CMD_RUN_TEST, CMD_RUN_TEST_DEFAULT)

    return (
        run_destination_default,
        run_ignore_cwd_default,
        run_force_default,
        run_dry_run_default,
        run_verbose_default,
        run_all_default,
        run_test_default)
