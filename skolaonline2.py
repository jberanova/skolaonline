class Student:
    def __init__(self, name):
        self.name = name
        self.classes = {}
        self.znamky = {}

    def trida(self, jmeno_tridy):
        self.classes[jmeno_tridy] = True
        print(f"{self.name} přidán do třídy {jmeno_tridy}.")

    def znamky_def(self, predmet, znamka):
        self.znamky.setdefault(predmet, []).append(znamka)
        print(f"{znamka} přidána za {predmet} u {self.name}.")

    def prumer_znamek_vypocet(self):
        return {predmet: sum(znamky) / len(znamky)}

class School:
    def __init__(self):
        self.students = {}

    def create_zak(self, name):
        student = Student(name)
        self.students[name] = student
        print(f"Jméno žáka: {name}.")
        return student

    def zak_trida(self, student, jmeno_tridy):
        student.trida(jmeno_tridy)

    def znamka_zakovi(self, student, predmet, znamka):
        student.znamky_def(predmet, znamka)

    def prumer_znamek(self, student):
        print(f"\nPrůměr známky: {student.name}:")
        for predmet, prumer in student.prumer_znamek_vypocet().items():
            print(f"{predmet}: {prumer}")

if __name__ == "__main__":
    skola = School()

    while True:
        print("\nMenu:")
        print("1. Jméno žáka")
        print("2. Přidat žáka do třídy")
        print("3. Přidat známku")
        print("4. Průměr známek")
        print("5. Ukončit školu online")
        choice = input("Zadejte (1/2/3/4): ")

        if choice == "1":
            zak_name = input("Jméno žáka: ")
            student = skola.create_zak(zak_name)
        elif choice == "2":
            jmeno_tridy = input("Třída: ")
            skola.zak_trida(student, jmeno_tridy)
        elif choice == "3":
            predmet = input("Předmět: ")
            znamka = float(input("Známka: "))
            skola.prumer_znamek(student, predmet, znamka)
        elif choice == "4":
            skola.prumer_znamek(student)
        elif choice == "5":
            break
        else:
            print("Špatná odpověď. Zkus to znovu.")