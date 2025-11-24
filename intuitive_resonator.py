class IntuitiveKB:
    def __init__(self):
        self.experiences = []

    def observe(self, exp):
        self.experiences.append(exp)

    def snap_judgment(self, situation):
        return {"judgment": "intuitive_feeling"}