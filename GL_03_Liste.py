# Eine leere Liste erstellen
my_list = []

# Elemente zur Liste hinzufügen
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Die Liste ausgeben
print("Liste nach dem Hinzufügen von Elementen:", my_list)

# Ein Element anhand des Index entfernen
removed_element = my_list.pop(1)
print("Entferntes Element:", removed_element)
print("Liste nach dem Entfernen eines Elements:", my_list)

# Ein Element am Ende hinzufügen
my_list.append(4)
print("Liste nach dem Hinzufügen eines weiteren Elements:", my_list)

# Ein Element an einer bestimmten Position einfügen
my_list.insert(1, 5)
print("Liste nach dem Einfügen eines Elements an einer bestimmten Position:", my_list)

# Ein Element anhand des Werts entfernen (nur das erste Vorkommen)
my_list.remove(2)
print("Liste nach dem Entfernen eines Elements anhand des Werts:", my_list)

# Index eines Elements finden
index_of_4 = my_list.index(4)
print("Index des Elements '4':", index_of_4)

# Liste sortieren
my_list.sort()
print("Sortierte Liste:", my_list)

# Liste in umgekehrter Reihenfolge sortieren
my_list.sort(reverse=True)
print("Umgekehrte sortierte Liste:", my_list)

# Eine kopierte und sortierte Liste erstellen, ohne die Originalliste zu ändern
sorted_list = sorted(my_list)
print("Originalliste:", my_list)
print("Neue sortierte Liste (ohne Änderung der Originalliste):", sorted_list)

# Die Länge der Liste abrufen
list_length = len(my_list)
print("Länge der Liste:", list_length)

# Über die Elemente der Liste iterieren
print("Elemente der Liste:")
for element in my_list:
    print(element)