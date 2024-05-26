import unittest
from altifier import alty_text

class TestAltCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(to_alt_case("hello"), "HeLlO")
        self.assertEqual(to_alt_case("world"), "WoRlD")

    def test_with_spaces(self):
        self.assertEqual(to_alt_case("hello world"), "
