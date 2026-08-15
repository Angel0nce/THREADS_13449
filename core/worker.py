# core/worker.py
import threading
import queue
import time
import datetime
import random

class OrderWorker(threading.Thread):
    def __init__(self, worker_id, order_queue, inventory_manager, stats_manager):
        super().__init__(name=f"WORKER-{worker_id}")
        self.order_queue = order_queue
        self.inventory_manager = inventory_manager
        self.stats_manager = stats_manager

    def run(self):
        while True:
            try:
                # Extracción Thread-safe
                order = self.order_queue.get_nowait()
            except queue.Empty:
                break # Sale del bucle si no hay más pedidos

            curr_time = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
            print(f"[{curr_time}] [{self.name}] Processing order {order['id']} | Customer: {order['customer']}")
            
            # Simular trabajo fuera de la sección crítica (0.5 a 1.5 seg)
            time.sleep(random.uniform(0.5, 1.5))
            
            if not order.get('items'):
                status, reason = "FAILED", "Order contains no items"
            else:
                status, reason = self.inventory_manager.process_order_items(order['items'])
            
            curr_time = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
            if status == "APPROVED":
                print(f"[{curr_time}] [{self.name}] {order['id']} APPROVED | {reason}")
            else:
                print(f"[{curr_time}] [{self.name}] {order['id']} {status} | Reason: {reason}")
            
            # Actualización de contadores a través del manager
            self.stats_manager.update(status)
            self.order_queue.task_done()