def masodik(lines):
    counter = 0
    for i in range(len(lines)):
        if "." in lines[i]:
            counter += 1
    return counter

def harmadik(lines):
    counter_one = 0
    counter_all = 0
    for i in range(len(lines)):
        if lines[i].strip() == "1":
            counter_one += 1
            counter_all += 1
        if lines[i].strip() == "0":
            counter_all += 1
    return round((counter_one / counter_all) * 100, 2)

def negyedik(lines):
    counter = 0
    for i in range(len(lines)):
        if i % 5 == 3 and lines[i+1].strip() == "1":
            counter += int(lines[i])
    days = int(counter / 60 / 24)
    hours = int(((counter / 60 / 24) - days) * 24)
    minutes = round(((counter / 60 / 24) - days - (hours / 24)) * 24 * 60)
    return [days, hours, minutes]

def otodik(lines):
    from datetime import datetime
    #my_date_str = input("Adjon meg egy dátumot! Dátum= ")
    my_date_str = "2017.10.18"
    my_date = datetime.strptime(my_date_str, "%Y.%m.%d")
    for i in range(len(lines)):
        if i % 5 == 0 and lines[i].strip() != "NI" and lines[i+4].strip() == "0" and (my_date - datetime.strptime(lines[i].strip(), "%Y.%m.%d")).days >= 0:
            print(f"{lines[i+2]}\t{lines[i+1]}")

def hetnapja(ev, ho, nap):
    napok = ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev = ev -1
    return napok[(ev + (ev // 4) - (ev // 100) + (ev // 400) + honapok[ho - 1] + nap) % 7]

def hetedik(lines):
    #day = input("Adja meg a hét egy napját (például cs)! Nap= ")
    day = "cs"
    series = []
    for i in range(len(lines)):
        if (
            i % 5 == 0 and lines[i].strip() != "NI" and
            hetnapja(int(lines[i].strip().split(".")[0]), int(lines[i].strip().split(".")[1]), int(lines[i].strip().split(".")[2])) == day
        ):
            if lines[i+1] not in series:
                series.append(lines[i+1])
    if series == []:
        print("Az adott napon nem kerül adásba sorozat.")
    for i in series:
        print(i)

def nyolcadik(lines):
    data_dict = dict()
    for i in range(len(lines)):
        if i % 5 == 1 and lines[i] in data_dict.keys():
            data_dict[lines[i]]["time"] += int(lines[i+2])
            data_dict[lines[i]]["count"] += 1
        if i % 5 == 1 and lines[i] not in data_dict.keys():
            data_dict[lines[i]] = {"time": int(lines[i+2]), "count": 1}
        
    with open("summa.txt", "w") as sum_file:
        for key, value in data_dict.items():
            sum_file.write("{} {} {}\n".format(key, value["time"], value["count"]))

if __name__ == "__main__":
    with open("list.txt", "r") as txt_file:
        lines = txt_file.read().splitlines()
    
    print("2. feladat")
    print(f"A listában {masodik(lines)} db vetítési dátummal rendelkező epizód van.\n")
    print("3. feladat")
    print(f"A listában levő epizódok {harmadik(lines)}%-át látta.\n")
    print("4. feladat")
    print(f"Sorozatnézéssel {negyedik(lines)[0]} napot {negyedik(lines)[1]} órát {negyedik(lines)[2]} percet töltött.\n")
    print("5. feladat")
    otodik(lines)
    print()
    print("7. feladat")
    print(hetedik(lines))
    nyolcadik(lines)