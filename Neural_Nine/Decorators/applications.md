# Where to use Decorators?

1. Loggen von Aufrufen
2. Zugriffskontrolle/Authentifizierung
3. Caching von Ergebnissen
4. Timing von Funktionen
5. Validierung von Eingaben
6. Singleton-Pattern Implementierung
7. Dekorieren von Klassenmethoden
8. Funktionswiederholung bei Fehlern

Die Beispiele lassen sich in den unteren Blöcken finden:

## 1. Loggen von Aufrufen

```python
import functools

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(2, 3)
```

## 2. Zugriffskontrolle/Authentifizierung

```python
def requires_permission(permission):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if not user.has_permission(permission):
                raise PermissionError(f"User does not have {permission} permission")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@requires_permission('edit')
def edit_document(user, document_id):
    print(f"Document {document_id} has been edited by {user.name}")
```

## 3. Caching von Ergebnissen

```python
def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(35))
```

## 4. Timing von Funktionen

```python
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    return "Finished"

slow_function()
```

## 5. Validierung von Eingaben

```python
def validate_non_negative(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if any(arg < 0 for arg in args):
            raise ValueError("Negative values are not allowed")
        return func(*args, **kwargs)
    return wrapper

@validate_non_negative
def calculate_square_root(x):
    return x ** 0.5

print(calculate_square_root(9))
```

## 6. Singleton-Pattern Implementierung

```python
def singleton(cls):
    instances = {}
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class DatabaseConnection:
    def __init__(self):
        print("Connecting to database...")

db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)  # True
```

## 7. Dekorieren von Klassenmethoden

```python
def class_method_decorator(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        print(f"Calling method {method.__name__} of {self.__class__.__name__}")
        return method(self, *args, **kwargs)
    return wrapper

class MyClass:
    @class_method_decorator
    def my_method(self):
        print("Executing my_method")

obj = MyClass()
obj.my_method()
```

## 8. Funktionswiederholung bei Fehlern

``` python
def retry(exceptions, tries=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(tries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt + 1 == tries:
                        raise
        return wrapper
    return decorator

@retry((ValueError, TypeError), tries=3)
def do_something_risky():
    import random
    if random.choice([True, False]):
        raise ValueError("Failed!")
    return "Success"

print(do_something_risky())
```
