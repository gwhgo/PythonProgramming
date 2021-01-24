import _thread as thread

stdoutmutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock() for i in range(10)]

def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myId,i))
        stdoutmutex.release()
    exitmutexes[myId].acquire() # signal main thread

for i in range(10):
    thread.start_new_thread(counter, (i,100))

# try commenting below 2 lines code, see what happen?
# would the last code in this script run?
for mutex in exitmutexes:
    while not mutex.locked(): pass

print('Main thread exiting.')
