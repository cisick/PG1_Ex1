

# Beispiel einer Try-Except-Blockstruktur
try:
    # Hier kommt der Code, der möglicherweise eine Ausnahme verursacht
    num1 = int(input("Gib die erste Zahl ein: "))
    num2 = int(input("Gib die zweite Zahl ein: "))
    result = num1 / num2
    print("Ergebnis der Division:", result)

except ValueError as ve:
    # Hier wird Code ausgeführt, wenn eine ValueError-Ausnahme auftritt
    print(f"Fehler beim Konvertieren einer Zahl: {ve}")

except ZeroDivisionError:
    # Hier wird Code ausgeführt, wenn eine ZeroDivisionError-Ausnahme auftritt
    print("Division durch Null ist nicht erlaubt!")

else:
    # Dieser Block wird ausgeführt, wenn keine Ausnahme aufgetreten ist
    print("Keine Ausnahme aufgetreten!")

finally:
    # Dieser Block wird immer ausgeführt, unabhängig davon, ob eine Ausnahme aufgetreten ist oder nicht
    print("Das Finally-Statement wird immer ausgeführt.")

# Beispiel einer benutzerdefinierten Exception-Klasse
class CustomError(Exception):
    pass

try:
    # Hier kommt der Code, der möglicherweise eine benutzerdefinierte Ausnahme auslöst
    raise CustomError("Dies ist eine benutzerdefinierte Ausnahme!")

except CustomError as ce:
    # Hier wird Code ausgeführt, wenn die benutzerdefinierte Ausnahme auftritt
    print(f"Benutzerdefinierte Ausnahme gefangen: {ce}")