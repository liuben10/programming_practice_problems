def ingest_from_start(expr, start_i):
    number = ""
    i = start_i
    while i < len(expr) and expr[i].isdigit():
        number += expr[i]
        i += 1
    return number, i

def ingest_from_end(expr, end_i):
    number = ""
    i = end_i
    while i >= 0 and expr[i].isdigit():
        number += expr[i]
        i -= 1
    return number, i

def eval(op, n1, n2):
    if (op == "+"):
        return int(n1) + int(n2)
    elif (op == "-"):
        return int(n1) - int(n2)
    else:
        return int(n1) * int(n2)

def different_ways_to_compute(expr):
    return list(different_parens_outputs_helper(expr).values())

def different_parens_outputs_helper(expr):
    if (expr.isnumeric()):
        return {expr: int(expr)}
    snum, sidx = ingest_from_start(expr, 0)
    result = {}
    if (sidx < len(expr)):
        op = expr[sidx]
        solutions = different_parens_outputs_helper(expr[sidx+1:])
        for res in solutions:
            rest_expr_str = "(" + res + ")" if not res.isnumeric() else res
            result[snum + op + rest_expr_str] = eval(op, snum, solutions[res])

    enum, eidx = ingest_from_end(expr, len(expr)-1)
    if (eidx >= 0):
        op = expr[eidx]
        solutions = different_parens_outputs_helper(expr[:eidx])
        for res in solutions:
            rest_expr_str = "(" + res + ")" if not res.isnumeric() else res
            result[rest_expr_str + op + enum] = eval(op, solutions[res], enum)
    return result

def is_op(c):
    return c in ["+", "-", "*"]

def different_parens_outputs(expr):
    if (expr.isnumeric()):
        return [int(expr)]
    result = []
    for i in range(len(expr)):
        c = expr[i]
        if (is_op(c)):
            left = different_parens_outputs(expr[:i])
            right = different_parens_outputs(expr[i+1:])
            for l in left:
                for r in right:
                    evaluated = eval(c, l, r)
                    result.append(evaluated)

    return result
        
        
print(different_parens_outputs("2-1-1"))
