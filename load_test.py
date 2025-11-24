from resonator import Resonator
import time
import threading

r = Resonator()

def test_request(i):
    start = time.time()
    result = r.process({'test': f'load_{i}'})
    elapsed = time.time() - start
    print(f'Request {i}: {elapsed:.2f}s, Glyph {result["glyph"]}')

threads = []
for i in range(10):
    t = threading.Thread(target=test_request, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f'Total requests: {r.request_count}, Errors: {r.error_count}')