# Podracer Class
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

# AnakinsPod Subclass
class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

# SebulbasPod Subclass
class SebulbasPod(Podracer):
    def flame_jet(self, other_pod):
        other_pod.condition = "trashed"

pod = Podracer(500, "perfect", 10000)
print(pod.condition)  # Output: perfect
pod.repair()
print(pod.condition)  # Output: repaired

anakins_pod = AnakinsPod(200, "perfect", 15000)
anakins_pod.boost()
print(anakins_pod.max_speed)  # Output: 400

sebulbas_pod = SebulbasPod(300, "trashed", 12000)
sebulbas_pod.flame_jet(anakins_pod)
print(anakins_pod.condition)  # Output: trashed