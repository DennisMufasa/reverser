import unittest

from reverse import reverser

numbers = [1,2,3,4,5]
letters = [
    "South Park",
    "Astronomy",
    "God of War 4",
    "Meditation",
    "God of War 4"
]
string = "dennis"
integer = 3000


class Test_reverse(unittest.TestCase):

    global string
    global integer
    global numbers
    global letters

    def test_output_type(self):
        output1 = reverser(numbers)
        output2 = reverser(letters)
        self.assertIsInstance(output1, list)
        self.assertIsInstance(output2, list)

    def test_output_reversal(self):
        output1 = reverser(numbers)
        output2 = reverser(letters)
        self.assertEqual(output1, [5,4,3,2,1])
        self.assertEqual(output2, ["God of War 4",
        "Meditation", "God of War 4", "Astronomy", "South Park"])

    def test_errorneous_arguments(self):
        output1 = reverser(string)
        output2 = reverser(integer)
        self.assertEqual(output1, "This method only accepts a single list!")
        self.assertEqual(output2, "This method only accepts a single list!")

if __name__ == '__main__':
    unittest.main()
