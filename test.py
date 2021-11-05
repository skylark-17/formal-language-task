import source
import unittest


class TestAnswer(unittest.TestCase):

    def test_plus_1(self) -> None:
        source.InputData().getinstance().regex = "ab+"
        source.InputData().getinstance().prefix_symbol = "a"
        source.InputData().getinstance().prefix_len = 1
        self.assertEqual(source.calculate_min_len_word_with_prefix(), 1)

    def test_plus_2(self) -> None:
        source.InputData().getinstance().regex = "ba+"
        source.InputData().getinstance().prefix_symbol = "b"
        source.InputData().getinstance().prefix_len = 1
        self.assertEqual(source.calculate_min_len_word_with_prefix(), 1)

    def test_multiply_1(self) -> None:
        source.InputData().getinstance().regex = "ab."
        source.InputData().getinstance().prefix_symbol = "a"
        source.InputData().getinstance().prefix_len = 1
        self.assertEqual(source.calculate_min_len_word_with_prefix(), 2)

    def test_multiply_2(self) -> None:
        source.InputData().getinstance().regex = "ab."
        source.InputData().getinstance().prefix_symbol = "a"
        source.InputData().getinstance().prefix_len = 2
        self.assertEqual(source.calculate_min_len_word_with_prefix(), source.inf)

    def test_multiply_3(self) -> None:
        source.InputData().getinstance().regex = "ab."
        source.InputData().getinstance().prefix_symbol = "b"
        source.InputData().getinstance().prefix_len = 1
        self.assertEqual(source.calculate_min_len_word_with_prefix(), source.inf)

    def test_star_1(self) -> None:
        source.InputData().getinstance().regex = "a*"
        source.InputData().getinstance().prefix_symbol = "a"
        source.InputData().getinstance().prefix_len = 1
        self.assertEqual(source.calculate_min_len_word_with_prefix(), 1)

    def test_star_2(self) -> None:
        source.InputData().getinstance().regex = "a*"
        source.InputData().getinstance().prefix_symbol = "a"
        source.InputData().getinstance().prefix_len = 2
        self.assertEqual(source.calculate_min_len_word_with_prefix(), 2)

    def test_star_3(self) -> None:
        source.InputData().getinstance().regex = "a*"
        source.InputData().getinstance().prefix_symbol = "b"
        source.InputData().getinstance().prefix_len = 1
        self.assertEqual(source.calculate_min_len_word_with_prefix(), source.inf)

    def test_average_1(self) -> None:
        source.InputData().getinstance().regex = "acb..bab.c.*.ab.ba.+.+*a."
        source.InputData().getinstance().prefix_symbol = "b"
        source.InputData().getinstance().prefix_len = 2
        self.assertEqual(source.calculate_min_len_word_with_prefix(), 4)

    def test_average_2(self) -> None:
        source.InputData().getinstance().regex = "ab+c.aba.*.bac.+.+*"
        source.InputData().getinstance().prefix_symbol = "с"
        source.InputData().getinstance().prefix_len = 4
        self.assertEqual(source.calculate_min_len_word_with_prefix(), source.inf)


class TestRead(unittest.TestCase):
    def test_read(self) -> None:
        source.InputData().getinstance().read()  # wrtie "ab+\n a\n 1\n"
        regex = "ab+"
        x = "a"
        k = 1
        self.assertEqual(source.InputData().getinstance().regex, regex)
        self.assertEqual(source.InputData().getinstance().prefix_symbol, x)
        self.assertEqual(source.InputData().getinstance().prefix_len, k)

    def test_read_file(self) -> None:
        with open("test_read.txt", 'w') as file:
            file.write("ab+\n")
            file.write("a\n")
            file.write("1")
        source.InputData().getinstance().read_from_file("test_read.txt")
        regex = "ab+\n"
        x = "a\n"
        k = 1
        self.assertEqual(source.InputData().getinstance().regex, regex)
        self.assertEqual(source.InputData().getinstance().prefix_symbol, x)
        self.assertEqual(source.InputData().getinstance().prefix_len, k)
        from os import remove
        remove("test_read.txt")


if __name__ == '__main__':
    unittest.main()
