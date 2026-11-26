from time import sleep

from adafruit_motor.servo import Servo


class RotoServo:
    """
    Steps a servo to a desired angle using a specified speed.
    """

    def __init__(self, servo: Servo, speed: float = 0.025) -> None:
        """Initialize the RotoServo with a servo and optional speed.

        Args:
            servo (Servo): the servo to control
            speed (float, optional): the speed to use for stepping. Defaults to 0.025.
        """
        self._servo = servo
        self._speed = speed
        servo.angle = 0

    @property
    def speed(self) -> float:
        """The amount of "time" to sleep between steps (defaults to .025)

        Returns:
            float: pause time
        """
        return self._speed

    @speed.setter
    def speed(self, howFast: float = 0.025):
        """Sets the "speed"

        Args:
            howFast (float, optional): the speed to use. Defaults to 0.025.
        """
        self._speed = howFast

    @property
    def angle(self) -> float | None:
        """Get the current angle of the servo

        Returns:
            float: current angle of the servo
        """
        return self._servo.angle

    @angle.setter
    def angle(self, angle: int):
        """Move the servo to this angle. Note this will "step"
        the servo using the speed property.

        Args:
            angle (int): the desired angle
        """
        servo = self._servo
        current = round(servo.angle) if servo.angle else 0
        if angle == current:
            return

        delta = 1 if angle > current else -1
        for i in range(current, angle, delta):
            servo.angle = i
            sleep(self._speed)

        # last step because the range is exclusive of the end value
        servo.angle = angle


def sg90(servo: Servo) -> RotoServo:
    """Wraps a servo in a "speed-controlled" class.

    Also sets the servo trim to appropriate values for an SG90.

    Args:
        servo (Servo): the servo to wrap

    Returns:
        RotoServo: speed-controlled, "stepping" servo
    """
    servo.set_pulse_width_range(500, 2400)
    return RotoServo(servo)


def mg90s(servo: Servo) -> RotoServo:
    """Wraps a servo in a "speed-controlled" class.

    Also sets the servo trim to appropriate values for an MG90S.
    Note that this may result in maximum angles > 180.

    Args:
        servo (Servo): the servo to wrap

    Returns:
        RotoServo: speed-controlled, "stepping" servo
    """
    servo.set_pulse_width_range(400, 2600)
    servo.actuation_range = 200
    return RotoServo(servo)


def mg996r(servo: Servo) -> RotoServo:
    """Wraps a servo in a "speed-controlled" class.

    Also sets the servo trim to appropriate values for an MG996R.
    Note that this may result in maximum angles > 180.

    Args:
        servo (Servo): the servo to wrap
    Returns:
        RotoServo: speed-controlled, "stepping" servo
    """
    servo.set_pulse_width_range(500, 2500)
    servo.actuation_range = 190
    return RotoServo(servo)
