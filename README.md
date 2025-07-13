# Family-Tree
The user to select an individual within the family tree and choose what information they require from a list of 12 features. This is displayed in a user-friendly format.

# How It's Made
Tech Used: Python

All individuals have their information stored in using a dictionary and added to list where everyone is stored. This is entered into the Family Tree class and made private so information cannot be changed from outside the family tree.

The user can choose any of these features from the menu.
1. Parents
2. Grandchildren
3. Immediate family
4. Alive extended family memeber
5. Siblings
6. Cousins
7. Birthdays of everyone in the family tree
8. Birthdays in a sorted by month 
9. Average age of death
10. How many children per person
11. Average age number of children in the family tree

# Optimisations
Originally, I stored the family members using a class called Person and created attributes for their perosnal information. However this complicated the process leading to features not working as they reuqired Family Tree class methods as well. After some reflection, I realised storing the family member's infomation using a dictionary was a more optimal approach. Using the keys and values, I was able to store information about each indivdual in a clear and understandable manner. This made accessing information faster with less code.

# Lessons Learned:
Over the course of completing this project, I was able to apply Object Oriented Programming to my code by my functions more reusable to other parts of my Family Tree class and encapsulating the Family Tree list to be private.
