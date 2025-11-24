from resonator import Resonator
import time

r = Resonator()
start = time.time()
result = r.process({'test': 'full_scale'})
elapsed = time.time() - start
print(f'Full Scale Test: Time {elapsed:.2f}s, Glyph {result["glyph"]}, Nodes {result["source_nodes"]}')