import unittest
from FamilyTreeClass import FamilyDict

class TestGetParents(unittest.TestCase):
    def test_has_parents(self):
        self.assertEqual(FamilyDict.get_parents("Marie"), ["Mara","Dan"])
    def test_no_parents(self):
        self.assertEqual(FamilyDict.get_parents("Mia"), ["Unknown","Unknown"])

class TestGetSpouse(unittest.TestCase):
    def test_with_spouse(self):
        self.assertEqual(FamilyDict.get_spouse("Marie"), "Nathan")
    def test_no_spouse(self):
        self.assertEqual(FamilyDict.get_spouse("Mia"), "Unknown")

class TestGetChildren(unittest.TestCase):
    def test_with_kids(self):
        self.assertEqual(FamilyDict.get_children("Marie"), ["Arie","Brie"])
    def test_without_kids(self):
        self.assertEqual(FamilyDict.get_children("Mia"), [])

class TestGetGrandchildren(unittest.TestCase):
    def test_has_grandchildren(self):
        self.assertEqual(FamilyDict.get_grandchildren("Marie"), ["Rie","Kie"])
    def test_has_children_no_grandchildren(self):
        self.assertEqual(FamilyDict.get_grandchildren("Arie"), [])
    def test_no_grandchildren(self):
        self.assertEqual(FamilyDict.get_grandchildren("Mia"), [])

class TestGetSiblings(unittest.TestCase):
    def test_has_siblings(self):
        self.assertEqual(FamilyDict.get_sibling("Arie"), ["Brie"])
    def test_no_siblings(self):
        self.assertEqual(FamilyDict.get_sibling("Mia"), [])

class TestGetImmediateFamily(unittest.TestCase):
    def test_has_all_family(self):
        self.assertEqual(FamilyDict.get_immediate("Arie"), "Mother: Marie \nFather: Nathan \nSiblings: Brie \nSpouse: Alex \nChildren: Rie")
    def test_has_no_siblings(self):
        self.assertEqual(FamilyDict.get_immediate("Marie"), "Mother: Mara \nFather: Dan \nSiblings: Unknown \nSpouse: Nathan \nChildren: Arie, Brie")
    def test_no_family(self):
        self.assertEqual(FamilyDict.get_immediate("Mia"), "Mother: Unknown \nFather: Unknown \nSiblings: Unknown \nSpouse: Unknown \nChildren: Unknown")

class TestGetAuntUncle(unittest.TestCase):
    def test_has_aunt_uncle(self):
        self.assertEqual(FamilyDict.get_aunts_uncles("Rie"), ["Brie"])
    def test_has_none(self):
        self.assertEqual(FamilyDict.get_aunts_uncles("Arie"), [])

class TestGetCousins(unittest.TestCase):
    def test_has_cousins(self):
        self.assertEqual(FamilyDict.get_cousins("Rie"), ["Kie"])
    def test_no_cousins(self):
        self.assertEqual(FamilyDict.get_sibling("Mia"), [])

class TestGetExtendedFamily(unittest.TestCase):
    def test_has_all_extended_family(self):
        self.assertEqual(FamilyDict.get_extended("Arie"), "Mother: Marie \nFather: Nathan \nSiblings: Brie \nSpouse: Alex \nChildren: Rie \nAunts/Uncles: Unknown \nCousins: Unknown" )

if __name__ == '__main__':
    unittest.main()


#print(FamilyDict.get_fam())
#print(FamilyDict.get_sibling("Mia"))
#print(FamilyDict.get_immediate("Marie"))
# print(FamilyDict.get_extended("Arie"))
# print()
# print(FamilyDict.get_extended("Rie"))
# print()
#print(FamilyDict.get_extended("Marie"))