class InductiveKB:
    def __init__(self):
        self.observations = []

    def observe(self, obs):
        self.observations.append(obs)

    def hypothesize(self):
        return [{"pattern": "inductive_hypothesis"}]