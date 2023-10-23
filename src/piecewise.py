def piecewise_linear_interpolation(
    x_zero: int, x_one: int, y_zero: int, y_one: int
) -> str:
    """
    Calculate the piecewise linear interpolation for two points.

    Paramaters:
        x_zero (int): Starting time point.
        x_one (int): Ending time point.
        y_zero (int): Starting temperature.
        y_one (int): Ending temperature.

    Returns:
        equation (string): The resulting equation.
    """
    slope = ((y_one - y_zero) / (x_one - x_zero))
    y_intercept = y_zero - (slope * x_zero)
    y_intercept = format(y_intercept, '.4f')

    return str(y_intercept)
