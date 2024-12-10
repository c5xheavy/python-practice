import multiprocessing
import time
import codecs

def process_a(queue_a_in, queue_ab):
    while True:
        try:
            msg = queue_a_in.get(True)
            lower_msg = msg.lower()
            queue_ab.put(lower_msg)
            print(f"Process A: {time.strftime('%Y-%m-%d %H:%M:%S')} - Received '{msg}', sent '{lower_msg}' to B")
            time.sleep(5)
        except KeyboardInterrupt:
            break

def process_b(queue_ab, queue_b_out):
    while True:
        try:
            msg = queue_ab.get(True)
            rot13_msg = codecs.encode(msg, 'rot13')
            queue_b_out.put(rot13_msg)
            print(f"Process B: {time.strftime('%Y-%m-%d %H:%M:%S')} - Received '{msg}', sent '{rot13_msg}' to main")
            print(f"Process B stdout: {time.strftime('%Y-%m-%d %H:%M:%S')} - {rot13_msg}")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    queue_a_in = multiprocessing.Queue()
    queue_ab = multiprocessing.Queue()
    queue_b_out = multiprocessing.Queue()

    process_a_instance = multiprocessing.Process(target=process_a, args=(queue_a_in, queue_ab))
    process_b_instance = multiprocessing.Process(target=process_b, args=(queue_ab, queue_b_out))

    process_a_instance.start()
    process_b_instance.start()

    try:
        with open("interaction_log.txt", "w") as log_file:
            while True:
                user_input = input("Enter message or 'quit': ")
                if user_input.lower() == 'quit':
                    break
                queue_a_in.put(user_input)
                print(f"Main: {time.strftime('%Y-%m-%d %H:%M:%S')} - Sent '{user_input}' to A")
                log_file.write(f"Main: {time.strftime('%Y-%m-%d %H:%M:%S')} - Sent '{user_input}' to A\n")

                try:
                    received_msg = queue_b_out.get(True, 10)
                    print(f"Main: {time.strftime('%Y-%m-%d %H:%M:%S')} - Received '{received_msg}' from B")
                    log_file.write(f"Main: {time.strftime('%Y-%m-%d %H:%M:%S')} - Received '{received_msg}' from B\n")

                except multiprocessing.Queue.Empty:
                    print(f"Main: {time.strftime('%Y-%m-%d %H:%M:%S')} - Queue B is empty.")
                    log_file.write(f"Main: {time.strftime('%Y-%m-%d %H:%M:%S')} - Queue B is empty.\n")

    except KeyboardInterrupt:
        pass
    finally:
        process_a_instance.terminate()
        process_b_instance.terminate()
