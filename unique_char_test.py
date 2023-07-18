from unique_char import find_unique_ch

import unittest

test_data = [["e",
              "C makes it easy for you to shoot yourself in the foot. C++ makes that harder, but when you do, it blows away your whole leg. (с) Bjarne Stroustrup R# R++"],
             ["m", "The Tao gave birth to machine language.  Machine language gave birth\n" +
              "to the assembler.\n" +
              "The assembler gave birth to the compiler.  Now there are ten thousand\n" +
              "languages.\n" +
              "Each language has its purpose, however humble.  Each language\n" +
              "expresses the Yin and Yang of software.  Each language has its place within\n" +
              "the Tao.\n" +
              "But do not program in COBOL if you can avoid it.\n" +
              "        -- Geoffrey James, \"The Tao of Programming\""],
             ["", ""],
             ["1", "1"],
             ["W", "QQQ EWE TTT"],
             ["", "QWQ EWE TWT"],
             ["H", "Hello World"],
             ["r", "bbookkeepper"],
             ["T", "Testing"]]


class Testing(unittest.TestCase):
    def test_unique_char(self):
        for case in test_data:
            self.assertEqual(case[0], find_unique_ch(case[1]))


if __name__ == '__main__':
    unittest.main()
