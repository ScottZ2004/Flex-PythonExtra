import re

while True:

    phone = input("Voer je postcode in : ")

    patroon = '^\d{4} ?\w{2}$'

    matches = re.findall(patroon, phone)

    if(len(matches)>0):
        break

print("Bedankt, postcode in juiste formaat", matches[0])


