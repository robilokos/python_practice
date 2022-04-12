print("Változók létrehozása és adat típusok gyakorlása")

# Szöveg típus: str
# Szám típusok: int, float, complex
# Szekvencia típusok: list, tuple, range
# Mapping típus: dict
# Halmaz típusok: set, frozenset
# Bool típus: bool
# Bináris típusok: bytes, bytearray, memoryview
# Típus lekérdezése: type(var)

print("Név változó létrehozása.\n")
name="Gaál Dávid"
print(name)


print("Életkor változó létrehozása.\n")
age=25
print(age)


print(f"Név: {name}, Életkor: {age}\n")



print("Változók típusának lekérdezése.\n")
print(type(age))
print(type(name))


print("Több változó létrehozása egyszerre.\n")

manufacturer,manufacturer2,manufacturer3="Faurecia","Purem","Katcon"
print(manufacturer)
print(manufacturer2)
print(manufacturer3)


print("Több egyforma értékű változó létrehozása egyszerre.\n")
Tibor=Gabor=Kalman=25
print(Tibor)
print(Kalman)
print(Gabor)

tools=["cp","FMEA","EK","SNAPP","PDCAFTA"]
print(tools)

human={
    "name":"Gaál Dávid",
    "age":25,
    "race":"white",
    "footsize":41
}
print(human)
#breakpoint()
"""
numbers={4,67,82,36,67,55,12,4}
print(numbers)
tools2=["cp","cp","FMEA","EK","SNAPP","PDCAFTA"]
print(set(tools2))
"""
print("done")