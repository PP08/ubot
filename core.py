import math
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
