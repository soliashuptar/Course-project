from unittest import TestCase
from map.radius import Circle


class TestCircle(TestCase):
    def setUp(self):
        self.circle_1 = Circle([40.759901, -73.984139], 6041196, 37111525)

    def test_get_district(self):
        self.assertTrue(self.circle_1.get_district(), 59.1)

    def test_abs_of_people(self):
        self.assertTrue(self.circle_1.abs_of_people(), 31070329)

    def test_count_radius(self):
        self.assertTrue(self.circle_1.count_radius(), 50)
