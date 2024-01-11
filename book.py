from app import details
import queue

max_size = 60

my_queue = queue.Queue(max_size)

my_queue.put(details)
