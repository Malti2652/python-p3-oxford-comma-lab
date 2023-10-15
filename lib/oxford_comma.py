# def oxford_comma(items):
#     return None
def oxford_comma(array):
    if len(array) == 1:
        return array[0]
    elif len(array) == 2:
        return " and ".join(array)
    else:
        last_element = array.pop()
        return ", ".join(array) + ", and " + last_element
