from time import sleep
import signal, os
import sys

print('My PID is:', os.getpid())

def handle_exit(signal, frame):
    print('lol')

def main():
    signal.signal(signal.SIGTERM, handle_exit)
    try:
        print ("Hello")
        i = 0
        while True:
            i += 1
            print ("Iteration #%i" % i)
            sleep(1)
    finally:
        print ("Goodbye")



if __name__ == '__main__':
    main()


# $ kill -SIGTERM 12345