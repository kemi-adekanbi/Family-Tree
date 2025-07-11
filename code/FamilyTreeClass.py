class FamilyTree:
    def __init__(self, lst):
        self.__family = lst

    def get_family(self):
        return self.__family # return a list of the family tree

    def get_family_member(self, name):
        for person in self.__family:
            if person["Name"] == name:
                return person #returns the details of person in the family tree

    def is_in_family(self, name):
        if self.get_family_member(name) is None: #checks if the name entered is not the family tree
            return False
        return True

    def get_parents(self,name):
        person = self.get_family_member(name)
        mother,father = person["Mother"], person["Father"]
        return [mother, father]   #returns the parents of the name inputted

    def get_children(self, name):
        children = []
        for person in self.__family:
            if person["Mother"] == name or person["Father"] == name: #checks if the person inputted is stored as anyone's parent
                children.append(person["Name"])

        return children  #returns a list of their children

    def get_grandchildren(self, name):
        grandchildren = []
        children = self.get_children(name) #finds the children of the name inputted
        if children != []:
            for x in children:
                grandkid = self.get_children(x) # checks if their child has their own kid
                if grandkid is not None:
                    for g in grandkid:
                        grandchildren.append(g) #if they do, it gets added to a list of grandchildren
        return grandchildren

    def get_spouse(self, name):
        person = self.get_family_member(name)
        return person["Spouse"] #returns their spouse/partner of the name entered

    def get_sibling(self, name):
        mother,father = self.get_parents(name)
        if mother == "Unknown" and father == "Unknown":
            return []
        siblings = self.get_children(mother) #gets the children of their parents
        if name in siblings: #removes the name inputted so it only has their siblings
            siblings.remove(name)
        return siblings
    @staticmethod
    def format_checker(lst):
        if lst == "Dead": #don't change anything if they dead
            return lst
        if lst == []: # no known family member
            return "Unknown"
        elif len(lst) == 1: #returns the only name in the list
            return lst[0]
        return ", ".join(lst)

    def get_immediate(self, name):
        #returns the immediate family of the name entered
        mother,father = self.get_parents(name)
        siblings = self.format_checker(self.get_sibling(name))
        spouse = self.get_spouse(name)
        children = self.format_checker(self.get_children(name))
        return f"Mother: {mother} \nFather: {father} \nSiblings: {siblings} \nSpouse: {spouse} \nChildren: {children}"

    def get_aunts_uncles(self, name):
        mother,father = self.get_parents(name)
        if mother == "Unknown" and father == "Unknown": #have no parents information
            return []
        m_sibling = self.get_sibling(mother) #finds the siblings of their parents
        f_sibling = self.get_sibling(father)
        if f_sibling == [] and mother != "Unknown": #if they have only one parent information
            return m_sibling
        elif m_sibling == [] and father != "Unknown":
            return f_sibling
        return m_sibling + f_sibling #if they have both parents information

    def get_cousins(self, name):
        cousins = []
        aunt_uncle = self.get_aunts_uncles(name) #finds the siblings of their parents
        if len(aunt_uncle) == 0:
            return aunt_uncle
        for person in aunt_uncle: #gets the kid of each aunt/uncles
            kid = self.get_children(person)
            if kid != []:
                cousins += kid
        return cousins


    def get_extended(self, name):
        def alive_checker(people):
            if people == "Unknown" or people == []:    #filtering out inputs without a family member
                return people
            if type(people) == str:
                person = self.get_family_member(people)
                if person["dod"] != "":    #it checks if the death date of the name entered is not empty
                    return "Dead"    #if it's not, then they are dead
            elif type(people) is list:
                for x in people:     #checks whether everyone in the list is alive
                    if self.get_family_member(x)["dod"] != "":    #any dead family is removed from the list
                        people.remove(x)
                if people == []:     #if list is empty, there are no alive family members
                    return "Dead"
            return people

        #returns the alive extended family members that are blood related
        mother,father = self.get_parents(name)
        alive_mother,alive_father = alive_checker(mother),alive_checker(father)
        alive_siblings = alive_checker(self.get_sibling(name))
        alive_spouse = alive_checker(self.get_spouse(name))
        alive_children = alive_checker(self.get_children(name))
        alive_aunts_uncles = alive_checker(self.get_aunts_uncles(name))
        alive_cousins = alive_checker(self.get_cousins(name))
        return (f"Mother: {alive_mother} \nFather: {alive_father} \nSiblings: {self.format_checker(alive_siblings)} "
                f"\nSpouse: {alive_spouse} \nChildren: {self.format_checker(alive_children)} \nAunts/Uncles: {self.format_checker(alive_aunts_uncles)} \nCousins: {self.format_checker(alive_cousins)}")

    def get_birthdays(self):
        birthdays = []
        for person in self.__family:
            birthdays.append(f'{person["Name"]} : {person["dob"]}') #adding the name and birthday of each person to the list
        return birthdays

    def get_birthday_calender(self):
        from datetime import datetime

        def bubble_sort(lst):
            for i in range(len(lst)-1,0,-1):#working backwards in the list
                swapped = False
                for k in range(i):
                    if lst[k]["month"] == lst[k + 1]["month"]: #checks if they were born on the same month
                        if lst[k]["day"] > lst[k + 1]["day"]: #if the current day is greater than the next day
                            lst[k], lst[k + 1] = lst[k + 1], lst[k] #swaps them
                            swapped = True
                if not swapped:
                    return lst
            return lst

        def calender_format(lst):
            month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                           "October", "November", "December"]
            calender = []
            for index, x in enumerate(lst):
                person2 = lst[index - 1]  # gets the dictionary at the previous index
                x["month"] = month_names[x["month"] - 1]  # changing the int version of the month to a string version of the month
                if x["month"] == person2["month"] and x["day"] == person2[
                    "day"]:  # checks to see if anyone has the same birthday
                    x["name"] = f"{person2['name']}, {x['name']}"  # combines their name together
                    lst.remove(person2)  # removes the dictionary as they've been combined with another
                    calender.remove(calender[-1])
                calender.append(f"{x['name']}: {x['day']} {x['month']}")  # storing the all the data in a string
            return calender

        birthdays = []
        for person in self.__family:
            date = datetime.strptime(person["dob"], '%d/%m/%Y')
            birthdays.append({"name": person["Name"], "month": date.month,
                              "day": date.day})  # storing the name and dob in dictionary for each person

        month_sorted = list(sorted(birthdays, key=lambda bday: bday['month']))  # sorts in ascending order using the month values

        sorted_birthdays = bubble_sort(month_sorted)

        return calender_format(sorted_birthdays)
    def get_average_death_age(self):
        all_age = []
        for x in self.__family:
            if x["dod"] != "": #checks if they are dead
                dob = x["dob"].split("/") #get the day,month and year numbers only
                dod = x["dod"].split("/")
                all_age.append(int(dod[2])-int(dob[2])) #to find the age they died, it subtracts the year they died from the year they were born on
        total_age = 0
        for x in all_age:
            total_age += x #adds up all the ages in the list
        return total_age/len(all_age) #divides the total but number of ages to get the average

    def get_children_per_person(self):
        people_children = []
        for x in self.__family:
            children = self.get_children(x["Name"]) # finds the children of each person in the family tree
            total = len(children) #gets the total number of children
            people_children.append([x['Name'], total])  #name of person and the total is added to a list
        return people_children

    def get_average_children(self):
        lst_children = self.get_children_per_person() # gets how many children each person has
        total = 0
        for x in lst_children:
            total += x[1] #adds up each number of children in the list
        return f"{total/len(lst_children) : .2f}" #returns the average to 2 significant figures









