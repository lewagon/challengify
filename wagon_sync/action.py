
from wagon_sync.action_copy import action_copy
from wagon_sync.action_clone import action_clone

from wagon_common.helpers.git.repo import get_git_top_level_directory

import os.path

import yaml

import inspect

from colorama import Fore, Style


def load_sync_actions(yaml_path):
    """
    loads actions from conf file
    """

    # check if conf exists
    if not os.path.isfile(yaml_path):

        print(Fore.BLUE
              + f"\nSync conf {yaml_path} does not exist"
              + Style.RESET_ALL
              + "\nNo actions performed")

        # return an empty conf
        return dict(actions=[])

    # load conf
    with open(yaml_path, "r") as file:
        actions_config = yaml.safe_load(file)

    return actions_config


def call_action(action_function, action_conf):
    """
    some fun with introspection
    have a look at action function parameters
    and detect if they are provided in the action conf
    """

    # get function signature
    args = inspect.getfullargspec(action_function).args  # only handle function positional arguments

    # iterating through parameters
    for arg in args:

        # testing if parameter is provided
        if arg not in action_conf:

            print(Fore.RED
                  + f"\nInvalid conf in yaml file"
                  + Style.RESET_ALL
                  + f"\nMissing {arg} parameter in action:"
                  + f"\n{action_conf}")

            # no action ran
            return

    # call action
    action_function(*[action_conf[arg] for arg in args])


def run_action(action_conf):
    """
    runs action depending its conf
    """

    # action methods
    actions = dict(
        copy=action_copy,
        clone=action_clone,
        )

    # retrieve action function
    action = action_conf.get("action", "copy")
    action_function = actions.get(action, action_copy)

    # execute action
    call_action(action_function, action_conf)


def unwrap(loaded_actions):
    """
    unfactor conf entries
    """

    # retrieve actions
    actions = loaded_actions["actions"]

    unwrapped_actions = []

    # iterate through actions
    for action in actions:

        # check if action is unwrappable
        if not "solutions" in action.keys():

            # add to actions as is
            unwrapped_actions.append(action)

            continue

        # retrieve confs
        confs = action.get("solutions", [])

        # iterate through confs
        for conf in confs:

            # create action
            unwrapped_action = action.copy()

            # iterate through conf items
            for k, v in conf.items():

                # unwrap conf
                unwrapped_action[k] = v

            # add to actions
            unwrapped_actions.append(unwrapped_action)

    return unwrapped_actions


def run_actions(yaml_path):
    """
    load configuration yaml
    iterate through actions
    inject code in solutions from external sources
    """

    # set destination to project root
    destination = get_git_top_level_directory()

    print(Fore.GREEN
          + "\nRun actions:"
          + Style.RESET_ALL)

    # load actions
    loaded_actions = load_sync_actions(yaml_path)

    # unwrap parameters
    actions = unwrap(loaded_actions)

    # iterate through actions
    for action in actions:

        # run action
        action["command_destination"] = destination

        run_action(action)
