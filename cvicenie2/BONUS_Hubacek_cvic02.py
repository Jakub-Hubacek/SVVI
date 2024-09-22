import time

dictionary = {"pes": "dog", "macka": "cat", "kon": "horse", "lev": "lion", "liska": "fox"}


def main():
    while True:
        print("\nMožnosti:")
        print("1. Zadajte slovenské slovo a zobraz preklad")
        print("2. Zobrazte počet kľúčových slov v slovníku")
        print("3. Pridajte nové slovo do slovníka")
        print("4. Ukončite program")

        choice = input("Zadajte číslo vašej voľby: ")

        if choice == "1":
            slovak_word = input("Zadajte slovenské slovo: ").lower()
            if slovak_word in dictionary:
                print(
                    f"Anglický preklad pre '{slovak_word}' je '{dictionary[slovak_word]}'."
                )
            else:
                print(f"Slovo '{slovak_word}' sa v slovníku nenachádza.")

        elif choice == "2":
            print(f"Počet kľúčových slov v slovníku: {len(dictionary)}")

        elif choice == "3":
            new_slovak_word = input("Zadajte nové slovenské slovo: ").lower()
            new_translation = input(
                f"Zadajte anglický preklad pre '{new_slovak_word}': "
            ).lower()
            dictionary[new_slovak_word] = new_translation
            print(
                f"Slovo '{new_slovak_word}' bolo pridané so slovenským prekladom '{new_translation}'."
            )

        elif choice == "4":
            print("Koniec programu.")
            break

        else:
            print("Neplatná voľba, skúste znova.")
        #time.sleep(2)

if __name__ == "__main__":
    main()
