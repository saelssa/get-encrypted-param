from demo.api.api import XLadon, XGorgon, XArgus, XCylons


class Helper:

    @staticmethod
    def get_x_ladon():
        param1 = XLadon.decrypt("ltCyalMN4I88MKaornPKU+LSy5Tl6jDZcJFrMF3eokqTucfp")
        print(param1)

        param2 = XLadon.encrypt(1646098215, "1225625952")
        print(param2)

        param3 = XLadon.decrypt(param2)
        print(param3 == param1)

    @staticmethod
    def get_x_gorgon():
        ss1 = XGorgon.decrypt("8404008900006d2495919861ae80fbdfc51b0161d0ded28ac70e")
        print(ss1)

        ss2 = XGorgon.encrypt(ss1)
        print(ss2)

        ss3 = XGorgon.decrypt(ss2)
        print(ss3 == (ss1))

    @staticmethod
    def get_x_argus():
        s1 = "4up7lV8l0txOeHMhPfVbpaSgUyqtZXii7SBk1RBZAu/colH8tJC+YKadXwoOw/RlILHO/jUzmw/NChqR2jKqyXS3uo7UtzBgjZSqW00SVLPgzF+tboWR1MozjpihOD0HnFZqw+QC5/GCHshpf2BR5H60OnehuepkccU3DODOed14A717LBDuATpB5njQNf/ALzFFFXfN5x6Kats1ylD2m2dwdQEkgTBclIfAf+JAJd9jsKiPXCnhGR/Lv65SwTxCrHY="
        ss1 = XArgus.decrypt(s1)
        ss1.dump()

        ss2 = XArgus.encrypt(ss1)
        print(ss2)

        ss3 = XArgus.decrypt(ss2)
        ss3.dump()
        print(ss3 == ss1)

    @staticmethod
    def get_x_cylons():
        x_cylons = "vCzcLbH1humC6lstWfdp4Cfl"
        ss1 = XCylons.decrypt(x_cylons)
        print(ss1)
        l = ss1.split(',')
        ss2 = XCylons.encrypt(l[1].strip(' '), l[0].strip(' '), l[2].strip(' '))
        print(ss2)
        print(ss2 == x_cylons)

    @staticmethod
    def read_file(filename: str) -> bytes:
        with open(filename, 'rb') as f:
            return f.read()
        return None

if __name__ == '__main__':
    # replace the method to obtain the corresponding parameter
    # get_x_ladon get_x_gorgon get_x_argus get_x_cylons
    Helper.get_x_gorgon()
