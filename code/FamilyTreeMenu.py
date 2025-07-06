from FamilyTreeClass import FamilyDict

names= [person["Name"] for person in FamilyDict.get_family()]
family_names = " | ".join(names)

menu = """
Family Tree Menu

1. View Parents
2. View Grandchildren
3. View Immediate Family
4. View Alive Extended Family
5. View Siblings
6. View Cousins
"""

def fam_menu():

    print(menu)
    choice = int(input("Enter the number of your choice (1-7): "))
    while choice != 7:
        print (family_names)
        name = input("Enter their full name: ").title()
        while FamilyDict.is_in_family(name) is not True:
            name = input("The name could not be found in the Family Tree. Please try again: ").title()
            FamilyDict.is_in_family(name)

        if choice == 1:
            mother,father = FamilyDict.get_parents(name)
            print(f"\nMother: {mother} \nFather: {father}")
        elif choice == 2:
            grandchildren = FamilyDict.get_grandchildren(name)
            print(f"\nGrandchildren: {FamilyDict.format_checker(grandchildren)}")
        elif choice == 3:
            print(f"\n{FamilyDict.get_immediate(name)}")
        elif choice == 4:
            print(f"\n{FamilyDict.get_extended(name)}")
        elif choice == 5:
            siblings = FamilyDict.get_sibling(name)
            print(f"\nSiblings: {FamilyDict.format_checker(siblings)}")
        elif choice == 6:
            cousins = FamilyDict.get_cousins(name)
            print(f"\nCousins: {FamilyDict.format_checker(cousins)}")
        print(menu)
        choice = int(input("Enter the number of your choice (1-7): "))

fam_menu()



