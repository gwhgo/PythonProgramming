import threading,time
import _thread 

def client(numId):
    while True:
        time.sleep(1)
        print(numId)

for i in range(10):
    # Note: This will cause endless loop in the first thread
    threading.Thread(target=client,args=(i,)).run()

    _thread.start_new_thread(client,(i,))

#time.sleep(10)
