# Beispiel einer While-Schleife mit einer Zählvariable
count = 0
while count < 5:
    print(f"Aktuelle Zählung: {count}")
    count += 1

# Beispiel einer While-Schleife mit einer Bedingung
user_input = ''
while user_input.lower() != 'quit':
    user_input = input("Gib 'quit' ein, um die Schleife zu beenden: ")

# Beispiel einer While-Schleife mit break-Anweisung
number = 1
while True:
    print(f"Aktuelle Zahl: {number}")
    if number == 3:
        break
    number += 1

# Beispiel einer While-Schleife mit continue-Anweisung
number = 0
while number < 5:
    number += 1
    if number % 2 == 0:
        continue
    print(f"Aktuelle ungerade Zahl: {number}")

# Beispiel einer While-Schleife mit vorzeitigem Abbruch
total = 0
while True:
    num = int(input("Gib eine Zahl ein (0 zum Beenden): "))
    if num == 0:
        break
    total += num

print(f"Summe der eingegebenen Zahlen: {total}")