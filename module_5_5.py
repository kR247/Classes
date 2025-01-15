class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(int(password))
        self.age = int(age)


class Video:
    def __init__(self, title, duration, time_now, adult_mode):
        self.title = title
        self.duration = int(duration)
        self.time_now = time_now
        self.adult_mode = bool(adult_mode)