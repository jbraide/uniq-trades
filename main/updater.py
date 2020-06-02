import time

def autoincr(val, numberOfTimes, timing):
    val = val
    for i in range(numberOfTimes):
        val += val * 0.15
        newValue = val
        print(newValue)
        time.sleep(timing)
    return newValue