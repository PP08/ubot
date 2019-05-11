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


class TestUBotInitialSetup(unittest.TestCase):
    def setUp(self):
        self.uBot = UBot()

    def test_uBot_initial_direction(self):
        self.assertEqual(self.uBot.get_direction(), 'North')

    def test_uBot_initial_x_coordinate(self):
        self.assertEqual(self.uBot.x, 0)

    def test_uBot_initial_y_coordinate(self):
        self.assertEqual(self.uBot.y, 0)


class TestUBotMovingFunction(unittest.TestCase):
    def setUp(self):
        self.uBot = UBot()

    def test_uBot_turn_left(self):
        self.uBot.move('L')
        self.assertEqual(self.uBot.get_direction(), 'West')
        self.assertEqual(self.uBot.x, 0)
        self.assertEqual(self.uBot.y, 0)

    def test_uBot_turn_right(self):
        self.uBot.move('R')
        self.assertEqual(self.uBot.get_direction(), 'East')
        self.assertEqual(self.uBot.x, 0)
        self.assertEqual(self.uBot.y, 0)

    def test_uBot_walking_one_step(self):
        self.uBot.move('W1')
        self.assertEqual(self.uBot.get_direction(), 'North')
        self.assertEqual(self.uBot.x, 0)
        self.assertEqual(self.uBot.y, 1)

    def test_uBot_moving_multiple_step(self):
        self.uBot.move('W5')
        self.assertEqual(self.uBot.get_direction(), 'North')
        self.assertEqual(self.uBot.x, 0)
        self.assertEqual(self.uBot.y, 5)
