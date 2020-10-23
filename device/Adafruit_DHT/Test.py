from . import common
from . import Test_Driver as driver

def read(sensor, pin):
    # Get a reading from C driver code.
    result, humidity, temp = driver.read(sensor, pin)
    if result in common.TRANSIENT_ERRORS:
        # Signal no result could be obtained, but the caller can retry.
        return (None, None)
    elif result != common.DHT_SUCCESS:
        # Some kind of error occured.
        raise RuntimeError('Error calling DHT test driver read: {0}'.format(result))
    return (humidity, temp)
