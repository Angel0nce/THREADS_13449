# Thread-safe statistics tracker for simulation progress

import threading

class SimulationStats:
    def __init__(self):
        self.approved = 0
        self.rejected = 0
        self.failed = 0
        self.lock = threading.Lock()

    def increment_approved(self):
        with self.lock:
            self.approved += 1

    def increment_rejected(self):
        with self.lock:
            self.rejected += 1

    def increment_failed(self):
        with self.lock:
            self.failed += 1

    def get_summary(self):
        with self.lock:
            return {
                "approved": self.approved,
                "rejected": self.rejected,
                "failed": self.failed,
                "total_processed": self.approved + self.rejected + self.failed
            }
