import threading
import random


class FileThread(threading.Thread):

    def __init__(self, file_count):
        threading.Thread.__init__(self)
        self.file_count = file_count

    def run(self):
        for i in range(1, self.file_count + 1):
            print(random.randint(1, 100))
            with open(f"file_{i}.txt", "x") as file:
                file.write(str(random.randint(1, 10)))


FileThread(6).start()
