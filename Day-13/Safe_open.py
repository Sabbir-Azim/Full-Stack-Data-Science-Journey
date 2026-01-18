try:
    with open('sample.txt','w') as f:
        f.write('Sample Line\n')
        raise ValueError
except ValueError:
    print('Handled')