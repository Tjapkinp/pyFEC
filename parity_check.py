# def parity_check_lists(inp_data_list,n_bits_per_frame=6,parity='odd'):


def lst_frame_parity_add(inp_frame_list, parity="even"):
    if parity == "even":
        parity_value = 0
    else:  # odd:
        parity_value = 1

    check_parity = sum(inp_frame_list) % 2
    if check_parity == 0:
        outp_frame_list = inp_frame_list + [parity_value]
    else:
        outp_frame_list = inp_frame_list + [int(not (parity_value))]

    return outp_frame_list


# Parity check
def lst_frame_parity_check(inp_frame_list, parity="even"):
    check_parity = sum(inp_frame_list) % 2
    if check_parity == 0:
        if parity == "even":  # parity to even:
            return 0
        else:
            return -1
    else:  # check_parity > 0:
        if parity == "even":
            return -1
        else:  # parity to odd:
            return 0


