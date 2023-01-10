def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
    s(str): parameter
     """
    d=len(s)
    if d>=n:
       c= s[0:n]
    else:
       c= False

    return c
print(main("jbadhb",9))
