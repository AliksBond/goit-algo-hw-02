from collections import deque

def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    dq = deque(cleaned)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

s = input("Введіть рядок: ")
print("Паліндром" if is_palindrome(s) else "Не паліндром")
