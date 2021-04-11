import threading
from threading import *


class MyThread(threading.Thread):
    def __init__(self,fun,args,name=''):
        threading.Thread.__init__(self)
        self.fun = fun
        self.args = args
        self.name = name

    def run(self):
        self.fun(*self.args)
