def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[None] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[m][n]
l=[]

def test(X):
    list = []
    LCS = []
    revsort = []
    i = 0
    count = 0
    indices = []
    import csv
    from copy import deepcopy

    with open('Daa.csv', 'rt')as f:
        data = csv.reader(f)
        for row in data:
            #print(row[0])
            list.append(row[0])
            #print("Length of LCS is ", lcs(X, row[0]))
            i = lcs(X, row[0])
            LCS.append(i)
    #print(list)
    #print("\nThe LCS of each word is:\n")
    #print(LCS)
    revsort = deepcopy(LCS)
    revsort.sort(reverse=True)
    #print("\nThe LCS of each word in Descending order is:\n")
    #print(revsort)
    i = 0
    f=[]
    #print("\nWord will be Corrected to:")
    while i < 1:
        indices = [j for j, x in enumerate(LCS) if x == revsort[i]]
        if len(indices) != 1:
            for k in indices:
                #print(list[k])
                f.append(list[k])
                count += 1
                if count == 5:
                    break
            i += len(indices) - 1
        else:
            #print(list[LCS.index(revsort[i])])
            f.append(list[LCS.index(revsort[i])])
            count += 1
        i += 1
        l.append(f[0])

a = "appl"
a=input("Enter the word")
for i in a.split():
    #print(i)
    test(i)

print("Word will be corrected to :")
print(*l)
s =input("Is the word correct?(y/n)")
if  s== "y":
    pass
else:
    f = open("DAA.csv","a+")
    f.write(a+"\n")