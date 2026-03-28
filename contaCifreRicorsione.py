def contatore(str, i, alpha, digit):
    # @param str: string
    # @param i: int set to 0
    # @param alpha: int set to 0
    # @param digit: int set to 0
    # @return: bool
    if i == len(str):
        return alpha == digit
    if str[i].isalpha():
        return contatore(str, i+1, alpha+1, digit)
    elif str[i].isdigit():
        return contatore(str, i+1, alpha, digit+1)


x = "ciao1245"
print(contatore(x, 0, 0, 0))