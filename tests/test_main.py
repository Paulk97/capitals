import unittest
import sys
sys.path.append('../myfolder')
from capitals import csv_reader
from capitals import type_file
import os


class TestMain(unittest.TestCase):

    def setUp(self):
        self.temporary_file = "/tmp/temporary_file.csv"
        f = open(self.temporary_file, 'w')
        f.close()
        
    def test_no_datafile(self):
        datafile = csv_reader(path="/tmp/nonexistentfile-wewefwwe")
        self.assertFalse(datafile)

    def test_empty_datafile(self):
        datafile = csv_reader(path=self.temporary_file)
        self.assertFalse(datafile)
        
    def test_valid_extension(self):
        extension = type_file(path="/tmp/nonexistentfile-wewefwwe")
        self.assertEqual(extension, ".csv")

    def tearDown(self):
        os.remove(self.temporary_file)
        
if __name__ == '__main__':
    unittest.main()
