from sympy import *
x = Symbol("x")

def substitution_function(input_function, variable_name, value):
    """ A function that takes a function and the variable name with the required value
     and returns the result of substitution"""
    return input_function.subs(variable_name, value).evalf()

def get_derivative(input_function, differentiation_element, number_of_derivatives=1):
    """ A function that takes a function and the differentiation element and
    returns the derivative function """
    return diff(input_function, differentiation_element, number_of_derivatives)

def newton_method(outer_function, value):
    count = 1
    first_derivative = get_derivative(outer_function, x)
    f__x = substitution_function(first_derivative, x, value)
    while f__x != 0:
        old_value = value
        f_x = substitution_function(outer_function, x, value)
        f__x = substitution_function(first_derivative, x, value)
        value = value - (f_x / f__x)
        if round(old_value, 7) == round(value, 7):
            break
        count += 1
    print(f"Final value of x is {round(value,5)}")

function = x**2 - x - 1
newton_method(function, 1)
function = x**3 - 7 * (x**2) + 8 * x - 1
newton_method(function, 5)
function = x * cos(x) - x**2
newton_method(function, 1)