import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
# even local_var is first defined in __main__, it's a global variable
# use threading.local() to create a local variable
if True:
    def show_value(var):
        try:
            logging.debug('var at %r', var)
            logging.debug('value=%s', var.value)
        except AttributeError:
            logging.debug('no_value')
            

    def worker():
        show_value(local_var)

    if __name__ == "__main__":
        local_var = threading.local()
        local_var.value = 1000
        show_value(local_var)
        
        for i in xrange(2):
            t = threading.Thread(target=worker)
            t.start()

time.sleep(.5)
print

if True:
    def show_value(var):
        logging.debug('value = %s', var)
        
    def worker():
        show_value(local_var)
        
    if __name__ == "__main__":
        local_var = 1000
        show_value(local_var)
        
        for i in xrange(2):
            t = threading.Thread(target=worker)
            t.start()
