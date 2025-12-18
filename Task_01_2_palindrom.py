from collections import deque

def is_palindrome(s: str) -> bool:
    s = "".join(ch.lower() for ch in s if ch.isalnum())
    d = deque(s)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True
