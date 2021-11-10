
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

# delimiters for code 👇

# code delete
LEWAGON_SOLUTION_CODE_DELETE_BEGIN = "# \$DELETE_BEGIN"  # $ escaped for re
LEWAGON_SOLUTION_CODE_DELETE_END = "# \$DELETE_END"

# code challengify
LEWAGON_SOLUTION_CODE_CHALLENGIFY_BEGIN = "# \$CHALLENGIFY_BEGIN"
LEWAGON_SOLUTION_CODE_CHALLENGIFY_END = "# \$CHALLENGIFY_END"

# replacements 👇

# notebook replacements
LEWAGON_SOLUTION_NB_MARKDOWN_REPLACEMENT = "> YOUR ANSWER HERE"

# single line replacements do not require to deal with code indentation
LEWAGON_SOLUTION_CODE_REPLACEMENT_PYTHON = "pass  # YOUR CODE HERE"
LEWAGON_SOLUTION_CODE_REPLACEMENT_PYTHON_COMMENT = "# YOUR CODE HERE"
LEWAGON_SOLUTION_CODE_REPLACEMENT_RUBY = "# YOUR CODE HERE"

# - - - - - delimiters for challengify iterate

# delimiters for code 👇

# version replacement
META_DELIMITER_VERSION_REPLACEMENT = "number"

# before
META_DELIMITER_BEFORE_BEGIN = "# $BEFORE_number_BEGIN"
META_DELIMITER_BEFORE_END = "# $BEFORE_number_END"

# after
META_DELIMITER_AFTER_BEGIN = "# $AFTER_number_BEGIN"
META_DELIMITER_AFTER_END = "# $AFTER_number_END"

# - - - - - file patterns for challengify test and clean

TEST_CHALLENGIFICATION_SUFFIX = "_challengify"

TEST_CHALLENGIFICATION_PATTERNS = [
    "**/.*_challengify*",
    "**/*_challengify*"]
