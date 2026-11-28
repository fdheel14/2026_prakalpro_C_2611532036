# Name: Fadhel Putra Nandes
# NIM: 2611532036


# Question 3A

text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])


# Question 3B

text = "Fadhel Putra Nandes"
count = 0
for char in text.lower():
    if char in "aiueo":
        count += 1
print("Vowels:", count)