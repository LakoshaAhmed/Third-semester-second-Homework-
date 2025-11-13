### `TransactionHistory` part 1 (1.5 points)


#Implement the `TransactionHistory` class. He must:
#- correctly store a list of transactions in the **private** attribute
#- have a simple constructor (sets a list of transactions `[]`)
#- have an initializer `from_list`, which creates based on a list of transactions
#- have a `from_json` initializer that creates an instance based on a long string that reflects a list of strings of the type that are needed for the `from_dict` of the `Transaction` class (essentially from JSON)
#- have an initializer `from_file`, which creates an instance based on a file (the path to the file is passed to the function).
#- have a `to_json` method, which converts the list into the required form
#- have a `to_file` method that saves JSON to a file whose name is passed to the method
import json
from typing import List, Any, Optional
from datetime import datetime


class TransactionHistory:
    def __init__(self, file_path: Optional[str] = None):
        self.__transactions = []
        self.file_path = file_path 

    @classmethod
    def from_list(cls, transactions: List[Any]) -> 'TransactionHistory':
        instance = cls()
        instance.__transactions = transactions.copy()
        return instance

    @classmethod
    def from_json(cls, json_str: str, transaction_class: Optional[Any] = None) -> 'TransactionHistory':
        data = json.loads(json_str)
        transactions = []
        if transaction_class is not None:
            for t in data:
                transactions.append(transaction_class.from_dict(t))
        else:
            transactions = data
        return cls.from_list(transactions)

    @classmethod
    def from_file(cls, file_path: str, transaction_class: Optional[Any] = None) -> 'TransactionHistory':
        with open(file_path, "r", encoding="utf-8") as f:
            json_str = f.read()
        instance = cls.from_json(json_str, transaction_class)
        instance.file_path = file_path
        return instance

    def add_transaction(self, transaction: Any) -> None:
        self.__transactions.append(transaction)
    
    def get_transactions(self) -> List[Any]:
        return self.__transactions.copy()

    def to_json(self) -> str:
        json_ready = [
            t.to_dict() if hasattr(t, "to_dict") else t for t in self.__transactions
        ]
        return json.dumps(json_ready, ensure_ascii=False, indent=4)

    def to_file(self, file_path: Optional[str] = None) -> None:
        path = file_path or self.file_path
        if not path:
            raise ValueError("No file path specified for saving transaction history.")
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.to_json())

    def __len__(self) -> int:
        return len(self.__transactions)
    
    def __repr__(self) -> str:
        return f"TransactionHistory(transactions_count={len(self.__transactions)})"

    @property
    def turnover(self) -> float:
        """Total revenue (sum of all incoming transactions)."""
        total = 0.0
        for t in self.__transactions:
            type_ = getattr(t, "type", None) or (t.get("type") if isinstance(t, dict) else None)
            amount = getattr(t, "amount", None) or (t.get("amount") if isinstance(t, dict) else None)
            if type_ == "income" and isinstance(amount, (int, float)):
                total += amount
        return total

    @property
    def profits(self) -> float:
        """Operating profit = income - expenses."""
        income = 0.0
        expenses = 0.0
        for t in self.__transactions:
            type_ = getattr(t, "type", None) or (t.get("type") if isinstance(t, dict) else None)
            amount = getattr(t, "amount", None) or (t.get("amount") if isinstance(t, dict) else None)
            if isinstance(amount, (int, float)):
                if type_ == "income":
                    income += amount
                elif type_ == "expense":
                    expenses += amount
        return income - expenses

    def __enter__(self) -> 'TransactionHistory':
        """Open transaction file and log entry."""
        if not self.file_path:
            raise ValueError("file_path must be set before using TransactionHistory as a context manager.")
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                json_str = f.read()
            data = json.loads(json_str)
            self.__transactions = data
        except FileNotFoundError:
            self.__transactions = []  

        self.__log_event(f"{self.file_path} TransactionHistory opened")

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Save transactions and log closing status."""
        status = "SUCCESS"
        reason = ""
        message = ""

        if exc_type:
            status = "FAIL"
            reason = exc_type.__name__
            message = str(exc_val)

        try:
            self.to_file()
        except Exception as e:
            self.__log_event(f"{self.file_path} TransactionHistory save failed: {e}")
            raise

        if status == "SUCCESS":
            self.__log_event(f"{self.file_path} TransactionHistory closed; status: SUCCESS")
        else:
            self.__log_event(
                f"{self.file_path} TransactionHistory closed; status: FAIL; "
                f"reason: {reason}; message: {message}"
            )

        return False

    def __log_event(self, message: str) -> None:
        """Append a formatted log message with timestamp."""
        timestamp = datetime.now().strftime("%d.%m %H:%M:%S")
        with open("transaction_logs.log", "a", encoding="utf-8") as log_file:
            log_file.write(f"{timestamp} {message}\n")



class Transaction:
    def __init__(self, amount, type_):
        self.amount = amount
        self.type = type_

    def to_dict(self):
        return {"amount": self.amount, "type": self.type}

    @classmethod
    def from_dict(cls, d):
        return cls(d["amount"], d["type"])


file_path = "transactions.json"

try:
    with TransactionHistory(file_path) as history:
        history.add_transaction({"amount": 1000, "type": "income"})
        history.add_transaction({"amount": 200, "type": "expense"})
        print("Turnover:", history.turnover)
        print("Profits:", history.profits)
       
except Exception as e:
    print("Error during transaction session:", e)

