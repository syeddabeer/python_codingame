def encode_char(char, place):
    if char.isalpha(): 
        gap = 65 if char.isupper() else 97
        return(chr((((ord(char) - gap) + place) % 26) + gap))
    else:
        return char
    

place = int(input())
msg = input()
# place = 3
# msg = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

encode = lambda string: encode_char(string, place)

print("".join(map(encode, msg)))