from queue import Queue
import itertools

request_queue = Queue()
counter = itertools.count(1)

def generate_request():
    req = {"id": next(counter)}
    request_queue.put(req)
    print(f"Згенеровано заявку #{req['id']}")

def process_request():
    if not request_queue.empty():
        req = request_queue.get()
        print(f"Обробляємо заявку #{req['id']}")
    else:
        print("Черга пуста — немає заявок для обробки")
