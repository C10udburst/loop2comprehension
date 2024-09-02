# 1. File I/O with for loop
with open('file.txt', 'r') as file:
    for line in file:
        print(line.strip())

# 3. Sending HTTP requests
import requests

urls = ['http://example.com', 'http://example.org']
for url in urls:
    response = requests.get(url)
    print(response.status_code)

# 4. User input with while loop
while True:
    user_input = input("Enter something (type 'exit' to quit): ")
    if user_input == 'exit':
        break
    print(f'You entered: {user_input}')

# 5. Break out of a loop based on a condition
for i in range(10):
    if i == 5:
        break
    print(i)

# 6. Continue in a loop based on a condition
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# 7. Nested loops with complex logic
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for item in row:
        print(item)

# 9. Logging inside a loop
import logging

logging.basicConfig(level=logging.INFO)
for i in range(5):
    logging.info(f'Iteration {i}')


# 10. Creating a generator
def my_generator():
    n = 0
    while True:
        yield n
        n += 1


g = my_generator()
for _ in range(5):
    print(next(g))

# 11. Using loop with a set
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)

# 13. Generating multiple output files
for i in range(3):
    with open(f'file_{i}.txt', 'w') as file:
        file.write(f'This is file number {i}')

# 14. Calling an external API with error handling
api_urls = ['http://api1.com', 'http://api2.com']
for url in api_urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.json())
    except requests.RequestException as e:
        print(f'Error: {e}')

# 15. Web scraping
from bs4 import BeautifulSoup

html_docs = ['<html><body><p>doc1</p></body></html>', '<html><body><p>doc2</p></body></html>']
for doc in html_docs:
    soup = BeautifulSoup(doc, 'html.parser')
    print(soup.p.text)


# 17. Using loop with a database connection
import sqlite3

connection = sqlite3.connect('example.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, value TEXT)')
test_data = ['value1', 'value2', 'value3']
for value in test_data:
    cursor.execute('INSERT INTO test (value) VALUES (?)', (value,))
connection.commit()
for row in cursor.execute('SELECT * FROM test'):
    print(row)

# 18. Threading and Queues
import threading
import queue


def worker(q):
    while not q.empty():
        item = q.get()
        print(f'Processing: {item}')
        q.task_done()


q = queue.Queue()
for item in range(5):
    q.put(item)
for i in range(2):
    t = threading.Thread(target=worker, args=(q,))
    t.start()
q.join()

# 19. Using loop with a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f'{key}: {value}')

# 20. Complex data structures
complex_structure = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
for item in complex_structure:
    print(f"ID: {item['id']}, Name: {item['name']}")

# 21. State machine pattern
state = 'A'
while state != 'C':
    if state == 'A':
        print("State A")
        state = 'B'
    elif state == 'B':
        print("State B")
        state = 'C'

# 22. Dynamic imports with loop
modules = ['os', 'sys']
for module in modules:
    globals()[module] = __import__(module)
print(os.name)
print(sys.version)

# 23. Using coroutines
import asyncio


async def fetch_data():
    for i in range(5):
        print(f'Fetching data {i}')
        await asyncio.sleep(1)


asyncio.run(fetch_data())

# 24. Real-time data processing
import random
import time

while True:
    data = random.randint(1, 100)
    print(f'New data: {data}')
    time.sleep(1)
    if data > 90:
        break

# 25. Infinite loop with signal handling
import signal


def handler(signum, frame):
    print("Signal handler called")
    raise SystemExit('Exiting...')


signal.signal(signal.SIGINT, handler)
while True:
    print("Running... (press Ctrl+C to stop)")
    time.sleep(1)
