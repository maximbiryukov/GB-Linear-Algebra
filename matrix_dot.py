# Метод для перемножения матриц

def dot_product(a, b):
    a_numrows = len(a)
    b_numrows = len(b)
    a_numcols = len(a[0])
    b_numcols = len(b[0])
    print(f'a({a_numrows}x{a_numcols}), b({b_numrows}x{b_numcols})')
    if a_numcols != b_numrows:
        print('Number of columns in A should be equal to number of rows in B')
        return False
    result = [[0]*b_numcols for i in range(a_numrows)]
    for i in range(a_numrows):
        for j in range(b_numcols):
            for k in range(a_numcols):
                result[i][j] += a[i][k] * b[k][j]
    return result
