from typing import Final
PI: Final = 3.14
print ("pi: %f" % (PI))
jari_2036 = float(input('Masukkan nilai jari-jari: '))
luas_2036 = PI * jari_2036 * jari_2036
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2036, luas_2036))