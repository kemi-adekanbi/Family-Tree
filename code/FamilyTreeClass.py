class FamilyTree:
    def __init__(self, lst):
        self.family = lst

    def is_in_family(self, name):
        #checks if someone in the family tree
        if name not in self.family:
            return False
        return True

    def get_family_member(self, name):
        #returns the details of person in the family tree
        for person in self.family:
            if person["Name"] == name:
                return person

    def get_parents(self,name):
        #returns of the person inputted
        person = self.get_family_member(name)
        mother,father = person["Mother"], person["Father"]
        return [mother, father]

    def get_children(self, name):
        #checks if the person inputted is stored as anyone's parent
        children = []
        for person in self.family:
            if person["Mother"] == name or person["Father"] == name:
                children.append(person["Name"])
        #returns a list of their children
        return children

    def get_grandchildren(self, name):
        grandchildren = []
        #finds the children of the name inputted
        children = self.get_children(name)
        if children != []:
            for x in children:
                grandkid = self.get_children(x)
                # checks if their child has their own kid
                if grandkid is not None:
                    for g in grandkid:
                        #if they do it gets added to a list of grandchildren
                        grandchildren.append(g)
        return grandchildren

    def get_spouse(self, name):
        #returns their spouse/partner
        person = self.get_family_member(name)
        return person["Spouse"]

    def get_sibling(self, name):
        #gets the children of their parents
        mother,father = self.get_parents(name)
        if mother == "Unknown" and father == "Unknown":
            return []
        siblings = self.get_children(mother)
        #removes the name inputted so it only has their siblings
        if name in siblings:
            siblings.remove(name)
        return siblings

    def format_checker(self, lst):
        if lst == "Dead":
            return lst
        if lst == []:
            return "Unknown"
        elif len(lst) == 1:
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
        #finds the siblings of their parents
        mother,father = self.get_parents(name)
        # have no parents information
        if mother == "Unknown" and father == "Unknown":
            return []
        m_sibling = self.get_sibling(mother)
        f_sibling = self.get_sibling(father)
        # have only one parent information
        if f_sibling == [] and mother != "Unknown":
            return m_sibling
        elif m_sibling == [] and father != "Unknown":
            return f_sibling
        # have both parents information
        return m_sibling + f_sibling

    def get_cousins(self, name):
        cousins = []
        #finds the siblings of their parents
        aunt_uncle = self.get_aunts_uncles(name)
        if len(aunt_uncle) == 0:
            return aunt_uncle
        #gets the kid of each aunt/uncles
        for person in aunt_uncle:
            kid = self.get_children(person)
            if kid != []:
                cousins += kid
        return cousins


    def get_extended(self, name):
        #returns a list of alive (blood related) extended family members
        def alive_checker(people):
            #filters out these inputs
            if people == "Unknown" or people == []:
                return people
            if type(people) == str:
                person = self.get_family_member(people)
                #it checks if the death date of the name entered is empty
                if person["dof"] != "":
                    #the name is replaced with dead if they are dead
                    return "Dead"
            elif type(people) is list:
                #checks whether everyone in the list is alive
                for x in people:
                    #they get removed if they aren't
                    if self.get_family_member(x)["dof"] != "":
                        people.remove(x)
                #if list is empty, there are no alive family members
                if people == []:
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





p1 = {"Name":"Elias", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Ruby", "dob":"01/02/2000", "dof":"02/02/2025"}
p2 = {"Name":"Ruby", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Elias", "dob":"01/02/2000", "dof":"02/02/2025"}


m1 = {"Name":"Mara", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Dan", "dob":"01/02/2000", "dof":"02/02/2025"}
m2 = {"Name":"Dan", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Mara", "dob":"01/02/1999", "dof":"02/02/2025"}
p6 = {"Name":"Donna", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Bailey", "dob":"01/02/1999", "dof":"02/02/2025"}
p5 = {"Name":"Bailey", "Mother":"Ruby", "Father":"Elias", "Spouse":"Donna", "dob":"01/02/1999", "dof":"02/02/2025"}
p4 = {"Name":"Lyndon", "Mother":"Ruby", "Father":"Elias", "Spouse":"Zara", "dob":"01/02/1999", "dof":"02/02/2025"}
p3 = {"Name":"Zara", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Lyndon", "dob":"01/02/1999", "dof":"02/02/2025"}

m3 = {"Name":"Marie", "Mother":"Mara", "Father":"Dan", "Spouse":"Nathan", "dob":"19/05/2006", "dof":""}
m4 = {"Name":"Nathan", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Marie", "dob":"15/01/2005", "dof":""}
p7 = {"Name":"Victoria", "Mother":"Zara", "Father":"Lyndon", "Spouse":"Unknown", "dob":"01/02/1999", "dof":""}
p8 = {"Name":"Lorenzo", "Mother":"Donna", "Father":"Bailey", "Spouse":"Christina", "dob":"10/07/2007", "dof":""}
p9 = {"Name":"Christina", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Lorenzo", "dob":"10/07/2007", "dof":""}
p10 = {"Name":"Amanda", "Mother":"Donna", "Father":"Bailey", "Spouse":"Unknown", "dob":"10/07/2007", "dof":""}


m5 = {"Name":"Arie", "Mother":"Marie", "Father":"Nathan", "Spouse":"Alex", "dob":"10/06/2007", "dof":""}
m6 = {"Name":"Alex", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Arie", "dob":"01/02/2005", "dof":""}
m7 = {"Name":"Brie", "Mother":"Marie", "Father":"Nathan", "Spouse":"Kat", "dob":"10/07/2007", "dof":""}
m8 = {"Name":"Kat", "Mother":"Christina", "Father":"Lorenzo", "Spouse":"Brie", "dob":"01/02/2000", "dof":""}
p11 = {"Name":"James", "Mother":"Christina", "Father":"Lorenzo", "Spouse":"Sienna", "dob":"10/07/2007", "dof":""}
p12 = {"Name":"Sienna", "Mother":"Unknown", "Father":"Unknown", "Spouse":"James", "dob":"10/07/2007", "dof":""}

m9 = {"Name":"Rie", "Mother":"Arie", "Father":"Alex", "Spouse":"Unknown", "dob":"11/07/2008", "dof":""}
m10 = {"Name":"Kie", "Mother":"Brie", "Father":"Kat", "Spouse":"Unknown", "dob":"10/07/2007", "dof":""}
p13 = {"Name":"Abby", "Mother":"James", "Father":"Sienna", "Spouse":"Unknown", "dob":"13/03/2006", "dof":""}

extra = {"Name":"Mia", "Mother":"Unknown", "Father":"Unknown", "Spouse":"Unknown", "dob":"11/07/2008", "dof":""}
famDict = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,extra,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13]
#a list containing the maternal and paternal branch

FamilyDict = FamilyTree(famDict)

#outside the class, check whether the name is in the family tree prior to searching
