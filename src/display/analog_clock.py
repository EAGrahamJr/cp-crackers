import math
import time

import displayio
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.line import Line


class Clock:
    def __init__(self, radius: int = 16, x: int = 0, y: int = 0, color: int = 0xFFFFFF):
        self.radius = radius
        self.center_x = radius + x
        self.center_y = radius + y

        self._tick = radius / 8
        self._hl = radius / 2
        self._ml = radius - 2 * self._tick

        # Create a group to hold clock elements
        clock_group = displayio.Group()

        # Draw the clock face (circle)
        self._color = color

        clock_face = Circle(radius, radius, radius - 1, outline=self._color)
        clock_group.append(clock_face)

        # Draw tick marks (every 5 minutes)
        for minute in range(0, 60, 5):
            angle = (minute / 60) * 2 * 3.14159
            x1 = radius + int(self._ml * math.cos(angle))
            y1 = radius + int(self._ml * math.sin(angle))
            x2 = radius + int((radius - self._tick) * math.cos(angle))
            y2 = radius + int((radius - self._tick) * math.sin(angle))
            tick_mark = Line(x1, y1, x2, y2, color=self._color)
            clock_group.append(tick_mark)

        self._group = clock_group
        self._start_size = len(clock_group)

    def get_group(self):
        return self._group

    def update(self):
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min

        group = self._group
        if len(group) > self._start_size:
            group.pop()
            group.pop()

        # Draw hour hand
        hour_angle = (hour % 12 + minute / 60) * 30
        hour_x = int(self._hl * math.cos(math.radians(hour_angle - 90)))
        hour_y = int(self._hl * math.sin(math.radians(hour_angle - 90)))
        hour_hand = Line(
            self.center_x,
            self.center_y,
            self.center_x + hour_x,
            self.center_y + hour_y,
            color=self._color,
        )
        group.append(hour_hand)

        # Draw minute hand
        minute_angle = minute * 6
        minute_x = int(self._ml * math.cos(math.radians(minute_angle - 90)))
        minute_y = int(self._ml * math.sin(math.radians(minute_angle - 90)))
        minute_hand = Line(
            self.center_x,
            self.center_y,
            self.center_x + minute_x,
            self.center_y + minute_y,
            color=self._color,
        )
        group.append(minute_hand)
