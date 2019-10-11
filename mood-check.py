mood = str(input("How do you feel?"))

if mood == "happy":
    print("It is great to see you happy!")
elif mood == "nervous" or "excited" or "sad":
    print("Take a deep breath 3 times.")
else:
    print("Cheer up, mate!")