import time


def refresh():
    secs = 0
    while secs < 10:
        print('sec: ' + str(secs))
        secs += 1
        try:
            time.sleep(1)
        except:
            continue