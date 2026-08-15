# Thread-safe statistics tracker for simulation progress

import threading

class StatsManager:
    def __init__(self):
        self.approved = 0
        self.rejected = 0
        self.failed = 0
        self.lock = threading.Lock()

    def update(self, status):
        with self.lock:
            if status == "APPROVED":
                self.approved += 1
            elif status == "REJECTED":
                self.rejected += 1
            elif status == "FAILED":
                self.failed += 1

    def get_stats(self):
        with self.lock:
            return {
                "approved": self.approved,
                "rejected": self.rejected,
                "failed": self.failed,
                "processed": self.approved + self.rejected + self.failed
            }
