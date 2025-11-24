from resonator import Resonator

r = Resonator()
glyphs = []

for i in range(5):
    result = r.process({'test': f'data{i}'}, telemetry=True)
    glyph = result['glyph']
    glyphs.append(glyph)
    print(f'Request {i+1}: Glyph {glyph}, Reasoning nodes: {len(result.get("reasoning_path", []))}')

print(f'Total requests: {r.request_count}, Errors: {r.error_count}')
print(f'Unique glyphs: {len(set(glyphs))} == 5: {len(set(glyphs)) == 5}')

# Test error handling
try:
    r.process(None, telemetry=True)
except Exception as e:
    print(f'Error handled: {e}')
    print(f'Errors after: {r.error_count}')