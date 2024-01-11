import pandas as pd

stationlen = 160

data = []
datastart = []
dataend = []
datalen = 0

def readData():
    global data
    global datalen
    global datastart
    global dataend
    df = pd.read_excel(r'D:\Desktop\one.xls', sheet_name='实例4')
    for i in df.values:
        data.append(i.tolist())
    datalen = len(data)
    datastart = [[] for i in range(stationlen)]
    dataend = [[] for i in range(stationlen)]
    for i in range(datalen):
        datastart[data[i][0]].append(i)
        dataend[data[i][1]].append(i)

def sovle():
    global datastart
    global dataend
    num = 0
    for i in range(stationlen):
        startlen = len(datastart[i])
        endlen = len(dataend[i])
        if startlen <= endlen:
            num += startlen
        else:
            num += endlen
    return 2 * datalen - num

if __name__ == "__main__":
    readData()
    print(sovle())

