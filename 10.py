from dataclasses import dataclass, field
from enum import Enum
from typing import List, Union
from datetime import datetime



class AssetType(Enum):
    CURRENCY = "Currency"
    CRYPTOCURRENCY = "Cryptocurrency"


class WithdrawalException(Exception):
    pass


def audit_trail(func):
   
    def wrapper(*args, **kwargs):
        print(f"[AUDIT] Calling {func.__name__} with args={args[1:]}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[AUDIT] Completed {func.__name__}")
        return result
    return wrapper


@dataclass
class Currency:
    name: str
    symbol: str


@dataclass
class Cryptocurrency:
    name: str
    symbol: str



@dataclass
class AssetManager:
  
    id: int
    asset_type: AssetType
    asset: Union[Currency, Cryptocurrency]
    balance: float = 0.0
    transaction_history: List[dict] = field(default_factory=list)

    @audit_trail
    def deposit(self, amount: float) -> None:
    
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self._add_transaction("DEPOSIT", amount)

    @audit_trail
    def withdraw(self, amount: float) -> None:
      
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise WithdrawalException("Insufficient funds for withdrawal.")
        self.balance -= amount
        self._add_transaction("WITHDRAW", amount)

    def _add_transaction(self, transaction_type: str, amount: float) -> None:
       
        self.transaction_history.append({
            "type": transaction_type,
            "amount": amount,
            "timestamp": datetime.now().isoformat(),
            "balance_after": self.balance
        })


rub = Currency(name="ruble", symbol="rub")
btc = Cryptocurrency(name="Bitcoin", symbol="BTC")

fiat_account = AssetManager(id=1, asset_type=AssetType.CURRENCY, asset=rub)
crypto_account = AssetManager(id=2, asset_type=AssetType.CRYPTOCURRENCY, asset=btc)

fiat_account.deposit(500.00)
crypto_account.deposit(0.25)

fiat_account.withdraw(200.00)

try:
    crypto_account.withdraw(1.0)
except WithdrawalException as e:
    print(f"Error: {e}")

print("\n Account Balances ")
print(f"Fiat Account Balance: {fiat_account.balance} {fiat_account.asset.symbol}")
print(f"Crypto Account Balance: {crypto_account.balance} {crypto_account.asset.symbol}")

print("\n Fiat Account Transaction History ")
for tx in fiat_account.transaction_history:
    print(tx)

print("\n Crypto Account Transaction History ")
for tx in crypto_account.transaction_history:
    print(tx)
