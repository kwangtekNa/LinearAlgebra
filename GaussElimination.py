def zero_mat(n, p):
    z = []
    for i in range(n):
        row = []
        for j in range(p):
            row.append(0)
        z.append(row)
    return z

def deepcopy(A):
    if type(A[0]) == list:
        n = len(A)
        p = len(A[0])
        res = zero_mat(n, p)
        for i in range(n):
            for j in range(p):
                res[i][j] = A[i][j]
    else:
        n = len(A)
        res = []
        for i in range(n):
            res.append(A[i])

    return res

def solver(A, b):
    X = deepcopy(A)
    sol = deepcopy(b)
    n = len(X)

    for i in range(n):
        x_row = X[i]
        y_row = sol[i]

        if x_row[i] != 0:
            x_temp = 1/x_row[i]
        else:
            x_temp = 0

        x_row = [x_temp * el for el in x_row]
        y_row = x_temp * y_row

        X[i] = x_row
        sol[i] = y_row

        for j in range(n):
            if i == j:
                continue
            x_next = X[j]
            y_next = sol[j]
            x_temp = [el*(-x_next[i]) for el in x_row]
            y_temp = y_row*(-x_next[i])

            for k in range(n):
                x_next[k] = x_temp[k]+x_next[k]
            y_next = y_temp + y_next

            X[j] = x_next
            sol[j] = y_next

    return sol

if __name__ =='__main__':
    X = [[3,1,2],[2,6,-1],[4,0,-1]]
    y = [5,1,3]
    sol = solver(X,y)
    print(sol)