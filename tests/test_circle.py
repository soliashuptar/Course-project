from unittest import TestCase
import unittest
import sys
sys.path.append("..")
from map.radius import Circle


class TestCircle(TestCase):
    def setUp(self):
        self.circle_1 = Circle([40.759901, -73.984139], 6041196, 37111525)
        self.circle_2 = Circle([40.759901, -73.984139], 1196, 27111525)

    def test_get_district(self):
        self.assertTrue(self.circle_1.get_district(), 59.1)
        self.assertTrue(self.circle_2.get_district(), 59.1)

    def test_abs_ofpeople(self):
        self.assertTrue(self.circle_1.abs_ofpeople(), 31070329)
        self.assertTrue(self.circle_2.abs_ofpeople(), 27110329)

    def test_count_radius(self):
        self.assertTrue(self.circle_1.count_radius(), 50)
        self.assertTrue(self.circle_2.count_radius(), 40)


if __name__ == '__main__':
    unittest.main()
