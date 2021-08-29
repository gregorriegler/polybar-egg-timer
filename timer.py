from datetime import timedelta


class Timer:

    def __init__(self, value=60, notify=None):
        self.__value = value
        self.__notify = notify
        self.__running = False

    def start(self, when):
        self.__start = when
        self.__running = True

    def pause(self, when):
        self.__running = False
        self.__value = self.__seconds_left(when)

    def time(self, when):
        if(not self.__running):
            return mmss(self.__value)

        result = self.__seconds_left(when)
        if(result == 0 and self.__notify):
            self.__notify()

        return mmss(result)

    def __seconds_left(self, when):
        return max(self.__value - (when - self.__start), 0)


def mmss(seconds):
    td = timedelta(seconds=seconds)
    return str(td)[2:]