p1 = {"Name":"Elias", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Ruby", "dob":"04/03/1900", "dod":"02/02/1960"}
p2 = {"Name":"Ruby", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Elias", "dob":"08/02/1903", "dod":"02/02/1970"}


m1 = {"Name":"Mara", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Dan", "dob":"13/02/1920", "dod":"02/02/1990"}
m2 = {"Name":"Dan", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Mara", "dob":"12/03/1919", "dod":"02/02/1995"}
p6 = {"Name":"Donna", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Bailey", "dob":"23/12/1929", "dod":"02/02/2006"}
p5 = {"Name":"Bailey", "Mother":"Ruby", "Father":"Elias", "Spouse":"Donna", "dob":"07/05/1930", "dod":"02/02/2010"}
p4 = {"Name":"Lyndon", "Mother":"Ruby", "Father":"Elias", "Spouse":"Zara", "dob":"19/01/1932", "dod":"02/02/2009"}
p3 = {"Name":"Zara", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Lyndon", "dob":"15/04/1938", "dod":"02/02/2017"}

m3 = {"Name":"Marie", "Mother":"Mara", "Father":"Dan", "Spouse":"Nathan", "dob":"03/05/1955", "dod":""}
m4 = {"Name":"Nathan", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Marie", "dob":"09/07/1960", "dod":""}
p7 = {"Name":"Victoria", "Mother":"Zara", "Father":"Lyndon", "Spouse":"Unknown", "dob":"02/08/1970", "dod":""}
p8 = {"Name":"Lorenzo", "Mother":"Donna", "Father":"Bailey", "Spouse":"Christina", "dob":"10/07/1957", "dod":""}
p9 = {"Name":"Christina", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Lorenzo", "dob":"16/11/1960", "dod":""}
p10 = {"Name":"Amanda", "Mother":"Donna", "Father":"Bailey", "Spouse":"Unknown", "dob":"10/07/1957", "dod":""}


m5 = {"Name":"Arie", "Mother":"Marie", "Father":"Nathan", "Spouse":"Alex", "dob":"25/10/1980", "dod":""}
m6 = {"Name":"Alex", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Arie", "dob":"28/02/1980", "dod":""}
m7 = {"Name":"Brie", "Mother":"Marie", "Father":"Nathan", "Spouse":"Kat", "dob":"15/07/1985", "dod":""}
m8 = {"Name":"Kat", "Mother":"Christina", "Father":"Lorenzo", "Spouse":"Brie", "dob":"01/08/1984", "dod":""}
p11 = {"Name":"James", "Mother":"Christina", "Father":"Lorenzo", "Spouse":"Sienna", "dob":"10/11/1990", "dod":""}
p12 = {"Name":"Sienna", "Mother":"Unknown", "Father":"Unknown", "Spouse":"James", "dob":"16/04/1994", "dod":""}

m9 = {"Name":"Rie", "Mother":"Arie", "Father":"Alex", "Spouse":"Unknown", "dob":"26/06/2005", "dod":""}
m10 = {"Name":"Kie", "Mother":"Brie", "Father":"Kat", "Spouse":"Unknown", "dob":"21/11/2010", "dod":""}
p13 = {"Name":"Abby", "Mother":"James", "Father":"Sienna", "Spouse":"Unknown", "dob":"13/03/2025", "dod":""}

extra = {"Name":"Mia", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Unknown", "dob":"11/07/2008", "dod":""}
famDict = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,extra,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13]
#a list containing the maternal and paternal branch

FamilyDict = FamilyTree(famDict)
