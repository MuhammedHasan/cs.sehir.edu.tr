# TODO: Write it as tag


class Countur:

    def __init__(self):
        self.number = 0

    def increase(self):
        self.number += 1
        return self.number

    def restart(self):
        self.number = 0
        return ''
