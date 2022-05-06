
# - - - - - delimiters for challengify run

# tags and delimiters for notebooks 👇

# notebook cell action tags
LEWAGON_SOLUTION_NB_TAG_DELETE = "delete"
LEWAGON_SOLUTION_NB_TAG_DELETE_BEGIN = "delete_begin"
LEWAGON_SOLUTION_NB_TAG_DELETE_END = "delete_end"
LEWAGON_SOLUTION_NB_TAG_CHALLENGIFY = "challengify"
LEWAGON_SOLUTION_NB_TAG_STEPS = "steps"
LEWAGON_SOLUTION_NB_TAG_CLEAR_OUTPUT = "clear_output"

# notebook content delete
LEWAGON_SOLUTION_NB_DELETE_BEGIN = "$DELETE_BEGIN"
LEWAGON_SOLUTION_NB_DELETE_END = "$DELETE_END"

# notebook content challengify
LEWAGON_SOLUTION_NB_CHALLENGIFY_BEGIN = "$CHALLENGIFY_BEGIN"
LEWAGON_SOLUTION_NB_CHALLENGIFY_END = "$CHALLENGIFY_END"

# notebook metadata
LEWAGON_SOLUTION_NB_METADATA_OPT = "challengify"
LEWAGON_SOLUTION_NB_METADATA_OPT_KEEP_OUTPUT = "keep_output"
LEWAGON_SOLUTION_NB_METADATA_OPT_KEEP_OUTPUT_DEFAULT = False

# notebook replacements
LEWAGON_SOLUTION_NB_MARKDOWN_REPLACEMENT = "> YOUR ANSWER HERE"

# single line replacements do not require to deal with code indentation
LEWAGON_SOLUTION_CODE_REPLACEMENT_PYTHON = "pass  # YOUR CODE HERE"
LEWAGON_SOLUTION_CODE_REPLACEMENT_PYTHON_COMMENT = "# YOUR CODE HERE"
LEWAGON_SOLUTION_CODE_REPLACEMENT_RUBY = "# YOUR CODE HERE"  # also used for shell script

# raw comment delimiters 👇

LANGUAGE_INLINE_COMMENT_DELIMITERS = dict(
    default=dict(   prefix="# "),           # "rb", "sh", "txt"
    py=dict(        prefix="# "),
    js=dict(        prefix="// "),
    sql=dict(       prefix="-- "),
    html=dict(      prefix="<!-- ",         suffix=" -->"),
    css=dict(       prefix="/* ",           suffix=" */"),
    html_erb=dict(  prefix="<%#= ",         suffix=" %>"),
    js_erb=dict(    prefix="<%#= ",         suffix=" %>"),
    md=dict(        prefix="[//]: # ( ",    suffix=" )"))

# raw block replacements 👇

REPLACEMENT_CONTENT = "YOUR CODE HERE"

VERB_REPLACEMENT = dict(
    CODE="YOUR CODE HERE")

CUSTOM_REPLACEMENTS = dict(
    py="pass  # YOUR CODE HERE")

# raw verbs 👇

CHALLENGIFY_VERBS = [
    dict(verb="CHALLENGIFY",    fill=True),
    dict(verb="CHA",            fill=True),
    dict(verb="CODE",           fill=True),
    dict(verb="DELETE",                                 trailing_newlines=0),   # consume the delimited block without the indentation or trailing newline
    dict(verb="DEL",                                    trailing_newlines=0),
    dict(verb="ERASE",          eat_indentation=True,   trailing_newlines=0),   # consume the line of the delimited block
    dict(verb="",               eat_indentation=True,   trailing_newlines=1),   # default verb is wipe
    dict(verb="WIPE",           eat_indentation=True,   trailing_newlines=1),   # erase + consume the line below the delimited block
    dict(verb="IMPLODE",        eat_indentation=True,   trailing_newlines=2)]   # wipe + consumes the line above the delimited block

# raw delimiter tag suffixes 👇

DELIMITER_PREFIX = "$"
DELIMITER_SUFFIX_BEGIN = "_BEGIN"
DELIMITER_SUFFIX_END = "_END"

# - - - - - delimiters for challengify iterate

# raw block delimiters 👇

ITERATE_VERSION_DELIMITERS = dict(
    only_to=dict(begin="# $ONLY_TO_version_verb_BEGIN",   end="# $ONLY_TO_version_verb_END"),
    only_for=dict(begin="# $ONLY_FOR_version_verb_BEGIN",  end="# $ONLY_FOR_version_verb_END"),
    only_from=dict(begin="# $ONLY_FROM_version_verb_BEGIN", end="# $ONLY_FROM_version_verb_END"))

# raw tag delimiters 👇

ITERATE_VERSION_META_DELIMITERS = \
    dict(begin="# $verb_ONLY_FOR_version_BEGIN",  end="# $verb_ONLY_FOR_version_END")

# - - - - - file patterns for challengify test and clean

TEST_CHALLENGIFICATION_SUFFIX = "_challengify"

TEST_CHALLENGIFICATION_PATTERNS = [
    "**/.*_challengify*",
    "**/*_challengify*"]
