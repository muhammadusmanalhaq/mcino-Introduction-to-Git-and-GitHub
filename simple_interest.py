# simple_interest.py
# Fix: corrected formula and variable naming typo

def simple_interest(p, t, r):
    """
    Calculate simple interest.
    p: principal amount
    t: time period in years
    r: annual rate of interest
    Returns: p * t * r / 100
    """
    return (p * t * r) / 100

if __name__ == "__main__":
    print(simple_interest(1000, 2, 5))
