import datetime

def log_result(func):
    def decorator_func(*args):
        result = func(*args)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"Function launched at {timestamp} with result {result}"
        with open("log.txt", "a") as file:
            file.write(log_message + "\n")
        return result
    return decorator_func

@log_result
def calculate_sum(*args):
    return sum(args)

result = calculate_sum(1, 2, 3, 4)
