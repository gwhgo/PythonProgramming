import threading
from time import sleep
def server():
    while True:
        sleep(3)
        print('server is waiting')

if __name__ == '__main__':
    thread = threading.Thread(target=server)
    thread.daemon = True
    thread.start()
    print("Now we end the main thread")
