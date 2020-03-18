from time import sleep
import signal, os
import sys

print('My PID is:', os.getpid())

def terminateProcess(signal, frame):
    print('обработчик сигнала')
    sys.exit()

def main():
    try:
        print ("Hello")
        i = 0
        while True:
            i += 1
            print ("Iteration #%i" % i)
            sleep(5)
    finally:
        print ("Goodbye")



if __name__ == '__main__':
    signal.signal(signal.SIGTERM, terminateProcess)
    main()


# $ kill -SIGTERM 12345