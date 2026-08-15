# core/inventory_manager.py
import threading
from data.inventory import INITIAL_INVENTORY

class InventoryManager:
    def __init__(self):
        # Hacemos una copia profunda superficial para no alterar el original
        self.inventory = {k: v.copy() for k, v in INITIAL_INVENTORY.items()}
        self.lock = threading.Lock()
    
    def process_order_items(self, items):
        # PROTECCIÓN DE LA SECCIÓN CRÍTICA (MUTEX)
        with self.lock:
            # 1. Validación de stock (Atomicidad)
            for p_code, qty in items.items():
                if p_code not in self.inventory:
                    return "FAILED", f"Product {p_code} does not exist"
                if qty <= 0:
                    return "FAILED", f"Invalid quantity ({qty}) requested for {p_code}"
                if self.inventory[p_code]['stock'] < qty:
                    return "REJECTED", f"Insufficient stock for product {p_code} (Requested: {qty}, Available: {self.inventory[p_code]['stock']})"
            
            # 2. Descuento de stock si todo es válido
            for p_code, qty in items.items():
                self.inventory[p_code]['stock'] -= qty
            
            return "APPROVED", f"Items: {items}"