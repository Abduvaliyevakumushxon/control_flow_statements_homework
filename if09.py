def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    x=(a%10)*10+a//10
    if a>=x:
        return True
    if a<x:
        return False
print(main(-9))