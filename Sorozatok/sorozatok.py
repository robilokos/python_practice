def masodik(lines):
    pass

def harmadik(lines):
    pass

def negyedik(lines):
    pass


if __name__ == "__main__":
    with open("lista.txt", "r") as txt_file:
        lines = txt_file.read().splitlines()
    
    print("2. feladat")
    print(f"A listában {masodik(lines)} db vetítési dátummal rendelkező epizód van.\n")
    print("3. feladat")
    print(f"A listában levő epizódok {harmadik(lines)}%-át látta.\n")
    print("4. feladat")
    print(f"Sorozatnézéssel {negyedik(lines)[0]} napot {negyedik(lines)[1]} órát {negyedik(lines)[2]} percet töltött.\n")