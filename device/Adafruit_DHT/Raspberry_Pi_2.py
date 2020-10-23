from . import common
from . import Raspberry_Pi_2_Driver as driver

def read(sensor, pin):
    # Validate pin is a valid GPIO.
    if pin is None or int(pin) < 0 or int(pin) > 31:
        raise ValueError('Pin must be a valid GPIO number 0 to 31.')
    # Get a reading from C driver code.
    result, humidity, temp = driver.read(sensor, int(pin))
    if result in common.TRANSIENT_ERRORS:
        # Signal no result could be obtained, but the caller can retry.
        return (None, None)
    elif result == common.DHT_ERROR_GPIO:
        raise RuntimeError('Error accessing GPIO.')
    elif result != common.DHT_SUCCESS:
        # Some kind of error occured.
        raise RuntimeError('Error calling DHT test driver read: {0}'.format(result))
    return (humidity, temp)
