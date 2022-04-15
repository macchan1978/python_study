import unittest
import cv2
import os
import sys

#MEMO : unittest実行時は、実行されるスクリプトの位置がapp_cv_testでないため、ここを検索パスに追加する必要がある。
sys.path.append('app_cv_test')
print(f'current directory : [{os.getcwd()}]')
from common import *

class OpenCvTests(unittest.TestCase):
    def test_imread(self):
        image = cv2.imread(common.getDefaultImageFilePath())
        print(f'image size : {image.shape[1]}x{image.shape[0]}')


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)  # type: ignore

if __name__ == '__main__':
    unittest.main()
