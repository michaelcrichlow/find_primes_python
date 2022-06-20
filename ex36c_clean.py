# ----- EX.  36.6 PRIME NUMBER PUZZLE - PART 2-------------
# ---------------------------------------------------------
# NOTE: This is an exercise to find the first 100 primes.


def check_if_prime(num: int) -> bool:
    """Returns True if 'num' is prime. Else returns False."""

    is_prime = False
    divisor = num - 1
    exit_loop = False

    while (divisor > 0) and (exit_loop == False):
        if (num % divisor == 0) and (divisor != 1):
            is_prime = False    
            exit_loop = True
        elif (num % divisor == 0) and (divisor == 1):
            is_prime = True
        
        divisor -= 1
    
    return is_prime



def number_of_primes(num: int) -> list[int]:
    """Returns a list with 'num' number of primes."""

    local_list = []
    i = 3
    add_to_list = False

    if num == 0:
        return local_list
    elif num == 1:
        local_list.append(2)
        return local_list
    elif num > 1:
        local_list.append(2)

        while len(local_list) < num:

            add_to_list = check_if_prime(i)

            if (add_to_list == True):
                local_list.append(i)

            i += 1

     
    return local_list


def main() -> None:

    test_list = number_of_primes(100)
    print(test_list)


if __name__=='__main__':
    main()