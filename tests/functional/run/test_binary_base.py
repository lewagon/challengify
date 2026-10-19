
from wagon_sync.challengify import Challengify

from wagon_sync.process import process

import unittest

import os


class TestBinaryBase(unittest.TestCase):
    """
    tests binary files are identified and copied as is
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.challengify = Challengify()

    def binary_transformation_test(self, source_file):

        # get data path
        in_file = os.path.join(os.path.dirname(__file__), "..", "..", "data", "code", source_file)
        in_file_root, in_file_extension = os.path.splitext(in_file)
        out_file = f"{in_file_root}_processed{in_file_extension}"
        control_file = f"{in_file_root}_generated{in_file_extension}"

        # transform code
        process(
            self.challengify,
            in_file, "", out_file, dry_run=False,
            ignore_tld=False, iterate_yaml_path=None,
            test=False)

        # read files as bytes
        with open(control_file, "rb") as file:
            control_content = file.read()

        with open(out_file, "rb") as file:
            out_content = file.read()

        # remove processed file
        os.remove(out_file)

        # compare results
        self.assertEqual(control_content, out_content)
