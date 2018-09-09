def parens(n):
    results = []
    gen_parens(results, "", 0, 0, n)
    return results

def gen_parens(results, res_so_far, op, cl, maxnum):
    print("sofar=%s, op=%d, cl=%d" % (res_so_far, op, cl))
    if (len(res_so_far) == maxnum * 2):
        results.append(res_so_far)
    else:
        if (op < maxnum):
            gen_parens(results, res_so_far + "(", op+1, cl, maxnum)
        if (cl < op):
            gen_parens(results, res_so_far + ")", op, cl+1, maxnum)
            


print(parens(3))
