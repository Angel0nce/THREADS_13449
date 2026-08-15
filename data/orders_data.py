# Seed list with at least 20 orders for simulation testing

ORDERS_LIST = [
    # Normal orders (CP-01)
    {"id": "ORD-001", "customer": "Ana López", "items": {"P001": 1}},
    {"id": "ORD-002", "customer": "Mario Pérez", "items": {"P002": 2}},
    {"id": "ORD-003", "customer": "Carlos Gómez", "items": {"P003": 1, "P004": 1}},
    {"id": "ORD-004", "customer": "Lucía Fernández", "items": {"P001": 2}},
    {"id": "ORD-005", "customer": "Roberto Díaz", "items": {"P002": 1}},

    # Contention orders for P005 Monitor (CP-02) - Stock = 6
    {"id": "ORD-006", "customer": "Elena Torres", "items": {"P005": 3}},
    {"id": "ORD-007", "customer": "Diego Ruiz", "items": {"P005": 3}},
    {"id": "ORD-008", "customer": "Sofia Morales", "items": {"P005": 2}}, # Should be rejected

    # Out of stock orders (CP-03)
    {"id": "ORD-009", "customer": "Gabriel Castro", "items": {"P004": 10}}, # Needs 10, only 8 available
    {"id": "ORD-010", "customer": "Valeria Silva", "items": {"P003": 15}},  # Needs 15, only 10 available

    # Malformed/Invalid orders (CP-04)
    {"id": "ORD-011", "customer": "Pedro Marmol", "items": {}}, # Empty items
    {"id": "ORD-012", "customer": "Invalid Customer", "items": {"P999": 1}}, # Non-existent product
    {"id": "ORD-013", "customer": "Zero Qty", "items": {"P001": 0}}, # Quantity 0

    # Remaining normal orders to complete at least 20
    {"id": "ORD-014", "customer": "Jorge Mendoza", "items": {"P002": 3}},
    {"id": "ORD-015", "customer": "Patricia Aguilar", "items": {"P001": 1, "P003": 1}},
    {"id": "ORD-016", "customer": "Fernando Ortiz", "items": {"P002": 2}},
    {"id": "ORD-017", "customer": "Camila Vargas", "items": {"P004": 1}},
    {"id": "ORD-018", "customer": "Esteban Ramos", "items": {"P001": 1}},
    {"id": "ORD-019", "customer": "Daniela Cruz", "items": {"P003": 2}},
    {"id": "ORD-020", "customer": "Alejandro Reyes", "items": {"P002": 1}},
]