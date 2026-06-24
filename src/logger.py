class Logger:
    def __init__(self):
        self.logs = []

    def log(self, msg):
        print(msg)
        self.logs.append(msg)

    def get_logs(self):
        return self.logs