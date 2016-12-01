#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Alexandre Viau <alexandre@alexandreviau.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import sys
from enum import Enum


class Direction(Enum):
    north = 1
    south = 2
    east = 3
    west = 4

    def left(self):
        if self == Direction.north:
            return Direction.west
        elif self == Direction.south:
            return Direction.east
        elif self == Direction.east:
            return Direction.north
        elif self == Direction.west:
            return Direction.south
        raise Exception("Bad direction")


    def right(self):
        if self == Direction.north:
            return Direction.east
        elif self == Direction.south:
            return Direction.west
        elif self == Direction.east:
            return Direction.south
        elif self == Direction.west:
            return Direction.north
        raise Exception("Bad direction")


def main():
    # Check for arg lenght
    if len(sys.argv) != 2:
        print("Usage:")
        print("\t%s \"R4, R3, L3\"" % __file__)
        sys.exit(0)

    commands = sys.argv[1].replace(" ", "").split(",")

    current_direction = Direction.north
    vertical_travel = 0
    horizontal_travel = 0
    locations_visited = {}
    found_hq = False

    for command in commands:
        # Turn
        if command[0] == 'L':
            current_direction = current_direction.left()
        elif command[0] == 'R':
            current_direction = current_direction.right()
        else:
            raise Exception("Direction '%s' not recognized" % command[0])

        # Walk
        travel_distance = int(command[1:])
        for i in range (0, travel_distance):
            if current_direction == Direction.north:
                vertical_travel = vertical_travel + 1
            elif current_direction == Direction.south:
                vertical_travel = vertical_travel - 1
            elif current_direction == Direction.east:
                horizontal_travel = horizontal_travel + 1
            elif current_direction == Direction.west:
                horizontal_travel = horizontal_travel - 1
            else:
                raise Exception("Direction '%s' not recognized" % current_direction)

            # At this moment, we are at a point in the map. It can be represented
            # by (X,Y) where X is horizontal_travel and Y is vertical_travel
            current_location = (horizontal_travel, vertical_travel)
            if found_hq is False and locations_visited.get(current_location):
                found_hq = True
                print("Visited the following location twice: %s" % str(current_location))
                total_distance_rabbit_hq = abs(vertical_travel) + abs(horizontal_travel)
                print("Total distance for the RabbitHQ location is: %s" % total_distance_rabbit_hq)
            locations_visited[current_location] = True

    total_distance_full_travel = abs(vertical_travel) + abs(horizontal_travel)
    print("Total distance for the full travel: %s" % total_distance_full_travel)

if __name__ == "__main__":
    main()
