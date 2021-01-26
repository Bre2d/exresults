import colorsys


def main():

    global math_t
    print("9adeh jebt fel a3ded hedhom ? :")
    arm_c = float(input("Devoir de controle 3arabeya (ma9al): "))
    arm_s = float(input("Devoir de synthése 3arabeya (ma9al): "))
    arb_c = float(input("Devoir de controle 3arabeya (bale8a): "))
    arb_s = float((input("Devoir de synthése 3arabeya (bale8a): ")))
    ar_oral = float(input("9adeh jebt chifehi arabeya: "))
    arm_t = float((arm_c + (arm_s * 2)) / 3)
    arb_t = float((arb_c+(arb_s*2))/3)
    ar_t = float((arb_t+ar_oral+(arm_t*2))/4)
    print("===================================")
    print("\003[0;32;30m Mou3adel 3arabeya: {}".format(ar_t))
    print("===================================")
    math_c = float(input("Devoir de controle math: "))
    math_c2 = float(input("Devoir de controle n°2 math: "))
    math_s = float(input("Devoir de synthése math: "))
    if math_c2 == 0:
        math_t = float((math_c+math_c2+(math_s*2))/3)
    if math_c2 != 0:
        math_t = float((math_c+math_c2+(math_s*2))/4)
    print("===================================")
    print("Mou3adel el math: {}".format(math_t))
    print("===================================")
    fr_c = float(input("Devoir de controle français: "))
    fr_oral = float(input("Oral français: "))
    fr_s = float(input("Devoir de synthése français: "))
    fr_t = float((fr_c+fr_oral+(fr_s*2))/4)
    print("===================================")
    print("Mou3adlek fel français: {}".format(fr_t))
    print("===================================")






if __name__ == '__main__':
    main()
