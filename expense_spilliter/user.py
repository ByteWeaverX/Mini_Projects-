class User:
    def __init__(self, userid, name):
        self.userid = userid
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"User({self.userid}, {self.name})"
