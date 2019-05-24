import math

def print_bitwise (iteration, number):
    shifts = iteration(number)
    N = shifts - 1
    for i in range(shifts):
        if(2**N > 9):
            print (2**N, end='|')
        else:
            print('0'+ str(2**N), end='|')
        N-=1
    print("\n")

def for_loop (iteration, number):
    shifts = iteration(number)
    val = shifts - 1
    for i in range(shifts):
        if(number & 1<<val > 0):
            print(' ' + str(1) + ' ', end = '')
        else:
            print(' ' + str(0) + ' ', end = '')
        val -= 1

def while_loop(iteration, number):
    shifts = iteration(number)
    i= shifts - 1
    while i >= 0:
        if (number & (1 << i)) > 0:
            print(str(' 1 '), end='')
        else:
            print(str(' 0 '), end='')
        i -= 1

def iteration (number):
    log10 = math.log(number + 1)
    # print("Log10: ", log10)
    log2 = log10 / math.log(2)
    # print("Log2: ", log10)
    shifts = math.ceil(log2)
    # print("Shifts", shifts)
    return shifts

number = int(input("Please enter a number you would like converted: "))

print("\nFor Loop Example: ", number, '\n')
print_bitwise(iteration,number)
for_loop(iteration, number)

print("\nWhile Loop Example: ", number, '\n')
print_bitwise(iteration,number)
while_loop(iteration,number)
