from datetime import datetime


def set_datetime():
    year = int(input("Geburtsjahr: "))
    month = int(input("Monat: "))
    day = int(input("Tag: "))

    return datetime(year, month, day)


# Ab hier testen:

time = set_datetime()

print("Ausgabe des Jahres: ", time.year)
print("Ausgabe des Monats: ", time.month)
print("Ausgabe des Tages: ", time.day)
print("Ausgabe der aktuellen Zeit: ", datetime.now())
