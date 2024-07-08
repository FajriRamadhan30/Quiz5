p = 11
q = 5
r = 4

hasil_2a = (p - r) == (r + q)
hasil_2b = ((p % 3) + q) != (r % 2)
hasil_2c = (q - 3) == (p % 2 + q)
hasil_2d = (r + q) != ((p * 2) % 2)
hasil_2e = ((q % 3) + p) > (r % 2)
hasil_2f = (r + p) <= (q * 5)

print(f"((p - r) == (r + q)): {hasil_2a}")
print(f"(((p % 3) + q) != (r % 2)): {hasil_2b}")
print(f"((q - 3) == (p % 2 + q)): {hasil_2c}")
print(f"((r + q) != ((p * 2) % 2)): {hasil_2d}")
print(f"(((q % 3) + p) > (r % 2)): {hasil_2e}")
print(f"((r + p) <= (q * 5)): {hasil_2f}")
