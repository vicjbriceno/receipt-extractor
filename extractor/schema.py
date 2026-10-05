from typing import Literal

from pydantic import BaseModel


class LineItem(BaseModel):
    description: str
    quantity: float | None = None
    unit_price: float | None = None
    total: float


class Receipt(BaseModel):
    items: list[LineItem] | None = None
    commerce: str
    date: str | None = None
    currency: str | None = None
    subtotal: float | None = None
    tax: float | None = None
    tip: float | None = None
    total: float
    payment_method: str | None = None
    category: Literal["food", "groceries", "transport", "health", "other"] | None = None
