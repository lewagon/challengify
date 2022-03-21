
class Tag:

    def __init__(self, begin, end, fill, eat_indentation):

        self.begin = begin
        self.end = end
        self.fill = fill
        self.eat_indentation = eat_indentation

    def print(self):

        begin = self.begin.replace("\n", "\\n")
        end = self.end.replace("\n", "\\n")

        print(f"\n- begin: {begin}"
              + f"\n- end: {end}"
              + f"\n- fill: {self.fill}"
              + f"\n- eat_indentation: {self.eat_indentation}")
