filepath = "students0.txt"

mail = ""
imie = ""
nazwisko = ""
punkty = 0
ocena = 0
status = ""
students = {}

def assignGrade(points):
    if (points <= 50):
        return 2
    elif (points <= 60):
        return 3
    elif (points <= 70):
        return 3.5
    elif (points <= 80):
        return 4
    elif (points <= 90):
        return 4.5
    else:
        return 5


def writeToFile(dictionary, path):
    with open(path, "w") as file_object:
        counter = 0
        for key in dictionary.keys():
            file_object.write(key + ",")
            file_object.write(str(dictionary.get(key)[0]) + ",")
            counter += 1
            file_object.write(str(dictionary.get(key)[1]) + ",")
            counter += 1
            file_object.write(str(dictionary.get(key)[2]) + ",")
            file_object.write(str(assignGrade(int(dictionary.get(key)[2]))) + "\n")
            counter += 1


with open(filepath) as file_object:
    for line in file_object:
        infoList = []
        values = line.split(',')
        mail = values[0]
        imie = values[1]
        nazwisko = values[2]
        punkty = int(values[3])

        infoList.append(imie)
        infoList.append(nazwisko)
        infoList.append(punkty)

        if len(values) == 5:  # zakładam że ocena to przedostatnia wartosc w linii
            ocena = values[4]
            infoList.append(ocena)
        else:
            ocena = assignGrade(punkty)
            infoList.append(ocena)

        if len(values) == 6:  # zakładam że ostatnia wartość w linii
            status = values[5]
            infoList.append(imie)

        students.update({mail: infoList})
        print(students)
        print(students)

print("=-=-=MENU=-=-=")
while True:
    option = input("1. Dodaj studenta \n 2. Usun studenta \n 3. Wypisz liste studentow \n 4. Zakoncz program")

    if int(option) == 1:
        newStudentString = input("Podaj dane w formacie (mail,imie,nazwisko,punkty)")
        newStudentSplitted = newStudentString.split(',')
        newInfoList = []

        if newStudentSplitted[0] in students.keys():
            print("Podany email jest już zajęty")
        else:
            newInfoList.append(newStudentSplitted[1])
            newInfoList.append(newStudentSplitted[2])
            newInfoList.append(newStudentSplitted[3])
            newInfoList.append(assignGrade(int(newStudentSplitted[3])))
            students.update({newStudentSplitted[0]: newInfoList})
            writeToFile(students, filepath)

    elif int(option) == 2:
        mailToDelete = input("Podaj mail studenta do usuniecia")

        if mailToDelete not in students.keys():
            print("Brak maila w bazie")
        else:
            students.pop(mailToDelete)
            writeToFile(students, filepath)
    elif int(option) == 3:
        print(students)
    elif int(option) == 4:
        break



