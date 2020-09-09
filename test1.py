class Bigtext:
    T1 = "*"*5
    T2 = " * * "
    T3 = "*    "
    T4 = "    *"
    T5 = "  *  "
    T6 = "*   *"
    # 0 = Y, 1 = O, 2 = U, 3 = L, 4 = S, 5 = E.
    CHAR = ((T6, T2, T5, T5, T5), (T1, T6, T6, T6, T1), (T6, T6, T6, T6, T1),
            (T3, T3, T3, T3, T1), (T1, T3, T1, T4, T1), (T1, T3, T1, T3, T1))

    def __init__(self, num):
        # 0 = Y, 1 = O, 2 = U, 3 = L, 4 = S, 5 = E.
        self.num = num

    def show_big(self):
        char = Bigtext.CHAR
        for i in char[self.num]:
            print(i)

    def show_text(self):
        text = ""
        bigY = Bigtext(0)
        bigO = Bigtext(1)
        bigU = Bigtext(2)
        bigL = Bigtext(3)
        bigS = Bigtext(4)
        bigE = Bigtext(5)
        for i in range(5):
            text += "{}\t{}\t{}\t\t{}\t{}\t{}\t{}\n".format(bigY.get_line(i), bigO.get_line(i), bigU.get_line(i),
                                                    bigL.get_line(i), bigO.get_line(i), bigS.get_line(i),
                                                    bigE.get_line(i))
        return text
    def get_line(self, line):
        char = Bigtext.CHAR
        return char[self.num][line]


if __name__ == '__main__':
    # test = Bigtext(0)
    # test.show_big()
    bigY = Bigtext(0)
    # bigO = Bigtext(1)
    # bigU = Bigtext(2)
    # bigL = Bigtext(3)
    # bigS = Bigtext(4)
    # bigE = Bigtext(5)
    # for i in range(5):
    #     print("{} {} {}     {} {} {} {}".format(bigY.get_line(i), bigO.get_line(i), bigU.get_line(i),
    #                                             bigL.get_line(i), bigO.get_line(i), bigS.get_line(i), bigE.get_line(i)))

    text = bigY.show_text()
    print(text)