import pandas as pd


class MetricsLogger:

    def __init__(self):
        self.data = []

    def log(self, episode, collision, min_ttc, success):
        self.data.append({
            "episode": episode,
            "collision": collision,
            "min_ttc": min_ttc,
            "success": success
        })

    def save(self, path):
        df = pd.DataFrame(self.data)
        df.to_csv(path, index=False)
