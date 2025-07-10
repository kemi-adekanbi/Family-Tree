from FamilyTreeClass import FamilyDict

def feature_menu():
    menu = """
    Family Tree Menu

    1. View Parents
    2. View Grandchildren
    3. View Immediate Family
    4. View Alive Extended Family
    5. View Siblings
    6. View Cousins
    7. View Family Birthdays
    8. View Birthday Calender
    9. Exit
    """
    print(menu)
    choice = int(input("Enter the number of your choice (1-9): "))
    return choice

def format_columns(lst):
    for first, second, third, fourth in zip(lst[::4], lst[1::4], lst[2::4], lst[3::4]):
        print(f"{first: >25} {second: >25} {third: >25} {fourth: >25}")

def names():
    name = [person["Name"] for person in FamilyDict.get_family()]
    format_columns(name)
    print()

def name_checker():
    name = input("Enter their full name: ").title()
    while FamilyDict.is_in_family(name) is not True:
        name = input("The name could not be found in the Family Tree. Please try again: ").title()
        FamilyDict.is_in_family(name)
    return name

def fam_menu():
    choice = feature_menu()
    while choice != 9:
        if choice == 1:
            names()
            name = name_checker()
            mother,father = FamilyDict.get_parents(name)
            print(f"\nMother: {mother} \nFather: {father}")
        elif choice == 2:
            names()
            name = name_checker()
            grandchildren = FamilyDict.get_grandchildren(name)
            print(f"\nGrandchildren: {FamilyDict.format_checker(grandchildren)}")
        elif choice == 3:
            names()
            name = name_checker()
            print(f"\n{FamilyDict.get_immediate(name)}")
        elif choice == 4:
            names()
            name = name_checker()
            print(f"\n{FamilyDict.get_extended(name)}")
        elif choice == 5:
            names()
            name = name_checker()
            siblings = FamilyDict.get_sibling(name)
            print(f"\nSiblings: {FamilyDict.format_checker(siblings)}")
        elif choice == 6:
            names()
            name = name_checker()
            cousins = FamilyDict.get_cousins(name)
            print(f"\nCousins: {FamilyDict.format_checker(cousins)}")
        elif choice == 7:
            format_columns(FamilyDict.get_birthdays())
        elif choice == 8:
            calender = FamilyDict.get_birthday_calender()
            print("\n".join(calender))
        choice = feature_menu()

fam_menu()