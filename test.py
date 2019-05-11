import unittest

from core import UBot


class TestUBotConvertAngleToDirection(unittest.TestCase):
    def test_convert_zero_degree_to_east(self):
        self.assertEqual(UBot.convert_angle_to_direction(0), 'East')

    def test_convert_ninety_degree_to_north(self):
        self.assertEqual(UBot.convert_angle_to_direction(90), 'North')

    def test_convert_minus_ninety_degree_to_south(self):
        self.assertEqual(UBot.convert_angle_to_direction(-90), 'South')

    def test_convert_minus_pi_to_west(self):
        self.assertEqual(UBot.convert_angle_to_direction(-180), 'West')

    def test_convert_pi_to_west(self):
        self.assertEqual(UBot.convert_angle_to_direction(180), 'West')

    def test_convert_270_degree_to_south(self):
        self.assertEqual(UBot.convert_angle_to_direction(270), 'South')

    def test_convert_unidentified_direction(self):
        self.assertNotIn(UBot.convert_angle_to_direction(60), ['East', 'West', 'North', 'South'])
