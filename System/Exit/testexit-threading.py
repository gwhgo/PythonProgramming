import threading, sys, time, os

def action():
    print("thread action")
    #sys.exit()
    os._exit(0)
    print('not reached')


threading.Thread(target=action).start()

time.sleep(2)
print('Main exit')
