
from colorama import Fore, Style


class Verb:

    def __init__(self, verb, fill=False, eat_indentation=False, trailing_newlines=0):

        self.name = verb                                    # verb name
        self.fill = fill                                    # whether replacement introduces content such as `pass  # YOUR CODE HERE`
        self.eat_indentation = eat_indentation              # whether replacement eats leading indentation
        self.trailing_newlines = trailing_newlines          # how many trailing newlines the block replacement eats

    def print(self):

        print(Fore.BLUE
              + f"\nVerb {self.name}:"
              + Style.RESET_ALL
              + f"\n- fill: {self.fill}"
              + f"\n- eat_indentation: {self.eat_indentation}"
              + f"\n- trailing_newlines: {self.trailing_newlines}")
