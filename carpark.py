import pandas as pd
import random
import copy
import math
import csv

C = 2
stationlen = 60
n = 1

a = 0.99
T = 1
targetmin = 0

data = []
dataA = []
dataB = []
datastart = []
dataend = []
dataC = []
dataX = []
datalen = 0
carlen = 0

tempdataA=[]

def readData():
    global data
    global datalen
    global dataA
    global dataB
    global dataC
    global datastart
    global dataend
    global carlen

    df = pd.read_excel(r'D:\Desktop\one.xls', sheet_name='实例3')
    for i in df.values:
        data.append(i.tolist())
    datalen = len(data)

    dataB = [[0 for col in range(stationlen)] for row in range(datalen)]
    for i in range(datalen):
        dataB[i][data[i][0]] = 1
        dataB[i][data[i][1]] = 1

    dataA = [[0 for col in range(stationlen)] for row in range(datalen)]
    for i in range(datalen):
        j = data[i][0]
        while j < data[i][1] :
            dataA[i][j] = 1
            j += 1


    carlen = round(datalen / C)

    datastart = [[] for i in range(stationlen)]
    dataend = [[] for i in range(stationlen)]
    for i in range(datalen):
        datastart[data[i][0]].append(i)
        dataend[data[i][1]].append(i)

    dataC = [[0 for j in range(datalen)] for i in range(carlen)]

def greedy_algorithm():
    result = []
    tempdatastart = copy.deepcopy(datastart)
    for i in range(carlen):
        # c = 0
        list1 = []
        list2 = []
        key = 0
        for t in range(stationlen):

            if key == 1 and len(list1) == 0:
                break

            for j in list1:
                if dataB[j][t] == 1:
                    list1.remove(j)

            while len(list1) < C:
                le = len(tempdatastart[t])
                if le != 0:
                    r = random.randint(0, len(tempdatastart[t]) - 1)
                    list1.append(tempdatastart[t][r])
                    list2.append(tempdatastart[t][r])
                    tempdatastart[t].pop(r)
                    key = 1
                else:
                    break

        result.append(list2)
    return result

def write(x):
    from xlutils.copy import copy
    import xlrd as xr

    file = "D:\\Desktop\\MatrixX.xls"
    oldwb = xr.open_workbook(file)
    newwb = copy(oldwb)
    newws = newwb.get_sheet(-1 + n)
    for i in range(carlen):
        for t in range(stationlen):
            newws.write(i + 1, t + 1, x[i][t])  # 行，列，数据
    newwb.save(file)

def getMatrixC(list):
    result = [[0 for j in range(datalen)] for i in range(carlen)]
    for i in range(carlen):
        for j in list[i]:
            result[i][j] = 1
    return result

def getMatriX(list):
    result = [[0 for t in range(stationlen) ] for i in range(carlen)]
    for i in range(carlen):
        for t in range(stationlen):
            s = sum([list[i][j] * dataB[j][t] for j in range(datalen)])
            # print(s)
            if s != 0:
                result[i][t] = 1
    return result

def ifMatriY(list):
    key = 1
    for i in range(carlen):
        for t in range(stationlen):
            s = sum([list[i][j] * dataA[j][t] for j in range(datalen)])
            if s > C:
                key = 0
                break
        if key == 0:
            break
    return key

def sumMatriX(list):
    num = 0
    for i in list:
        num += sum(i)
        # print(sum(i))
    return num

def acceptrule(df):
    if df <= 0:
        return 1
    else:
        r = random.randint(0,1000000000000)/1000000000000
        if r < math.exp(-1*df/T):
            return 1
        else :
            return 0

def writescv(x):
    with open("D:\Desktop\MatrixC.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(dataC)
    with open("D:\Desktop\MatrixX.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(x)


if __name__ == "__main__":
    # writescv()
    readData()

    list = greedy_algorithm()
    dataC = getMatrixC(list)
    x = getMatriX(dataC)
    targetmin = sumMatriX(x)
    # write(x)
    if ifMatriY(dataC) == 1:
        writescv(x)
    print(targetmin)
    while T > math.pow(10,-30):
        templist = greedy_algorithm()
        tempdataC = getMatrixC(templist)
        tempx = getMatriX(tempdataC)
        temptargetmin = sumMatriX(tempx)
        if acceptrule(temptargetmin - targetmin) == 1:
            list = copy.deepcopy(templist)
            dataC = copy.deepcopy(tempdataC)
            x = tempx
            targetmin = temptargetmin
            # write(x)
            if ifMatriY(dataC) == 1:
                writescv(x)
            print(targetmin)
        T = a * T
