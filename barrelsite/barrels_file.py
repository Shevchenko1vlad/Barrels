class Barrel:
    def __init__(self, idd):
        self.idd = idd


class BarrelsSet:
    def __init__(self, idd, barrels_l=[]):
        self.idd = idd
        self.barrels_l = [Barrel(i) for i in range(4, 0, -1)]

    def getBarrels(self):
        return [i.idd for i in self.barrels_l]

    def addSet(self, sett):
        self.barrels_l.append(sett)

    def removeSet(self, sett):
        self.barrels_l.remove(sett)


class Section:
    def __init__(self, idd, sets_l=[]):
        self.idd = idd
        self.sets_l = [BarrelsSet(i + 1) for i in range(1)]

    def getSets(self):
        return [i.idd for i in self.sets_l]

    def getId(self):
        return self.idd

    def addSet(self, sett):
        self.sets_l.append(sett)

    def removeSet(self, sett):
        self.sets_l.remove(sett)


class Factory:
    def __init__(self):
        self.sections = [[] for i in range(12)]
        self.generateSections()

    def getSection(self, ind):
        for i in self.sections:
            for j in i:
                if j.idd == ind:
                    return j

    def generateSections(self):
        tmp = [[0 for i in range(22)] for j in range(12)]
        for i in range(11, -1, -1):
            for j in range(22):
                tmp[11 - i][j] = (Section(12 * j + i + 1))
        ranges = [0, 6, 6, 9, 9, 12, 12, 15, 15, 19, 19, 22]
        for i in range(6):
            t_u = [tmp[j][ranges[2 * i]:ranges[(2 * i + 1)]] for j in range(0, 6)]
            t_l = [tmp[j][ranges[2 * i]:ranges[(2 * i + 1)]] for j in range(6, 12)]
            self.sections[i] = [t_u[i][j] for i in range(len(t_u)) for j in range(len(t_u[0]))]
            self.sections[6 + i] = [t_l[i][j] for i in range(len(t_l)) for j in range(len(t_l[0]))]

    def getEnumUpper(self):
        t = [6, 3, 3, 3, 4, 3, 6, 3, 3, 3, 4, 3]
        return [[[j.getId() for j in self.sections[i]], t[i]] for i in range(6)]

    def getEnumLower(self):
        t = [6, 3, 3, 3, 4, 3, 6, 3, 3, 3, 4, 3]
        return [[[j.getId() for j in self.sections[i]], t[i]] for i in range(6, 12)]


mainFactory = Factory()
