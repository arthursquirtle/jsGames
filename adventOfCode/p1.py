with open('adventOfCode/p1input.txt', 'r') as file:
#with open('adventOfCode/p1b.txt', 'r') as file:
    count = 0
    lList = []
    rList = []
    while True:
        line = file.readline()
        if not line:
            break
        #print(f"Line{count}: {line.strip()}")
        #print(f"Line{count}: {line.split()}")
        splitVal = line.split()
        lVal = int(splitVal[0])
        rVal = int(splitVal[1])
        #print (lVal, rVal, lVal < rVal)
        lList.append(lVal)
        rList.append(rVal)
    lList.sort()
    rList.sort()
    print (lList)
    print (rList)
    for i in range(0,len(lList)):
        timesFound = 0
        for j in range(0,len(rList)):
            if lList[i] == rList [j]:   
                timesFound +=1
        similarityScore = lList[i]*timesFound
        print(lList[i],timesFound,similarityScore)
        count += similarityScore

        #print(rList[i])
        #diff = lList[i]- rList[i]
        #print(abs(diff),'\n')
        #count += abs(diff)
        #print(lList[i],rList[i], abs(diff))
        print(count)
    #for val in a:
    #print(val)