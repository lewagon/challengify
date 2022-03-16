import re
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

# new raw delimiters 👇

CHALLENGIFY_DELIMITERS = dict(
    challengify=[
        dict(begin="# $CHALLENGIFY_BEGIN",  end="# $CHALLENGIFY_END"),
        dict(begin="# $CHA_BEGIN",          end="# $CHA_END")],
    delete=[
        dict(begin="# $DELETE_BEGIN",       end="# $DELETE_END"),               # consume the delimited block without the trailing newline
        dict(begin="# $DEL_BEGIN",          end="# $DEL_END"),
        dict(begin="# $ERASE_BEGIN",        end="# $ERASE_END\n"),              # consume the line of the delimited block
        dict(begin="# $WIPE_BEGIN",         end="# $WIPE_END\n\n"),             # erase + consume the line below the delimited block
        dict(begin="\n# $IMPLODE_BEGIN",    end="# $IMPLODE_END\n\n")])         # wipe + consumes the line above the delimited block

# raw delimiters 👇

# code delete
RAW_CODE_DELETE_BEGIN = "# $DELETE_BEGIN"
RAW_CODE_DELETE_END = "# $DELETE_END"

# code challengify
RAW_CODE_CHALLENGIFY_BEGIN = "# $CHALLENGIFY_BEGIN"
RAW_CODE_CHALLENGIFY_END = "# $CHALLENGIFY_END"

# replacements 👇

# notebook replacements
LEWAGON_SOLUTION_NB_MARKDOWN_REPLACEMENT = "> YOUR ANSWER HERE"

# single line replacements do not require to deal with code indentation
LEWAGON_SOLUTION_CODE_REPLACEMENT_PYTHON = "pass  # YOUR CODE HERE"
LEWAGON_SOLUTION_CODE_REPLACEMENT_PYTHON_COMMENT = "# YOUR CODE HERE"
LEWAGON_SOLUTION_CODE_REPLACEMENT_RUBY = "# YOUR CODE HERE"  # also used for shell script

# - - - - - delimiters for challengify iterate

# delimiters for code 👇

# version replacement
META_DELIMITER_VERSION_REPLACEMENT = "number"

# before
META_DELIMITER_BEFORE_BEGIN = "# $BEFORE_number_BEGIN"
META_DELIMITER_BEFORE_END = "# $BEFORE_number_END"

# only
META_DELIMITER_ONLY_BEGIN = "# $ONLY_number_BEGIN"
META_DELIMITER_ONLY_END = "# $ONLY_number_END"

# after
META_DELIMITER_AFTER_BEGIN = "# $AFTER_number_BEGIN"
META_DELIMITER_AFTER_END = "# $AFTER_number_END"

# ignore code delete
ITERATE_IGNORE_CODE_DELETE_BEGIN = "# $IGNORED_DELETE_BEGIN"
ITERATE_IGNORE_CODE_DELETE_END = "# $IGNORED_DELETE_END"

# ignore code challengify
ITERATE_IGNORE_CODE_CHALLENGIFY_BEGIN = "# $IGNORED_CHALLENGIFY_BEGIN"
ITERATE_IGNORE_CODE_CHALLENGIFY_END = "# $IGNORED_CHALLENGIFY_END"

# - - - - - file patterns for challengify test and clean

TEST_CHALLENGIFICATION_SUFFIX = "_challengify"

TEST_CHALLENGIFICATION_PATTERNS = [
    "**/.*_challengify*",
    "**/*_challengify*"]
