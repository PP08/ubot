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


class TestUBotParsingCommand(unittest.TestCase):

    def test_uBot_parsing_turning_command(self):
        self.assertListEqual(UBot.parse_command_to_actions('RLLRRR'), ['R', 'L', 'L', 'R', 'R', 'R'])

    def test_uBot_parsing_turning_and_walking_command(self):
        self.assertListEqual(UBot.parse_command_to_actions('RRW55LW100R'), ['R', 'R', 'W55', 'L', 'W100', 'R'])

    def test_uBot_parsing_complex_command_1(self):
        self.assertListEqual(UBot.parse_command_to_actions('RRW11RLLW19RRW12LW1'),
                             ['R', 'R', 'W11', 'R', 'L', 'L', 'W19', 'R', 'R', 'W12', 'L', 'W1'])

    def test_uBot_parsing_complex_command_2(self):
        self.assertListEqual(UBot.parse_command_to_actions('LLW100W50RW200W10'),
                             ['L', 'L', 'W100', 'W50', 'R', 'W200', 'W10'])

    def test_uBot_parsing_complex_command_3(self):
        self.assertListEqual(UBot.parse_command_to_actions('W55555RW555555W444444W1'),
                             ['W55555', 'R', 'W555555', 'W444444', 'W1'])


class TestUBotDoingMultipleActions(unittest.TestCase):

    def setUp(self):
        self.uBot = UBot()

    def test_uBot_doing_multiple_rotating_actions(self):
        self.uBot.execute_command('RLLRRR')
        self.assertEqual(self.uBot.get_direction(), 'South')
        self.assertEqual(self.uBot.x, 0)
        self.assertEqual(self.uBot.y, 0)

    def test_uBot_doing_multiple_rotating_and_walking_actions(self):
        self.uBot.execute_command('RRW55LW100R')
        self.assertEqual(self.uBot.get_direction(), 'South')
        self.assertEqual(self.uBot.x, 100)
        self.assertEqual(self.uBot.y, -55)

    def test_uBot_doing_complex_multiple_action_1(self):
        self.uBot.execute_command('RRW11RLLW19RRW12LW1')
        self.assertEqual(self.uBot.get_direction(), 'South')
        self.assertEqual(self.uBot.x, 7)
        self.assertEqual(self.uBot.y, -12)

    def test_uBot_doing_complex_multiple_action_2(self):
        self.uBot.execute_command('RRW11RLLW19RRW12LW1')
        self.assertEqual(self.uBot.get_direction(), 'South')
        self.assertEqual(self.uBot.x, 7)
        self.assertEqual(self.uBot.y, -12)

    def test_uBot_doing_complex_multiple_action_3(self):
        self.uBot.execute_command('LLLLLW99RRRRRW88LLLRL')
        self.assertEqual(self.uBot.get_direction(), 'East')
        self.assertEqual(self.uBot.x, -99)
        self.assertEqual(self.uBot.y, 88)
