# core/monitor.py
import threading

class SystemMonitor(threading.Thread):
    def __init__(self, stop_event, stats_manager, total_orders):
        super().__init__(name="MONITOR")
        self.stop_event = stop_event
        self.stats_manager = stats_manager
        self.total_orders = total_orders

    def run(self):
        while not self.stop_event.is_set():
            stats = self.stats_manager.get_stats()
            pending = self.total_orders - stats['processed']
            active = sum(1 for t in threading.enumerate() if t.name.startswith("WORKER"))
            
            print(f"[MONITOR] Pending: {pending} | Approved: {stats['approved']} | Rejected: {stats['rejected']} | Failed: {stats['failed']} | Active Workers: {active}")
            
            # Bloqueo con timeout (espera 1.5s o se interrumpe)
            self.stop_event.wait(1.5)