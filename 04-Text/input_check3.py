import re

while True:

    phone = input("Voer je nummerbord in : ")

    patroon = '^\w{2}-?\d{3}-?\w{3}$'

    matches = re.findall(patroon, phone)

    if(len(matches)>0):
        break

print("Bedankt, nummerbord in juiste formaat", matches[0])


