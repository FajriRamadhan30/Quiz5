hasil_1a = 15 % 5
print(f"15 mod 5 : {hasil_1a}")

hasil_1b = 12 +3*5==75
print(f"12 +3*5==75 : {hasil_1b}")

hasil_1c =  "PML" + "15523"
print(f'"PML" + "15523": {hasil_1c}')

try:
    hasil_1d = "100" + 234
except TypeError as e:
    hasil_1d = str(e)
hasil_1e = ((11 % 3) + 2) != 8 / 2

print(f'"100" + 234: {hasil_1d}')
print(f"((11 % 3) + 2) != 8 / 2 : {hasil_1e}")
