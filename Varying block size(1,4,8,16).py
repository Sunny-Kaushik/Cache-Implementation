import math
byte_size=["1","4","8","16"]
input_files=["gcc","gzip","swim","twolf","mcf"]
for t in input_files:
    for bi in byte_size:
        m=int(math.log(int(bi),2))
        rows, cols = (2**(17-m), 4)
        arr = [[-1 for i in range(cols)] for j in range(rows)]                          # 2d array for maintaining track of rows and coloums.
        rows, cols = (2**(17-m), 4)
        queue = [[] for j in range(rows)]                                               #2d array for queue for maintaing the track of the least recently used way
        mis,hit=0,0
        file = open(f"/Users/karthikeyavadlamudi/Desktop/{t}.txt","r")                  #file input
        for line in file:
            i = int(line[4:12],16)
            b=str('{:032b}'.format(i))                                                  #convert the string from line to binary
            index,tag=int(b[15:(32-m)],2),int(b[0:15],2)
            for j in range(0,4):
                if((arr[index][j])==-1):
                    arr[index][j]=tag
                    queue[index].append(j)                                              #updating the the line with values in ways if they are empty and updateing the queue
                    mis=mis+1
                    break
                if((arr[index][j])!=-1 and arr[index][j]==tag):
                    queue[index].pop(queue[index].index(j))
                    queue[index].append(j)
                    hit=hit+1                                                           #if there is a tag match then update the queue and increase the hit                                                               
                    break
                elif(arr[index][j]!=tag and j==3): 
                    c=queue[index].pop(0)
                    arr[index][c]=tag
                    queue[index].append(c)                                              #if there is no tag match then we just update the queue and update the values in array.
                    mis=mis+1         
        print("\n")
        print(f"---------------Test file: {t}.trace-----------------------------\n")
        print("Byte size :",bi)
        print(f"number of Hits = {hit} out of {mis+hit}")
        print("Mis rate =",(mis/(mis+hit)*100),"    ||        ","Hit rate =",((hit/(mis+hit))*100))              #print the HIT RATE and MISS RATE
        file.close()