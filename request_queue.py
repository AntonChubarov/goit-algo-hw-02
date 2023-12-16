from queue import Queue
from uuid import uuid4
from random import choice, randint, randbytes, uniform
from base64 import b64encode
from time import sleep

import threading
import sys
import logging

exit_event = threading.Event()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

request_queue = Queue()

command_names = ["run", "jump", "stop", "start", "pause", "resume", "reset", "exit", "save", "load", "help", "status"]


def run_generating_requests():
    while not exit_event.is_set():
        sleep(uniform(0.2, 0.5))

        req = {
            "id": str(uuid4()),
            "cmd": choice(command_names),
            "data": b64encode(randbytes(randint(32, 64))).decode("utf-8")
        }

        request_queue.put(req)


def run_processing_requests():
    while not exit_event.is_set():
        req = request_queue.get()

        sleep(uniform(0.2, 0.5))

        log.info(f"Queue size: {request_queue.qsize()}; Proceed request: {req}")


def main():
    generating_thread = threading.Thread(target=run_generating_requests)
    processing_thread = threading.Thread(target=run_processing_requests)

    generating_thread.start()
    processing_thread.start()

    try:
        while True:
            sleep(0.5)
    except KeyboardInterrupt:
        exit_event.set()

        generating_thread.join()
        processing_thread.join()

        print('Interrupted! Exiting...')

        sys.exit()


if __name__ == '__main__':
    main()
