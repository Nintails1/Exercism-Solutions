"""Leap year calculator"""

def leap_year(year):
    """Determine if the inputted year is a leap year.

    Parameters:
        year (int): The value of the year being checked.

    Return:
        Boolean: A True/False depending if year was a leap year or not.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
