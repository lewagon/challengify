
import re


def replace_content(source, replacement, begin_delimiter, end_delimiter):

    # replace content within delimiters
    # (.|\n)*?                non greedily `?`
    #                         capture any characters and new lines `(.|\n)*`
    # (?<!{end_delimiter})    negative lookbehind: assert that what immediately
    #                         follows is not `{end_delimiter}`
    pattern = f"{begin_delimiter}(.|\n)*?(?<!{end_delimiter}){end_delimiter}"
    replaced_content = re.sub(pattern, replacement, source)

    return replaced_content
