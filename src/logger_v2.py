class LoggerV2:

    def __init__(self):
        self.logs = []

    def log(self, msg):
        self.logs.append(msg)
        print("📝", msg)

    def get_logs(self):
        return self.logs