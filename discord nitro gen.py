import random
import string

fic = open("number.txt", "w")

while True:
    code = "".join(random.choices(
    string.ascii_uppercase + string.digits + string.ascii_lowercase,
    k = 16
    ))
    fic.write(f"https://discord.gift/{code}\n")
    print(f"https://discord.gift/{code}\n")







