import pyautogui
from threading import Timer
from time import sleep

width, height = pyautogui.size()
middleWidth = width / 2
middleHeight = height / 2
leftXLimit = middleWidth / 2
rightXLimit = middleWidth + leftXLimit
class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

def moveMouse():
    for i in range(4):
        pyautogui.moveTo(leftXLimit,middleHeight,duration=0.25)
        pyautogui.moveTo(rightXLimit,middleHeight,duration=0.25)

def main():
    print('Press Ctrl-C to quit.')
    moveMouseTimer = None
    try:
        while True:
            lastXPos = pyautogui.position().x
            lastYPos = pyautogui.position().y
            sleep(1)
            x, y = pyautogui.position()
            if lastXPos == x and lastYPos == y:
                if moveMouseTimer is None:
                    moveMouseTimer = RepeatedTimer(14, moveMouse) # Timer creation
                elif not moveMouseTimer.is_running:
                    moveMouseTimer.start() # Stating Timer
            elif moveMouseTimer.is_running:
                if y != middleHeight or x < leftXLimit or x > rightXLimit:
                    moveMouseTimer.stop() # Stopping Timer
    except KeyboardInterrupt:
        moveMouseTimer.stop()
        print('\n')

if __name__ == "__main__":
    main()
