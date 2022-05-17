
from wagon_sync.challengify import Challengify

from wagon_sync.params.delimiters import (
    LEWAGON_SOLUTION_NB_TAG_DELETE,
    LEWAGON_SOLUTION_NB_TAG_DELETE_BEGIN,
    LEWAGON_SOLUTION_NB_TAG_DELETE_END,
    LEWAGON_SOLUTION_NB_TAG_CHALLENGIFY,
    LEWAGON_SOLUTION_NB_TAG_STEPS,
    LEWAGON_SOLUTION_NB_TAG_CLEAR_OUTPUT,
    LEWAGON_SOLUTION_NB_DELETE_BEGIN,
    LEWAGON_SOLUTION_NB_DELETE_END,
    LEWAGON_SOLUTION_NB_CHALLENGIFY_BEGIN,
    LEWAGON_SOLUTION_NB_CHALLENGIFY_END,
    LEWAGON_SOLUTION_NB_METADATA_OPT,
    LEWAGON_SOLUTION_NB_METADATA_OPT_KEEP_OUTPUT,
    LEWAGON_SOLUTION_NB_METADATA_OPT_KEEP_OUTPUT_DEFAULT,
    LEWAGON_SOLUTION_NB_MARKDOWN_REPLACEMENT,
    LEWAGON_SOLUTION_CODE_REPLACEMENT_PYTHON,
    LEWAGON_SOLUTION_CODE_REPLACEMENT_PYTHON_COMMENT,
    LEWAGON_SOLUTION_CODE_REPLACEMENT_RUBY)

from wagon_common.helpers.notebook import read_notebook, save_notebook

from wagon_sync.wotebook import Wotebook

import re


def cellify(content):
    """ transform a paragraph of text into a notebook cell source """

    # transform text into a list of lines (keep all the newlines but the last one)
    source = [line + "\n" for line in content.split("\n")]
    source[-1] = source[-1][:-1]

    return source


def stepify(content, replacement):
    """ replace the non single line comment content of a code cell """

    # convert cell to string
    cell_content = "".join(content)

    # find single line comments
    matches = re.findall("#.*", cell_content)

    # replace everything else
    replaced_content = f"\n\n{replacement}\n\n".join(matches) \
                       + f"\n\n{replacement}\n"

    # convert string to cell
    return cellify(replaced_content)


def preprocess_notebook(notebook_content):
    """ clean notebook manually """

    # get notebook language
    nb_metadata = notebook_content.get("metadata", {})
    kernelspec = nb_metadata.get("kernelspec", {})
    language = kernelspec.get("language")
    is_python = language == "python"
    is_ruby = language == "ruby"

    # iterate through notebook cells
    delete_all_cells = False

    for cell in notebook_content.get("cells", []):

        # get cell metadata tags
        metadata = cell.get("metadata", {})
        tags = metadata.get("tags", [])

        # retrieve cell type
        cell_type = cell.get("cell_type")
        is_markdown = cell_type == "markdown"
        is_code = cell_type == "code"

        # replace content of cells with specific tag
        if LEWAGON_SOLUTION_NB_TAG_CHALLENGIFY in tags:

            # replace content with # YOUR CODE HERE / > YOUR ANSWER HERE
            if is_markdown:
                cell["source"] = cellify(LEWAGON_SOLUTION_NB_MARKDOWN_REPLACEMENT)
            elif is_code and is_python:
                cell["source"] = cellify(LEWAGON_SOLUTION_CODE_REPLACEMENT_PYTHON_COMMENT)
            elif is_code and is_ruby:
                cell["source"] = cellify(LEWAGON_SOLUTION_CODE_REPLACEMENT_RUBY)

        # replace the non single line comment content of a code cell
        if LEWAGON_SOLUTION_NB_TAG_STEPS in tags:

            if is_markdown:
                cell["source"] = cellify(LEWAGON_SOLUTION_NB_MARKDOWN_REPLACEMENT)
            elif is_code and is_python:
                cell["source"] = stepify(cell.get("source", ""),
                                         LEWAGON_SOLUTION_CODE_REPLACEMENT_PYTHON_COMMENT)
            elif is_code and is_ruby:
                cell["source"] = stepify(cell.get("source", ""),
                                         LEWAGON_SOLUTION_CODE_REPLACEMENT_RUBY)

        # look for delete begin tag
        if LEWAGON_SOLUTION_NB_TAG_DELETE_BEGIN in tags:
            delete_all_cells = True

        # delete cells between tagged cells included
        if delete_all_cells:

            # create cell metadata tags
            cell["metadata"] = metadata
            metadata["tags"] = tags

            # mark cell for deletion by notebook cleaning process
            tags.append(LEWAGON_SOLUTION_NB_TAG_DELETE)

        # look for delete end tag
        if LEWAGON_SOLUTION_NB_TAG_DELETE_END in tags:
            delete_all_cells = False


