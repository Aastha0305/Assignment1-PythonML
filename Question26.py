def starts__endswith(string, prefix=None, suffix=None):
    if prefix is not None and string.startswith(prefix):
        return True, "starts with '{}'".format(prefix)
    elif suffix is not None and string.endswith(suffix):
        return True, "ends with '{}'".format(suffix)
    else:
        return False, "does not start with '{}' or end with '{}'".format(prefix, suffix)


string = input("Enter a string: ")
prefix = input("Enter a prefix : ")
suffix = input("Enter a suffix : ")

result, message = starts__endswith(string, prefix, suffix)
print("The string '{}' {}.".format(string, message))
