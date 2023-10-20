# Find the first non-repeated character in a string:
from collections import Counter

def non_repet_char(inp_string):
    char_count=Counter(inp_string)
    # print(char_count)
    for char in inp_string:
        if char_count[char]==1:
            return char
    return None


inp_string=input("Enter string:")
result=non_repet_char(inp_string)
if result:
    print("first non rep char is:",result)
else:
    print("no non-repete char")