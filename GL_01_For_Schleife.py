# Beispiel einer For-Schleife über eine Liste
my_list = [1, 2, 3, 4, 5]
print("For-Schleife über eine Liste:")
for element in my_list:
    print(element)

# Beispiel einer For-Schleife über einen Bereich von Zahlen
print("\nFor-Schleife über einen Bereich von Zahlen:")
for i in range(1, 6):  # von 1 bis 5 (nicht inklusive 6)
    print(i)

# Beispiel einer For-Schleife mit Index und Element
print("\nFor-Schleife mit Index und Element:")
for index, element in enumerate(my_list):
    print(f"Index: {index}, Element: {element}")

# Beispiel einer For-Schleife über ein Dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print("\nFor-Schleife über ein Dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Beispiel einer verschachtelten For-Schleife
print("\nVerschachtelte For-Schleife:")
for i in range(3):
    for j in range(2):
        print(f"Äußere Schleife: {i}, Innere Schleife: {j}")

# Beispiel einer For-Schleife mit vorzeitigem Abbruch
print("\nFor-Schleife mit vorzeitigem Abbruch:")
for number in my_list:
    if number == 3:
        break
    print(number)

# Beispiel einer For-Schleife mit Überspringen bestimmter Elemente
print("\nFor-Schleife mit Überspringen bestimmter Elemente:")
for number in my_list:
    if number % 2 == 0:
        continue
    print(number)