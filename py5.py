def cube_maker():
    rows = int(input('Rows: '))
    columns  = int(input('Colums: '))
    charaters = input('Charater: ')
    for x in range(0,rows):
        for y in range(0,columns):
            print(charaters,end='')
            
        print()
    
cube_maker()