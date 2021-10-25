# Apply the algorithm: https://oeis.org/wiki/Balanced_ternary_numeral_system#Algorithms_for_converting_to_balanced_ternary

number = int(input())
tenary = []

exponent = 0
while number != 0:
    digit = (number % 3 ** (exponent + 1)) / 3 ** exponent
    if digit == 2:
        digit = -1
        caractere = "T"
    else:
        caractere = str(int(digit))
    tenary.insert(0, caractere)
    
    number -= digit * 3 ** exponent
    exponent += 1
    
if number == 3 ** exponent:
    tenary.append(str(1))

print("".join(tenary) or "0")