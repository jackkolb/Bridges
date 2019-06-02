def ToReducedRowEchelonForm(M):
    if not M:
        print("not M")
        return ["NOT M"]
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return M
        i = r
        while M[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return M
        M[i], M[r] = M[r], M[i]
        lv = M[r][lead]
        M[r] = [mrx / float(lv) for mrx in M[r]]
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = [iv - lv * rv for rv, iv in zip(M[r], M[i])]
        lead += 1

    return M
