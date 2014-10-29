from threading import Thread
import time


def envia_comando():
    time.sleep(5)
    print "I'm in thread'"


def main():
        th = Thread(target=envia_comando)
        th.setDaemon(False)
        th.start()
        print "I'm in the main thread"
        th.join(10)

if __name__ == '__main__':
    main()
