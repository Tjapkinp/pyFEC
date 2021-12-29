from parity_check import lst_frame_parity_add,lst_frame_parity_check

# 1. Simple parity check algorithm:
parity = "even"

# Adding bit errors to encoded message:
# 0: no bit errors will be added
# 1: inverse first element of the list
# 2: inverse first and second elements of the list
add_bit_err = 0

lst_wt_parity = [1, 1, 0, 1, 0]

# Encoding: adding parity "bit" to input data list
lst_w_parity = lst_frame_parity_add(lst_wt_parity, parity=parity)

# Adding bit errors:
if add_bit_err > 0:
    lst_w_parity[0] = int(not(lst_w_parity[0]))
if add_bit_err > 1:
    lst_w_parity[1] = int(not (lst_w_parity[0]))

print("Simple parity check algorithm:")

print("Parity: " + parity)
print(lst_wt_parity)
print(lst_w_parity)

# Decoding: check for parity errors:
# output = 0: parity check error not found
# output = -1: found parity check error
if lst_frame_parity_check(lst_w_parity, parity=parity) == 0:
    print("Parity check error not found!")
else:
    print("Parity check error found!")

