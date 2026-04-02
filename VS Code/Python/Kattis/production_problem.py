def simplex(A, C):
    m, n = len(A), len(A[0])-1; c = [[0]*(m+n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n): c[i][j] = A[i][j]
        c[i][-1] = A[i][-1]
    for i in range(n): c[-1][i] = C[i]
    for i in range(m): c[i][i+n] = 1
    while True:
        if (col:=min([(i,e) for i,e in enumerate(c[-1]) if e<0], key=lambda x: x[1], default=[-1])[0]) == -1: break
        if (row:=min([(i,e,c[i][-1]/c[i][col]) for i,e in enumerate(c[t][col] for t in range(m)) if e>0], key=lambda x: x[2], default=[-1])[0]) == -1: break
        k = c[row][col]
        for i in range(m+n+1): c[row][i] /= k
        for i in range(m+1):
            if i == row: continue
            k = c[i][col]
            for j in range(m+n+1): c[i][j] -= k*c[row][j]
    return c[-1][-1]
m, n = map(int, input().split()); A = [[0]*(n+1) for _ in range(m)]; C = []
for i, e in enumerate(map(int, input().split())): A[i][n] = e
for i in range(n):
    *v, p = map(float, input().split()); C.append(-p)
    for j in range(m): A[j][i] = v[j]/100
print('%.2f'%simplex(A, C))


#My attempt.
"""
no_materials, no_products  = map(int, input().split())
material_vols = list(map(int, input().split()))
prod_list = []
max_profits = []
for i in range(no_products):
    prod_list.append(list(map(float, input().split())))
for i in range(no_products):
    max_profits.append(0)
    max_prod = []
    updated_materials = []
    for j in range(no_materials):
        max_prod.append(material_vols[j]*100 / prod_list[i][j]) if not prod_list[i][j] == 0 else None
    produced = min(max_prod)
    max_profits[i] += produced*prod_list[i][no_materials]

    for j in range(no_materials):
        updated_materials.append(material_vols[j] - produced*prod_list[i][j]/100)
    secondaries = []
    for k in range(no_products):
        if k != i:
            secondaries.append(k)
    def efficiency(k):
        tot = sum(prod_list[k][j] for j in range(no_materials) if prod_list[k][j] > 0)
        return prod_list[k][no_materials] / tot if tot > 0 else 0
    
    secondaries.sort(key=efficiency, reverse=True)

    for k in secondaries:
        vol_calc = []
        for j in range(no_materials):
            vol_calc.append(updated_materials[j]*100 / prod_list[k][j]) if not prod_list[k][j] == 0 else None 
        if not vol_calc:
            continue
        produced = min(vol_calc)
        max_profits[i] += produced*prod_list[k][no_materials]
        for j in range(no_materials):
            updated_materials[j] -= produced*prod_list[k][j]/100
            updated_materials[j] = max(0, updated_materials[j])
print(f"{max(max_profits):.2f}")"""