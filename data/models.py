from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class Order:
    order_id: str
    customer_name: str
    items: Dict[str, int]  # Dict of {product_code: quantity}
    status: str = "PENDING"  # PENDING, APPROVED, REJECTED, INVALID
    rejection_reason: Optional[str] = None
    processed_by: Optional[str] = None