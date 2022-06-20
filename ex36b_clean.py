# ----- EX.  36.6 PRIME NUMBER PUZZLE -------------
# -------------------------------------------------
# NOTE: This is an exercise to find all the primes from 1 to 100.


def reduce_to_primes(l: list[int]) -> list[int]:
    """Finds the primes in the formal parameter and returns them as a list."""

    local_list = []

    for i in l:
        if i == 2:
            local_list.append(i)
        elif i > 2:
            divisor = i - 1
            exit_loop = False
            while divisor > 0 and exit_loop == False:
                if (i % divisor == 0) and (divisor != 1):
                    # exit the loop and go onto the next index(i)
                    exit_loop = True
                elif (i % divisor == 0) and (divisor == 1):
                    local_list.append(i)

                divisor -= 1

    return local_list


def main() -> None:

    odd_numbers_list = [i for i in range(1, 101, 2)]
    odd_numbers_list.insert(1, 2)

    prime_numbers_list = reduce_to_primes(odd_numbers_list)
    print(prime_numbers_list)


if __name__=='__main__':
    main()