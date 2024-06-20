#Convertite Module is for convert all units
__author__ = 'Mohammad Parsa Mortazavi'
__version__ = 1.0
class temp:
    def convert(prenext,prenum):
        preunit,nextunit = prenext.split(' ')
        prenum = float(prenum)
        if preunit == 'c' and prenum>=(-273.15):
            if nextunit == 'k':
                return round(prenum + 273.15,2)
            if nextunit == 'f':
                return round(prenum * 1.8 + 32,2)
        elif preunit == 'k' and prenum>=0:
            if nextunit == 'c':
                return round(prenum - 273.15,2)
            if nextunit == 'f':
                if prenum == 0:
                    return -459.67
                return round(((prenum-273.15)*1.8)+32,2)
        elif preunit == 'f' and prenum>=-459.67:
            if nextunit == 'c':
                return round((prenum - 32)/1.8,2)
            if nextunit == 'k':
                return round(((prenum - 32)/1.8)+273.15,2)
        else:
            return 'Unit Not Found!'
class length:
    def convert(prenext,prenum):
        preunit,nextunit = prenext.split(' ')
        prenum = float(prenum)
        x = ''
        if preunit=="km":
            x = "km"
            a = 1000
        if preunit=="hm":
            x = "hm"
            a = 100
        if preunit=="dm":
            x = "dm"
            a = 10
        if preunit=="m":
            x = "m"
            a = 1
        if preunit=="ds":
            x = "ds"
            a = 0.1
        if preunit=="cm":
            x = "cm"
            a = 0.01
        if preunit=="mm":
            x = "mm"
            a = 0.001
        if nextunit=="km":
            y = "km"
            b = 1000
        if nextunit=="hm":
            y = "hm"
            b = 100
        if nextunit=="dm":
            y = "dm"
            b = 10
        if nextunit=="m":
            y = "m"
            b = 1
        if nextunit=="ds":
            y = "ds"
            b = 0.1
        if nextunit=="cm":
            y = "cm"
            b = 0.01
        if nextunit=="mm":
            y = "mm"
            b = 0.001
        xx = a/b
        prenum *= xx
        return prenum
class volume:
    def convert(prenext,prenum):
        preunit,nextunit = prenext.split(' ')
        prenum = float(prenum)
        x = ''
        if preunit=="km3":
            x = "km3"
            a = 1000000000
        if preunit=="hm3":
            x = "hm3"
            a = 1000000
        if preunit=="dm3":
            x = "dm3"
            a = 1000
        if preunit=="m3":
            x = "m3"
            a = 1
        if preunit=="ds3":
            x = "ds3"
            a = 0.001
        if preunit=="cm3":
            x = "cm3"
            a = 0.000001
        if preunit=="mm3":
            x = "mm3"
            a = 0.000000001
        if nextunit=="km3":
            y = "km3"
            b = 1000000000
        if nextunit=="hm3":
            y = "hm3"
            b = 1000000
        if nextunit=="dm3":
            y = "dm3"
            b = 1000
        if nextunit=="m3":
            y = "m3"
            b = 1
        if nextunit=="ds":
            y = "ds"
            b = 0.001
        if nextunit=="cm3":
            y = "cm3"
            b = 0.000001
        if nextunit=="mm3":
            y = "mm3"
            b = 0.000000001
        xx = a/b
        prenum *= xx
        return prenum
class area:
    def convert(prenext,prenum):
        preunit,nextunit = prenext.split(' ')
        prenum = float(prenum)
        x = ''
        if preunit=="km2":
            x = "km2"
            a = 1000000
        if preunit=="hm2":
            x = "hm2"
            a = 10000
        if preunit=="dm2":
            x = "dm2"
            a = 100
        if preunit=="m2":
            x = "m2"
            a = 1
        if preunit=="ds2":
            x = "ds2"
            a = 0.01
        if preunit=="cm2":
            x = "cm2"
            a = 0.0001
        if preunit=="mm2":
            x = "mm2"
            a = 0.000001
        if nextunit=="km2":
            y = "km2"
            b = 1000000
        if nextunit=="hm2":
            y = "hm2"
            b = 10000
        if nextunit=="dm2":
            y = "dm2"
            b = 100
        if nextunit=="m2":
            y = "m2"
            b = 1
        if nextunit=="ds":
            y = "ds"
            b = 0.01
        if nextunit=="cm2":
            y = "cm2"
            b = 0.0001
        if nextunit=="mm2":
            y = "mm2"
            b = 0.000001
        xx = a/b
        prenum *= xx
        return prenum
