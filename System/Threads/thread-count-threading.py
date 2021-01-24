"producer and consumer threads communicating with a shared queue"

numconsumers = 2        # how many consumers to start
numproducers = 4        # how many producers to start
nummessages = 4         # messages per producer to put


import _thread as thread, queue, time
safeprint = thread.allocate_lock()  # else prints may overlap
dataQueue = queue.Queue()           # shared global, infinite size

def producer(idnum):
    for msgnum in range(nummessages):
        time.sleep(idnum)
        dataQueue.put('[producer  id=%d, count=%d]' % (idnum, msgnum))

def consumer(idnum):
    while True:
        time.sleep(0.1)
        try:
            data = dataQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            with safeprint:
                print('consumer', idnum, 'got =>', data)
                
if __name__ == '__main__':
    for i in range(numconsumers):
        thread = threading.Thread(target=consumer, args=(i,dataQueue))
        thread.daemon = True
        thread.start()

    waitfor = []
    for i in range(numproducers):
        thread = threading.Thread(target=producer, args=(i, dataQueue))
        waitfor.append(thread)
        thread.start()

    
