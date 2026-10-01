import ast

def depth(d):
    if not isinstance(d, dict):
        return 0

    if not d:
        return 1

    return 1 + max(depth(v) for v in d.values())


d = ast.literal_eval(input())

print(depth(d))