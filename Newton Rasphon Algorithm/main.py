import time, math

x = 180
x_list = [x]



def f_x(x):
    return round(round((x * round(math.sin(math.radians(x)),4)), 4) + round(math.cos(math.radians(x)),4), 4)
def f_prime_x(x):
    return round(x * round(math.cos(math.radians(x)), 4), 4)

def new_raph(prev_x, f_pre_x, f_prime_prev_x):
    val = round(prev_x - round((f_pre_x / f_prime_prev_x),4),4)
    return val

i = 0
j = 0
print("The intital value of x", x)
print()
for k in range(0,300):
    if x_list[i] == x_list[i-1] and len(x_list) != 1:
        print("Processing answer.....")
        time.sleep(2)
        print("The real square root of the equation is, ", x)
        break
    estimate_f_x = f_x(x)
    estimate_f_prime_x = f_prime_x(x)
    print(f"\tf(X{i}) = ", estimate_f_x, f" and f'(x{i}) = ", estimate_f_prime_x)
    print(f"\tf(x{i}) / f'(x{i}) = ", round(estimate_f_x / estimate_f_prime_x, 4))
    new_x = new_raph(x, estimate_f_x, estimate_f_prime_x)
    print(f"The value of x{i+1} for the ", i+1, " iteration is ", new_x, "\n\n")
    x_list.append(new_x)
    x = new_x
    i +=1