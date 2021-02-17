import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Driver creates some newlines which mess up the unittest.
driver = webdriver.Chrome(ChromeDriverManager().install())


def selenium(driver):
    """
    >>> selenium()
    True
    """
    url = 'https://campbells.com.au/convenience'
    username = '0032353419'
    password = 'Australia@1'
    driver.get(url)
    driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
    driver.find_element_by_class_name('loginLink').click()
    time.sleep(1)
    driver.find_element_by_id("j_username").send_keys(username)
    driver.find_element_by_id("j_password").send_keys(password)
    driver.find_element_by_id("loginButton").click()
    return True


# An example of code that uses doctests to automatically test code.
def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n + 1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
