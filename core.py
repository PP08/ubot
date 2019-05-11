import math
import re
import sys
from enum import Enum


class Action(Enum):
    """Actions that UBot can understand"""
    TURN_LEFT = 'L'
    TURN_RIGHT = 'R'
    WALK = 'W'


class UBot:
    def __init__(self, x=0, y=0, angle=90):
        """
        Initial state of UBot
        default: x = 0, y = 0, UBot is facing to the North, equivalent with 90 degree
        """
        self.x = x
        self.y = y
        self.angle = angle

    def execute_command(self, moving_command):
        """execute moving command"""
        actions = self.parse_command_to_actions(moving_command)
        for action in actions:
            self.move(action)

    @staticmethod
    def parse_command_to_actions(moving_command):
        """parse command to list of single step"""
        regex = re.compile(r'[A-Z][0-9]*')
        return re.findall(regex, moving_command)

    def move(self, action):
        """do action: turning or walking"""
        if action == Action.TURN_LEFT.value:
            self.angle += 90
        elif action == Action.TURN_RIGHT.value:
            self.angle -= 90
        elif re.compile(r'^W[0-9]+$').match(action):
            steps = int(action[1:])
            _rad_angle = math.radians(self.angle)
            _sin = math.sin(_rad_angle)
            _cos = math.cos(_rad_angle)
            if -1 < _sin < 1:
                self.x += int(_cos * steps)
            elif -1 < _cos < 1:
                self.y += int(_sin * steps)
            else:
                print('something went wrong. Current action: {}, bot-angle: {}, bot-x: {}, bot-y: {}'.format(action,
                                                                                                             self.angle,
                                                                                                             self.x,
                                                                                                             self.y))
                exit()
        else:
            print("UBot cannot complete the command due the bot cannot understand the {} action".format(action))
            exit()

    def get_direction(self):
        """return UBot direction"""
        return self.convert_angle_to_direction(self.angle)

    @staticmethod
    def convert_angle_to_direction(angle):
        """convert angle to direction"""
        _rad = math.radians(angle)
        _sin = math.sin(_rad)
        _cos = math.cos(_rad)
        if -1 < _sin < 1:
            if _cos == 1:
                return 'East'
            elif _cos == -1:
                return 'West'
        elif _sin == 1:
            return 'North'
        elif _sin == -1:
            return 'South'
        return 'Unidentified (angle: {})'.format(angle)

    def __repr__(self):
        """UBot object representation"""
        return 'X: {} Y: {} Direction: {}'.format(self.x, self.y, self.get_direction())


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Missing command for the bot')
        exit()
    command = sys.argv[1].rstrip().lstrip().upper()
    uBot = UBot()
    uBot.execute_command(command)
    print(uBot.__repr__())
