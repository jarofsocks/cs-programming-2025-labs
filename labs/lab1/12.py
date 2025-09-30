while True:
    word = input()
    if len(word) >= 10:
        break
print(word[:4], word[-2:], word[4::8], word[::-1])

        
