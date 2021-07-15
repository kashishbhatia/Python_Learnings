
# example where both threads are sharing a variable


from threading import Thread
import time

a = 0  # global variable


def thread3(threadname):
    global a
    a=200
    print("I am %s ......." % threadname)

def thread1(threadname):
    global a
    for k in range(100):
        print("{} {}".format(threadname, a))
        time.sleep(0.1)
        if k == 5:
            a += 100
    call_func(thread3, "Thread-3")


def thread2(threadname):
    global a
    for k in range(10):
        print("{} {}".format(threadname, a))
        a += 1
        time.sleep(0.2)



def call_func(func, arg):
    thread1 = Thread(target=func, args=(arg,))

    thread1.start()

    thread1.join()

if __name__ == '__main__':
    call_func(thread1, "Thread-1")
    call_func(thread2, "Thread-2")
