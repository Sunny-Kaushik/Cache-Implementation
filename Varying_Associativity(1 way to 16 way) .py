import math
ways=["1","2","4","8","16"] #here we are varrying the way of the cache
input_files=["gcc","gzip","swim","twolf","mcf"] # taking diferent input 
for t in input_files:
    for bi in ways:
        m=int(math.log(int(bi),2))        
        rows, cols = (2**(17-m), int(bi))
        arr = [[-1 for i in range(cols)] for j in range(rows)]                          # 2d array for maintaining track of rows and coloums.
        rows, cols = (2**(17-m), int(bi))
        queue = [[] for j in range(rows)]                                               #2d array for queue for maintaing the track of the least recently used way
        mis,hit=0,0
        file = open(f"/Users/karthikeyavadlamudi/Desktop/{t}.txt","r")                  #file input
        for line in file:
            i = int(line[4:12],16)
            b=str('{:032b}'.format(i))                                                  #convert the string from line to binary
            index,tag=int(b[(13+m):30],2),int(b[0:(13+m)],2)
            for j in range(0,int(bi)):
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
                elif(arr[index][j]!=tag and j==(int(bi)-1)): 
                    c=queue[index].pop(0)
                    arr[index][c]=tag
                    queue[index].append(c)                                              #if there is no tag match then we just update the queue and update the values in array.
                    mis=mis+1         
        print("\n")
        print(f"---------------Test file: {t}.trace-----------------------------\n")
        print("Number of ways :",bi)
        print(f"number of Hits = {hit} out of {mis+hit}")
        print("Mis rate =",(mis/(mis+hit)*100),"    ||        ","Hit rate =",((hit/(mis+hit))*100))              #print the HIT RATE and MISS RATE
        file.close()