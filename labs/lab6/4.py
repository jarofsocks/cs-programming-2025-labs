def matrix_master(x, merge = False, mt1 = '', mt2 = ''):
    matrix = []
    for i in range(x):
        while 1:
            if merge:
                matrix_input = [int(mt1[i][mt_element]) + int(mt2[i][mt_element]) for mt_element in range(x)]
                matrix.extend([matrix_input])  
            else:
                matrix_input = input().split(' ')
                matrix.extend([matrix_input])
            if len(matrix_input) > x:
                print('Error!')
                continue
            break
    return matrix

while 1:
    ino = int(input())
    if ino < 2:
        print('Error!')
        continue
    break

matrix_1 = matrix_master(ino)
matrix_2 = matrix_master(ino)
matrix_3 = matrix_master(ino, merge = True, mt1 = matrix_1, mt2 = matrix_2)

print()
for i in matrix_3:    
    print(*i)


    