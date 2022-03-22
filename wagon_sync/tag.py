
from wagon_sync.code_edition import replace_content


class Tag:  # Mask

    def __init__(self, begin, end, replacement, eat_indentation):

        self.begin = begin                        # begin delimiter
        self.end = end                            # end delimiter
        self.replacement = replacement
        self.eat_indentation = eat_indentation

    def apply(self, content):

        decorated = replace_content(
            content, self.replacement, self.begin, self.end, self.eat_indentation)

        return decorated

    def print(self):

        begin = self.begin.replace("\n", "\\n")
        end = self.end.replace("\n", "\\n")

        print(f"\n- begin: {begin}"
              + f"\n- end: {end}"
              + f"\n- replacement: {self.replacement}"
              + f"\n- eat_indentation: {self.eat_indentation}")
