class SafetyChecker:

    def __init__(self, ttc_threshold=2.0):
        self.ttc_threshold = ttc_threshold

    def check_ttc(self, ttc):
        return ttc > self.ttc_threshold

    def collision_detected(self, collision_flag):
        return collision_flag
