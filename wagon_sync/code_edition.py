
import re


def replace_content(source, replacement, begin_delimiter, end_delimiter, eat_leading_tabs=False):

    # build leading pattern
    leading_pattern = "\n[ \t]*" if eat_leading_tabs else ""

    # escape delimiters
    begin_escaped = re.escape(begin_delimiter)
    end_escaped = re.escape(end_delimiter)

    # replace content within delimiters
    # (.|\n)*?                non greedily `?`
    #                         capture any characters and new lines `(.|\n)*`
    # (?<!{end_escaped})      negative lookbehind: assert that what immediately
    #                         follows is not `{end_escaped}`
    pattern = f"{leading_pattern}{begin_escaped}(.|\n)*?(?<!{end_escaped}){end_escaped}"
    replaced_content = re.sub(pattern, replacement, source)

    return replaced_content
