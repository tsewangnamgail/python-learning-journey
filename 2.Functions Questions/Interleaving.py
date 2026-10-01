def interleave(a, b, result=""):
    if not a and not b:
        print(result, end=" ")
        return

    if a:
        interleave(a[1:], b, result + a[0])

    if b:
        interleave(a, b[1:], result + b[0])


a = input()
b = input()

interleave(a, b)