import pandas as pd
from pulp import *

C = 2
stationlen = 20

data = []
dataA = []
dataB = []
datalen = 0
carlen = 0

def readData():
    global data
    global datalen
    global dataA
    global dataB
    global carlen
    df = pd.read_excel(r'D:\Desktop\one.xls', sheet_name='实例1')
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

def assignment_problem():
    prob = LpProblem("Car Problem", LpMinimize)
    varC = LpVariable.dicts("C", (range(carlen),range(datalen)), lowBound=0)
    prob += lpSum([varC[i][j] * dataB[j][t] for i in range(carlen) for t in range(stationlen) for j in range(datalen)])

    for j in range(datalen):
        prob += (lpSum([varC[i][j] for i in range(carlen)]) == 1)
    for i in range(carlen):
        for t in range(stationlen):
            prob += (lpSum([varC[i][j] * dataA[j][t]for j in range(datalen)]) <= C)
            prob += (lpSum([varC[i][j] * dataA[j][t] for j in range(datalen)]) >= 0)

    prob.solve()
    # print("answer is",value(prob.objective))
    result_C = [[value(varC[i][j]) for j in range(datalen)] for i in range(carlen)]
    return {"result_C":result_C,"answer":value(prob.objective)}

if __name__ == "__main__":
    readData()
    ans = assignment_problem()
    print(ans["result_C"])
    print(len(ans["result_C"]),len(ans["result_C"][0]))
    print(dataB)
    print(len(dataB))
    print(ans["answer"])
    print(sum([ans["result_C"][i][j] * dataB[j][t] for i in range(carlen) for t in range(stationlen) for j in range(datalen)]))