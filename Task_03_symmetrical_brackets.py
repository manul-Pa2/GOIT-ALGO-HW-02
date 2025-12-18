def check_delimiters(s: str) -> str:      # створюю словник незачинених дужок
    pairs = {')': '(', ']': '[', '}': '{'}
    opening = set(pairs.values())
    stack = []

    for ch in s:
        if ch in opening:
            stack.append(ch)            # push
        elif ch in pairs:
            if not stack:
                return "Несиметрично"      # зайва закриваюча дужка
            top = stack.pop()            # pop
            if top != pairs[ch]:
                return "Несиметрично"     # неправильна пара типів, напр. ( }
    return "Симетрично" if not stack else "Несиметрично"     # якщо лишились відкриті
 
# Testing 
examples = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }",
]
for e in examples:
    print(f"{e}: {check_delimiters(e)}")
