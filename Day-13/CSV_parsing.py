import csv

# w=csv.writer(open('sample.csv','w',newline=''))
# w.writerow(['name','value'])
# w.writerow(['Potato',100])
# w.writerow(['Tomato',150])
# w.writerow(['Cabbage',50])
# w.writerow(['Onion',70])

for r in csv.DictReader(open('sample.csv')): print(r)