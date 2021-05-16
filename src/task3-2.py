import unittest

from collections import Counter


def find_repeated_element(data: list):

    if len(data) == len(set(data)):
        return "No repeating elements"

    d = Counter()

    for element in data:
        d[element] += 1
        if d[element] >= 2:
            return element


class TestFind_repeated_element(unittest.TestCase):

    datasets = [
        (["a", "b", "c", "c", "a"], "c"),

        (["A", "a", "A", "c", "a"], "A"),

        (["a", "aa", "aaa", "aaaaaa", "aaaaaa"], "aaaaaa"),

        ([
            "a", "b", "c", "d", "e", "f", "g",
            "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"
        ], "No repeating elements"),

        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1], 1)
    ]

    def test_find_repeated_elements(self) -> None:

        for i in range(len(self.datasets)):

            self.assertEqual(
                find_repeated_element(
                    self.datasets[i][0]
                ),
                self.datasets[i][1],
                'Somthing goes wrong'
            )

            print(f"Test {i}: Success. ")


if __name__ == "__main__":
    unittest.main()
