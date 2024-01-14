# Ein leeres Dictionary erstellen
my_dict = {}

# Schlüssel-Wert-Paare hinzufügen
my_dict['name'] = 'John'
my_dict['age'] = 25
my_dict['city'] = 'New York'

# Das Dictionary ausgeben
print("Dictionary nach dem Hinzufügen von Schlüssel-Wert-Paaren:", my_dict)

# Wert anhand des Schlüssels abrufen
name_value = my_dict['name']
print("Wert des Schlüssels 'name':", name_value)

# Schlüssel-Wert-Paar entfernen
removed_pair = my_dict.pop('age')
print("Entferntes Schlüssel-Wert-Paar:", removed_pair)
print("Dictionary nach dem Entfernen eines Schlüssels:", my_dict)

# Über Schlüssel-Wert-Paare iterieren
print("Schlüssel-Wert-Paare im Dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Überprüfen, ob ein Schlüssel im Dictionary vorhanden ist
is_key_present = 'age' in my_dict
print("Ist 'age' im Dictionary vorhanden:", is_key_present)

# Liste der Schlüssel und Werte extrahieren
keys_list = list(my_dict.keys())
values_list = list(my_dict.values())
print("Liste der Schlüssel:", keys_list)
print("Liste der Werte:", values_list)

# Dictionary leeren
my_dict.clear()
print("Dictionary nach dem Leeren:", my_dict)