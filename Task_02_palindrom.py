from collections import deque

def is_palindrome(text: str) -> bool:
    # 1) прибираємо пробіли і зводимо до нижнього регістру
    cleaned = "".join(ch.lower() for ch in text if not ch.isspace())

    # 2) кладемо всі символи в deque
    d = deque(cleaned)

    # 3) порівнюємо з двох кінців
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False

    return True


# test
print(is_palindrome("Anna"))                 # True
print(is_palindrome("А роза упала на лапу Азора"))  # True
print(is_palindrome("hello"))                # False
