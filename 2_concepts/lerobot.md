# LeRobot

- use `find_motors_bus_port.py` to find the device
- use `configure_motor.py` to set ids for motors:
    - sends our defined ID via serial to be stored in a known EEPROM address
    - this ID can be retrieved from this EEPROM address (where the ID is stored) so we know which motor state belongs to which motor when they are daisy chained together
- 