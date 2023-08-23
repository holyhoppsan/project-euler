from timeit import default_timer as timer

def calculate_sum_of_multiples_3_5_brute(r):
    start = timer()
    sum = 0
    for index in range (1, r):
        if index % 3 == 0 or index % 5 == 0:
            print('Found multiple: ' + str(index))
            sum += index
            index += 1
    end = timer()

    print ('The total sum is: ' + str(sum))
    print(f'Completed in () executed in {(end-start):.6f}s')


def calculate_partial_sum_of_mulitples_of_n_below_x(n, x):
    range = (x-1) / n
    sum = (n * ((range) * (range+1)))/2
    return sum

def calculate_multiples_of_x_and_y_below_r(x, y, r):
    start = timer()
    result = calculate_partial_sum_of_mulitples_of_n_below_x(x, r) + calculate_partial_sum_of_mulitples_of_n_below_x(y, r) - calculate_partial_sum_of_mulitples_of_n_below_x(x*y, r)
    end = timer()
    print ('The total sum is: ' + str(result))
    print(f'Completed in () executed in {(end-start):.6f}s')

if __name__ == "__main__":
    limit = 1000
    calculate_sum_of_multiples_3_5_brute(limit)

    calculate_partial_sum_of_mulitples_of_n_below_x(3, limit)

    calculate_multiples_of_x_and_y_below_r(3, 5, limit)