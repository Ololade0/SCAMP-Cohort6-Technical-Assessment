number = (int(input("Enter a number: ")))


def prime_number(number):
    """ Checks if the inputted number is a prime number """
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return "It isn't a prime number"
                break
    return "It is a prime number"


print(f'{number} = {prime_number(number)}')