def get_notebook_metadata_options(notebook_content):
    """ retrieve notebook metadata challengify options """

    # get options
    nb_metadata = notebook_content.get("metadata", {})
    challengify_options = nb_metadata.get(LEWAGON_SOLUTION_NB_METADATA_OPT, {})

    return challengify_options


def clean_notebook(source, destination, file_extension, nb_options):
    """ clean notebook """

    # get notebook options
    keep_output = nb_options.get(
        LEWAGON_SOLUTION_NB_METADATA_OPT_KEEP_OUTPUT,
        LEWAGON_SOLUTION_NB_METADATA_OPT_KEEP_OUTPUT_DEFAULT)

    # select replacement string for solution code depending on code language
    if file_extension == "rb":
        solution_code_replacement = LEWAGON_SOLUTION_CODE_REPLACEMENT_RUBY
    else:
        solution_code_replacement = LEWAGON_SOLUTION_CODE_REPLACEMENT_PYTHON

    # create notebook cleaner
    # ntbk = nbc.NotebookCleaner(source)
    ntbk = Wotebook(source)

    # handle cells output and standard error
    if keep_output:

        # clean only tagged cells
        # ntbk.clear(["output", "stderr"], tag=LEWAGON_SOLUTION_NB_TAG_CLEAR_OUTPUT)
        ntbk.clear_outputs(tag=LEWAGON_SOLUTION_NB_TAG_CLEAR_OUTPUT)

    else:

        # clean all cells of the notebook
        # ntbk.clear(["output", "stderr"])
        ntbk.clear_outputs()

    # remove cells marked with solution tag
    # ntbk.remove_cells(tag=LEWAGON_SOLUTION_NB_TAG_DELETE)
    ntbk.remove_cells(LEWAGON_SOLUTION_NB_TAG_DELETE)

    # remove content within delimiters
    ntbk.replace_text(
        LEWAGON_SOLUTION_NB_DELETE_BEGIN,
        LEWAGON_SOLUTION_NB_DELETE_END,
        replace_code="",
        replace_md="")

    # replace content within delimiters
    ntbk.replace_text(
        LEWAGON_SOLUTION_NB_CHALLENGIFY_BEGIN,
        LEWAGON_SOLUTION_NB_CHALLENGIFY_END,
        replace_code=solution_code_replacement,
        replace_md=LEWAGON_SOLUTION_NB_MARKDOWN_REPLACEMENT)

    # save edited notebook
    ntbk.save(destination)


def process_notebook(
        challengify: Challengify,
        source, destination, file_extension, version_iterator=None):
    """
    control notebook processes
    """

    # TODO: handle challengify iterate (version_iterator)

    # read notebook into a python dictionary
    notebook_content = read_notebook(source)

    # preprocess notebook
    preprocess_notebook(notebook_content)

    # save updated notebook to disk
    save_notebook(notebook_content, destination)

    # get notebook metadata options
    nb_options = get_notebook_metadata_options(notebook_content)

    # clean preprocessed notebook
    clean_notebook(destination, destination, file_extension, nb_options)
