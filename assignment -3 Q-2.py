def length_of_last_word(s: str) -> int:
    s = s.rstrip()
    last_space_index = s.rfind(' ')
    if last_space_index == -1:
        return len(s)
    return len(s) - last_space_index - 1
s = "Hello World"
print(length_of_last_word(s))
