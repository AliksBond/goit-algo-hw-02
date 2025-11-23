from queue import Queue
import time

queue = Queue()
request_number = 1

def generate_request():
    global request_number
    request = f"Заявка №{request_number}"
    queue.put(request)
    print(f"[+] Створено: {request}")
    request_number += 1

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"[✔] Обробляється: {request}")
    else:
        print("[!] Черга порожня")

def main():
    print("Система запуску заявок (Ctrl+C — зупинка)\n")
    try:
        while True:
            generate_request()
            process_request()
            time.sleep(1)
            print()
    except KeyboardInterrupt:
        print("\nЗавершено користувачем.")

if __name__ == "__main__":
    main()
