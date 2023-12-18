def main(a,b,c):
    """
    Find number of negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    f=0
    if a<0:
        f+=1
    if b<0:
        f+=1
    if c<0:
        f+=1
        return f
print(main(3,-3,-6))