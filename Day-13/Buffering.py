with open('buffering.txt','w') as f:
    [f.write(str(i)+'\n') for i in range(1_000_000)]