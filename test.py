import main
import unittest


class test_answer(unittest.TestCase):

    def test_plus_1(self) -> None:
        inf = main.info_class()
        inf.regex = "ab+"
        inf.x = "a"
        inf.k = 1
        self.assertEqual(main.calculate(inf), 1)

    def test_plus_2(self) -> None:
        inf = main.info_class()
        inf.regex = "ba+"
        inf.x = "b"
        inf.k = 1
        self.assertEqual(main.calculate(inf), 1)

    def test_multiply_1(self) -> None:
        inf = main.info_class()
        inf.regex = "ab."
        inf.x = "a"
        inf.k = 1
        self.assertEqual(main.calculate(inf), 2)

    def test_multiply_2(self) -> None:
        inf = main.info_class()
        inf.regex = "ab."
        inf.x = "a"
        inf.k = 2
        self.assertEqual(main.calculate(inf), main.inf)

    def test_multiply_3(self) -> None:
        inf = main.info_class()
        inf.regex = "ab."
        inf.x = "b"
        inf.k = 1
        self.assertEqual(main.calculate(inf), main.inf)

    def test_star_1(self) -> None:
        inf = main.info_class()
        inf.regex = "a*"
        inf.x = "a"
        inf.k = 1
        self.assertEqual(main.calculate(inf), 1)

    def test_star_2(self) -> None:
        inf = main.info_class()
        inf.regex = "a*"
        inf.x = "a"
        inf.k = 2
        self.assertEqual(main.calculate(inf), 2)

    def test_star_3(self) -> None:
        inf = main.info_class()
        inf.regex = "a*"
        inf.x = "b"
        inf.k = 1
        self.assertEqual(main.calculate(inf), main.inf)

    def test_average_1(self) -> None:
        inf = main.info_class()
        inf.regex = "acb..bab.c.*.ab.ba.+.+*a."
        inf.x = "b"
        inf.k = 2
        self.assertEqual(main.calculate(inf), 4)

    def test_average_2(self) -> None:
        inf = main.info_class()
        inf.regex = "ab+c.aba.*.bac.+.+*"
        inf.x = "с"
        inf.k = 4
        self.assertEqual(main.calculate(inf), main.inf)


class test_read(unittest.TestCase):
    def test_read(self) -> None:
        inf_1 = main.info_class()
        inf_1.read()  # wrtie "ab+\n a\n 1\n"
        inf_2 = main.info_class()
        inf_2.regex = "ab+"
        inf_2.x = "a"
        inf_2.k = 1
        self.assertEqual(inf_1.regex, inf_2.regex)
        self.assertEqual(inf_1.x, inf_2.x)
        self.assertEqual(inf_1.k, inf_2.k)

    def test_read_file(self) -> None:
        with open("test_read.txt", 'w') as file:
            file.write("ab+\n")
            file.write("a\n")
            file.write("1\n")
        inf_1 = main.info_class()
        inf_1.read_from_file("test_read.txt")
        inf_2 = main.info_class()
        inf_2.regex = "ab+"
        inf_2.x = "a"
        from os import system
        system("rm test_read.txt")


if __name__ == '__main__':
    unittest.main()
