import threading
import time
import logging as log

def thread_function(ttl):
    log.info('starts')
    time.sleep(ttl)
    log.info('diiied')

if __name__ == "__main__":
    format = "%(asctime)s [Thread-%(threadName)s]: %(message)s"
    log.basicConfig(format=format, 
                        level=log.INFO,
                        datefmt="%H:%M:%S")

    log.info("start ---")
    luke = threading.Thread(target=thread_function, name="luke", args=(5,))
    darthvader = threading.Thread(target=thread_function, name="darthvader", args=(10,))
    luke.start()
    darthvader.start()

    log.info ("end -----")