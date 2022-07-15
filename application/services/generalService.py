def strip_upper(string: str) -> str:
    '''
        returns the inputted string without spaces and uppercased
    '''
    return string.replace(" ", "").upper()

print(strip_upper('saih  aan'))