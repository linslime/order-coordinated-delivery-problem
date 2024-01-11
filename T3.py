list1 = [[1,2,3],[4,6,6]]
list2 = [[1,2,3,5],[3,5,3,7],[3,8,9,4]]
a = sum([(list1[i][j] * list2[j][t] )  for i in range(2) for j in range(3) for t in range(4) ])
print(a)