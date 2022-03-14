
from wagon_sync.process import get_file_extension
from wagon_sync.process_code import process_code

import unittest

import os


class TestCodeActions(unittest.TestCase):

    def __code_transformation_test(self, source_file):

        # get data path
        in_file = os.path.join(os.path.dirname(__file__), "code", source_file)
        in_file_root, in_file_extension = os.path.splitext(in_file)
        out_file = f"{in_file_root}_generated{in_file_extension}"
        processed_file = f"{in_file_root}_processed{in_file_extension}"

        # process file extension
        file_extension = get_file_extension(in_file)

        # transform code
        process_code(in_file, processed_file, file_extension)

        # read files
        with open(out_file, "r") as file:
            out_content = file.read()

        with open(processed_file, "r") as file:
            processed_content = file.read()

        # remove processed file
        os.remove(processed_file)

        # compare results
        self.assertEqual(out_content, processed_content)

    def test_python(self):
        """
        test python code file transformations
        """
        self.__code_transformation_test("python/code.py")

    def test_ruby(self):
        """
        test ruby code file transformations
        """
        self.__code_transformation_test("ruby/code.rb")

    def test_shell(self):
        """
        test shell code file transformations
        """
        self.__code_transformation_test("shell/Dockerfile")
        self.__code_transformation_test("shell/Makefile")
        self.__code_transformation_test("shell/script.sh")

    def test_text(self):
        """
        test text code file transformations
        """
        self.__code_transformation_test("txt/requirements.txt")


if __name__ == '__main__':
    unittest.main()
