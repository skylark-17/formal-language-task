import main
import unittest


class test_answer(unittest.TestCase):

    def test_plus_1(self) -> None:
        main.info.getinstance().regex = "ab+"
        main.info.getinstance().prefix_symbol = "a"
        main.info.getinstance().prefix_len = 1
        self.assertEqual(main.calculate_min_len_word_with_prefix(), 1)

    def test_plus_2(self) -> None:
        main.info.getinstance().regex = "ba+"
        main.info.getinstance().prefix_symbol = "b"
        main.info.getinstance().prefix_len = 1
        self.assertEqual(main.calculate_min_len_word_with_prefix(), 1)

    def test_multiply_1(self) -> None:
        main.info.getinstance().regex = "ab."
        main.info.getinstance().prefix_symbol = "a"
        main.info.getinstance().prefix_len = 1
        self.assertEqual(main.calculate_min_len_word_with_prefix(), 2)

    def test_multiply_2(self) -> None:
        main.info.getinstance().regex = "ab."
        main.info.getinstance().prefix_symbol = "a"
        main.info.getinstance().prefix_len = 2
        self.assertEqual(main.calculate_min_len_word_with_prefix(), main.inf)

    def test_multiply_3(self) -> None:
        main.info.getinstance().regex = "ab."
        main.info.getinstance().prefix_symbol = "b"
        main.info.getinstance().prefix_len = 1
        self.assertEqual(main.calculate_min_len_word_with_prefix(), main.inf)

    def test_star_1(self) -> None:
        main.info.getinstance().regex = "a*"
        main.info.getinstance().prefix_symbol = "a"
        main.info.getinstance().prefix_len = 1
        self.assertEqual(main.calculate_min_len_word_with_prefix(), 1)

    def test_star_2(self) -> None:
        main.info.getinstance().regex = "a*"
        main.info.getinstance().prefix_symbol = "a"
        main.info.getinstance().prefix_len = 2
        self.assertEqual(main.calculate_min_len_word_with_prefix(), 2)

    def test_star_3(self) -> None:
        main.info.getinstance().regex = "a*"
        main.info.getinstance().prefix_symbol = "b"
        main.info.getinstance().prefix_len = 1
        self.assertEqual(main.calculate_min_len_word_with_prefix(), main.inf)

    def test_average_1(self) -> None:
        main.info.getinstance().regex = "acb..bab.c.*.ab.ba.+.+*a."
        main.info.getinstance().prefix_symbol = "b"
        main.info.getinstance().prefix_len = 2
        self.assertEqual(main.calculate_min_len_word_with_prefix(), 4)

    def test_average_2(self) -> None:
        main.info.getinstance().regex = "ab+c.aba.*.bac.+.+*"
        main.info.getinstance().prefix_symbol = "с"
        main.info.getinstance().prefix_len = 4
        self.assertEqual(main.calculate_min_len_word_with_prefix(), main.inf)


class test_read(unittest.TestCase):
    def test_read(self) -> None:
        main.info.getinstance().read()  # wrtie "ab+\n a\n 1\n"
        regex = "ab+"
        x = "a"
        k = 1
        self.assertEqual(main.info.getinstance().regex, regex)
        self.assertEqual(main.info.getinstance().prefix_symbol, x)
        self.assertEqual(main.info.getinstance().prefix_len, k)

    def test_read_file(self) -> None:
        with open("test_read.txt", 'w') as file:
            file.write("ab+\n")
            file.write("a\n")
            file.write("1")
        main.info.getinstance().read_from_file("test_read.txt")
        regex = "ab+\n"
        x = "a\n"
        k = 1
        self.assertEqual(main.info.getinstance().regex, regex)
        self.assertEqual(main.info.getinstance().prefix_symbol, x)
        self.assertEqual(main.info.getinstance().prefix_len, k)
        from os import system
        system("rm test_read.txt")


if __name__ == '__main__':
    unittest.main()
