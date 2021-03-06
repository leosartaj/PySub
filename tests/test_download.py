#!/usr/bin/env python2

##
# sub
# https://github.com/leosartaj/sub.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import unittest
from sub.main import download
import os

class options():
    """
    Class for making options objects
    having verbose, recursive and timeout attributes
    """
    def __init__(self, verbose=False, recursive=False, timeout=30):
        self.verbose = verbose
        self.recursive = recursive
        self.timeout = timeout

class TestGetHash(unittest.TestCase):
    """
    Tests the hashing function
    """
    def setUp(self):
        """
        sets the files to work on
        """
        self.smallFile = 'smallFile.testFile'
        self.noSuchFile = '$!$!$'
        self.options = options()
        with open(self.smallFile, 'w') as f:
            f.write('Just Testing\n')
            for cou in range(5000):
                f.write(str(cou))
        
    def test_download_smallFile(self):
        self.assertEqual(download(self.smallFile, self.options), 0)

    def test_download_directory_not_recursive(self):
        self.recursive = False
        self.assertEqual(download(os.getcwd(), self.options), 0)

    def test_download_directory_recursive(self):
        self.recursive = True
        self.assertEqual(download(os.getcwd(), self.options), 0)

    def tearDown(self):
        os.remove(self.smallFile)

if __name__ == '__main__':
    unittest.main()

