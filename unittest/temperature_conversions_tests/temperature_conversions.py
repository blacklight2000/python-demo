""" Validating the 'convert' function """


def convert(temperature, input_unit, output_unit, rounding=0):
    '''
       Converts temperature from F to C and C to F. Default rounding is 0
       Syntax: convert(temperature, input_unit, output_unit, rounding=0)
    '''
    if (input_unit == output_unit):
        return temperature
    if (input_unit == "F")and(output_unit == "C"):
        return round((temperature - 32) * 5/9.0, rounding)
    if (input_unit == "C")and(output_unit == "F"):
        return round((temperature * 9/5.0) + 32, rounding)

if __name__ == "__main__":
    assert(convert(100, "C", "F") == 212)
    assert(convert(212, "F", "C") == 100)
    assert(convert(100, "C", "C") == 100)
    assert(convert(212, "F", "F") == 212)
