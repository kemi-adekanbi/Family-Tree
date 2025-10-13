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
In my original plan for this project, I had class called Person that had private attributes to store each person's information. While I had no trouble on finding their parents as it was stored within the object, finding relationships that were not explicitly stated was difficult e.g. grandchildren. With this in mind, I switched to using a dictionary for faster and easier retrival of information. The information was stored using key-value pairs and weren't individually private. This significantly boosted my progress.

## Lessons Learned
I learnt the importance of choosing the right data structure that fit the needs of my projects as well as how to applying object orientated programming principles to my code. For example, encapusulation by making the family tree list private so it can't be changed from outside the class.
