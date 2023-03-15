import threading
import time


def thread_function(ttl):
    name = threading.current_thread().getName()
    print("[Thread %s] starts" % (name))
    time.sleep(ttl)
    print("[Thread %s] diiied" % name)


if __name__ == "__main__":
    print("[Thread Main] start ---")
    luke = threading.Thread(target=thread_function, name="luke", args=(5,))
    darthvader = threading.Thread(target=thread_function, name="darthvader", args=(10,))
    luke.start()
    darthvader.start()

    print("[Thread Main] end -----")
