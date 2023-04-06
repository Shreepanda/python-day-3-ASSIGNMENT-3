def alternate_merge(s1: str, s2: str) -> str:
    merged_str = ""
    min_len = min(len(s1), len(s2))
    
    for i in range(min_len):
        merged_str += s1[i] + s2[i]
    
    if len(s1) > min_len:
        merged_str += s1[min_len:]
    elif len(s2) > min_len:
        merged_str += s2[min_len:]
    
    
    return merged_str


def count_vowels(s: str) -> int:
    
    vowels = set("aeiouAEIOU")
    vowel_count = 0
    for char in s:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

S1 = "welcome"
S2 = "Homely"
index = 1

merged_str = alternate_merge(S1, S2)
vowel_count = count_vowels(merged_str)

print("Merged string:", merged_str)
print("Vowel count:", vowel_count)
print("Character at index {}: {}".format(index, merged_str[index]))
