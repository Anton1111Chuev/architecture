from dataclasses import dataclass
from datetime import datetime


@dataclass
class Ticket:
    id: int
    departure_zone: int
    arrival_zone: int
    route_number: int
    departure_time: datetime
    arrival_time: datetime
    buyer_id: int
    is_used: bool
    price: float
    place: str


@dataclass
class Account:
    user_account_id: int
    balance: float


@dataclass
class User:
    id: int
    name: str
    tickets: list[Ticket]
    login: str
    password_hash_code: float
    account_id: float
