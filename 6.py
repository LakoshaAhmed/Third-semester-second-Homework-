import datetime
import functools

AUDIT_FILE = "audit_log.txt"

def audit_trail(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        operation = func.__name__
        timestamp = datetime.datetime.now().strftime("%d.%m %H:%M:%S")

        try:
            result = func(*args, **kwargs)

            arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
            arg_dict = dict(zip(arg_names, args))
            arg_dict.update(kwargs)
            if "self" in arg_dict:
                del arg_dict["self"]

            args_str = ", ".join(f"{k}={v}" for k, v in arg_dict.items())

            with open(AUDIT_FILE, "a") as f:
                f.write(f"{timestamp} operation: {operation}; status: SUCCESS; arguments: {args_str}\n")

            return result

        except Exception as e:
            with open(AUDIT_FILE, "a") as f:
                f.write(f"{timestamp} operation: {operation}; status: FAIL; Exception: {type(e).__name__}\n")
            raise 
    return wrapper
class BankAccount:
    @audit_trail
    def withdraw(self, owner, amount):
        if amount > 100:
            raise Exception("WithdrawalException")  
        print(f"{owner} withdrew {amount} units.")


if __name__ == "__main__":
    acc = BankAccount()
    acc.withdraw("Nick", amount=15)  
    try:
        acc.withdraw("Nick", amount=150)  
    except Exception:
        pass
