def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    z=""
    if temp<0:
        z="Freezing"
    if temp>=1 and temp <=10:
        z="Very Cold"
    if temp>=11 and temp <=20:
        z="Cold"
    if temp>=21 and temp<=30:
        z="Normal"
    if temp>=31 and temp<=40:
        z="Hot"
    if temp>40:
        z="Very Hot"
    return z
print(main(21))