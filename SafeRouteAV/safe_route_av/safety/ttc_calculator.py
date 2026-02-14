import numpy as np


class TTCCalculator:

    @staticmethod
    def compute(relative_distance, relative_velocity):
        if relative_velocity <= 0:
            return float("inf")
        return relative_distance / relative_velocity
