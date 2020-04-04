def suma_kolokviumi(rezultati):
    for student in rezultati:
        student["Vkupno od kolokviumi"] = student["Kolokvium 1"] + student["Kolokvium 2"]
        del student["Kolokvium 1"]
        del student["Kolokvium 2"]

    return rezultati


if __name__ == "__main__":
    n = int(input())
    rezultati = []  # ova e listata od rechnici
    for i in range(0, n):
        r = {}  # rechnik koj kje chuva podatoci za eden student
        brojIndeks = input()
        brojPoeni1 = float(input())
        brojPoeni2 = float(input())
        r["indeks"] = brojIndeks
        r["Predmet"] = "Veshtachka inteligencija"
        r["Kolokvium 1"] = brojPoeni1
        r["Kolokvium 2"] = brojPoeni2
        rezultati.append(r)

    print(suma_kolokviumi(rezultati))

