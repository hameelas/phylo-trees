print("Hello")

INF = float('Inf')

def main(fname):
    d = get_distances(fname)
    n = len(d)

    for k in range(n-2):
        m = n - k
        q, dict_q = calc_q(m, d)
        i, j = dict_q[min(dict_q.keys())]
        branchDist1, branchDist2 = calc_blen(m, i, j, d)
        join(m, d, i, j)
        print(k)
        print(i, j)
        import pprint
        pprint.pprint(q)
        pprint.pprint(d)
    
def join(m, d, i, j):   
    d += [[]]
    n = len(d)
    for k in range(n):
        if(k == n-1):
            d[n-1] += [0]
            continue
        d[n-1] += [0.5*(d[i][k] + d[j][k] - d[i][j])]
        d[k] += [d[n-1][k]]

    for k in range(n):
        m = n - k
        d[i][k] = INF
        d[j][k] = INF
        d[k][i] = INF
        d[k][j] = INF
    

def calc_blen(m, i, j, d):
    n = len(d)
    rows = sum_rows(d)
    branchDist1 =  0.5 * d[i][j]+(1/(2*(m-2)))*(rows[i]-rows[j])
    
    branchDist2 =  0.5 * d[i][j]+(1/(2*(m-2)))*(rows[j]-rows[i])

    return branchDist1, branchDist2

def sum_rows(d):
    n = len(d)
    rows = [0]*n
    for i in range(len(d)):
        for j in range(len(d)):
            if(d[i][j] != INF):
                rows[i] += d[i][j]
    return rows

def calc_q(m, d):
    q = []
    n = len(d)
    q_dict = {}

    rows = sum_rows(d)
    # print('rows:')
    # print(rows)

    for i in range(n):
        q += [[]]

        for j in range(n):
            if (i == j):
                q[-1] += [0]
                continue
            val = (m-2) * (d[i][j]) - rows[i] - rows[j]
            q[-1] += [val]
            
            q_dict[val] = (i,j)
    
    return q, q_dict

def get_distances(fname):
    with open(fname) as f:
        lines = f.readlines()

        d = [[int(x) for x in line.strip().split()] for line in lines]

    return d

if __name__ == '__main__':
    fname = 'data.txt'

    main(fname)
