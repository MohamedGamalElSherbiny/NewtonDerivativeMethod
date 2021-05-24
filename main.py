from sympy import *
x = Symbol("x")

def get_derivative(input_function, differentiation_element, number_of_derivatives, value):
    """ A function that takes a function and a number_of_derivatives choosing the number of derivates with
    an element showing the differentiation element and the value of the element and
    returns the answer after substituting """
    inner_function = diff(input_function, differentiation_element, number_of_derivatives)
    return inner_function.subs(differentiation_element, value).evalf()

def newton_method(outer_function, value):
    count = 1
    while count < 100:
        old_value = value
        first_derivative = get_derivative(outer_function, x, 1, value)
        second_derivative = get_derivative(outer_function, x, 2, value)
        print(f"x({count}): x= {value}, F(x)= {first_derivative}, F''(x)= {second_derivative}")
        value = value - (first_derivative / second_derivative)
        if round(old_value, 6) == round(value, 6):
            break
        count += 1
    print(f"Final value of x is {round(value,5)}")

function = x**2 - x - 1
newton_method(function, 1)
function = x**3 - 7 * (x**2) + 8 * x - 1
newton_method(function, 5)
function = x * cos(x) - x**2
newton_method(function, 1)