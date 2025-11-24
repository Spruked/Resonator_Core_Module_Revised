from resonator_pyramid import ResonatorPyramid
import time

class Resonator:
    def __init__(self):
        self.pyramid = ResonatorPyramid()
        self.request_count = 0
        self.error_count = 0

    def process(self, input_data, telemetry=True):
        start = time.time()
        try:
            result = self.pyramid.distill(input_data)
            duration = time.time() - start
            if telemetry:
                self.request_count += 1
                print(f"Request {self.request_count}: {duration:.2f}s")
            return result
        except Exception as e:
            if telemetry:
                self.error_count += 1
            return {"error": str(e)}