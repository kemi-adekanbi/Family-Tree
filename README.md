# Family-Tree
This project has a family tree where you interact with a pre-set list of family member with kinship queries.

## How It's Made:
**Tech used:** Python

The information of each family memeber is stored in a dictionary. This includes their name, mother and father, spouse, date of birth and death. This added to a list where all the family members will be stored. That list is passed into the FamilyTree class, which has functions that are used to find the relationship between family members. 

**List of queries that can be made:**
1. View Parents
2. View Grandchildren
3. View Immediate Family
4. View Alive Extended Family
5. View Siblings
6. View Cousins
7. View Family Birthdays
8. View Birthday Calender
9. View Average Age Of Death
10. View Number Of Children Per Person
11. View Average Number Of Children

## How to use it
Run the `FamilyTreeMenu.py` file to start interacting with the family tree.

## Optimisations
Originally, I stored the family members using a class called Person and created attributes for their personal information. However, this complicated the process leading to features not working as they required Family Tree class methods as well. After some reflection, I realised storing the family member's infomation using a dictionary was a more optimal approach. Using the keys and values, I was able to store information about each indivdual in a clear and understandable manner. This made accessing information faster with less code.

## Lessons Learned
I learnt the importance of choosing the right data structure that fit the needs of my projects as well as how to applying object orientated programming principles to my code. For example, encapusulation by making the family tree list private so it can't be changed from outside the class and making my functions more reusable to other parts of my FamilyTree class.
