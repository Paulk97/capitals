import unittest
import sys
sys.path.append('home/seed/capitals/myfolder')
from myfolder.capitals import csv_reader
from myfolder.capitals import type_file
import os


class TestMain(unittest.TestCase):

    def setUp(self):
        self.temporary_file = "/tmp/temporary_file.csv"
        f = open(self.temporary_file, 'w')
        f.close()
        
    def test_no_datafile(self):
        datafile = csv_reader()
        self.assertIn(".csv", self.temporary_file)
        
    def test_full_datafile(self):
        datafile = csv_reader()
        self.assertTrue(datafile)
        
    def test_valid_extension(self):
        extension = type_file(path=self.temporary_file)
        self.assertEqual(extension, ".csv")

    def tearDown(self):
        os.remove(self.temporary_file)
        
if __name__ == '__main__':
    unittest.main()
