
from wagon_sync.challengify import Challengify

from wagon_sync.process import get_file_extension
from wagon_sync.process_code import process_code

import unittest

import os


class TestCodeBase(unittest.TestCase):
    """
    basic tests to verify that the outcome of the transformation
    on code files does not change
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.challengify = Challengify()

    def code_transformation_test(self, source_file):

        # get data path
        in_file = os.path.join(os.path.dirname(__file__), "code", source_file)
        in_file_root, in_file_extension = os.path.splitext(in_file)
        out_file = f"{in_file_root}_generated{in_file_extension}"
        processed_file = f"{in_file_root}_processed{in_file_extension}"

        # process file extension
        file_extension = get_file_extension(in_file)

        # transform code
        process_code(
            self.challengify,
            in_file, processed_file, file_extension)

        # read files
        with open(out_file, "r") as file:
            out_content = file.read()

        with open(processed_file, "r") as file:
            processed_content = file.read()

        # remove processed file
        os.remove(processed_file)

        # compare results
        self.assertEqual(out_content, processed_content)
