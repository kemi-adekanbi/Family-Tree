import unittest
from FamilyTreeClass import FamilyDict

class TestGetParents(unittest.TestCase):
    def test_has_parents(self):
        self.assertEqual(FamilyDict.get_parents("Lorenzo"), ["Donna", "Bailey"])
        self.assertEqual(FamilyDict.get_parents("Bailey"), ["Ruby", "Elias"])
        self.assertEqual(FamilyDict.get_parents("Lyndon"), ["Ruby", "Elias"])
        self.assertEqual(FamilyDict.get_parents("James"), ["Christina", "Lorenzo"])
        self.assertEqual(FamilyDict.get_parents("Kat"), ["Christina","Lorenzo"])
        self.assertEqual(FamilyDict.get_parents("Abby"), ["James", "Sienna"])

    def test_no_parents(self):
        self.assertEqual(FamilyDict.get_parents("Elias"), ["Unknown","Unknown"])

class TestGetSpouse(unittest.TestCase):
    def test_with_spouse(self):
        self.assertEqual(FamilyDict.get_spouse("Kat"), "Brie")
    def test_no_spouse(self):
        self.assertEqual(FamilyDict.get_spouse("Kie"), "Unknown")

class TestGetChildren(unittest.TestCase):
    def test_with_kids(self):
        self.assertEqual(FamilyDict.get_children("Kat"), ["Kie"])
        self.assertEqual(FamilyDict.get_children("Bailey"), ["Lorenzo","Amanda"])
    def test_without_kids(self):
        self.assertEqual(FamilyDict.get_children("Mia"), [])

class TestGetGrandchildren(unittest.TestCase):
    def test_has_grandchildren(self):
        self.assertEqual(FamilyDict.get_grandchildren("Lorenzo"), ["Kie","Abby"])
        self.assertEqual(FamilyDict.get_grandchildren("Elias"), ["Victoria","Lorenzo","Amanda"])
        self.assertEqual(FamilyDict.get_grandchildren("Bailey"), ["Kat", "James"])
    def test_has_children_no_grandchildren(self):
        self.assertEqual(FamilyDict.get_grandchildren("James"), [])
        self.assertEqual(FamilyDict.get_grandchildren("Sienna"), [])
    def test_no_grandchildren(self):
        self.assertEqual(FamilyDict.get_grandchildren("Victoria"), [])
        self.assertEqual(FamilyDict.get_grandchildren("Amanda"), [])

class TestGetSiblings(unittest.TestCase):
    def test_has_siblings(self):
        self.assertEqual(FamilyDict.get_sibling("Bailey"), ["Lyndon"])
        self.assertEqual(FamilyDict.get_sibling("James"), ["Kat"])
        self.assertEqual(FamilyDict.get_sibling("Amanda"), ["Lorenzo"])
    def test_no_siblings(self):
        self.assertEqual(FamilyDict.get_sibling("Victoria"), [])
        self.assertEqual(FamilyDict.get_sibling("Abby"), [])


class TestGetImmediateFamily(unittest.TestCase):
    def test_has_all_family(self):
        self.assertEqual(FamilyDict.get_immediate("Bailey"), "Mother: Ruby \nFather: Elias \nSiblings: Lyndon \nSpouse: Donna \nChildren: Lorenzo, Amanda")
    def test_has_no_siblings(self):
        self.assertEqual(FamilyDict.get_immediate("Victoria"), "Mother: Zara \nFather: Lyndon \nSiblings: Unknown \nSpouse: Unknown \nChildren: Unknown")
    def test_no_family(self):
        self.assertEqual(FamilyDict.get_immediate("Elias"), "Mother: Unknown \nFather: Unknown \nSiblings: Unknown \nSpouse: Ruby \nChildren: Lyndon, Bailey")

class TestGetAuntUncle(unittest.TestCase):
    def test_has_aunt_uncle(self):
        self.assertEqual(FamilyDict.get_aunts_uncles("Lorenzo"), ["Lyndon"])
        self.assertEqual(FamilyDict.get_aunts_uncles("Abby"), ["Kat"])
        self.assertEqual(FamilyDict.get_aunts_uncles("Kie"), ["Arie","James"])
    def test_has_none(self):
        self.assertEqual(FamilyDict.get_aunts_uncles("Donna"), [])

class TestGetCousins(unittest.TestCase):
    def test_has_cousins(self):
        self.assertEqual(FamilyDict.get_cousins("Lorenzo"), ["Victoria"])
        self.assertEqual(FamilyDict.get_cousins("Kie"), ["Rie","Abby"])
    def test_no_cousins(self):
        self.assertEqual(FamilyDict.get_cousins("James"), [])

class TestGetExtendedFamily(unittest.TestCase):
    def test_has_some_extended_family(self):
        self.assertEqual(FamilyDict.get_extended("Lorenzo"), "Mother: Dead \nFather: Dead \nSiblings: Amanda \nSpouse: Christina \nChildren: Kat, James \nAunts/Uncles: Dead \nCousins: Victoria")
        self.assertEqual(FamilyDict.get_extended("James"), "Mother: Christina \nFather: Lorenzo \nSiblings: Kat \nSpouse: Sienna \nChildren: Abby \nAunts/Uncles: Amanda \nCousins: Unknown")



if __name__ == '__main__':
    unittest.main()


