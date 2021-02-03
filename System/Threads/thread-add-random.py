import threading, time
count = 0

def adder():
    global count
    count = count + 1
    # time.sleep(0.5)
    count = count + 1

threads = []
for i in range(10000):
    thread = threading.Thread(target=adder,args=())
    thread.start()
    threads.append(thread)

for thread in threads: thread.join()

# this output should be random, but is the same on my computer
print(count)
