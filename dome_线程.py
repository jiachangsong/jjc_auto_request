import threading
from time import *
import logging
from MyThread import *

logging.basicConfig(level=logging.INFO)

loops = (2,4,3,3)
def loop(nloop,nsec):
    logging.info(f"start loop:{nloop} at{ctime()}")
    sleep(nsec)
    logging.info(f"end loop:{nloop} at{ctime()}")


def main():
    logging.info(f"start all at{ctime()}")
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        print(f"这里是i：{i}")
        th = MyThread(loop,(i,loops[i]),"11")
        threads.append(th)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()
    logging.info(f"end all at{ctime()}")

if __name__ == '__main__':
    main()