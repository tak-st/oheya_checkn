import mh_z19
import time

def get_co2():
    out = mh_z19.read_all()
    val = out["co2"]

    return val
