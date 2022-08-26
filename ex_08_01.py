def chop(t_list):
    if type(t_list) == list and len(t_list) > 2:
        del t_list[0]
        del t_list[len(t_list) - 1]
        return None
    else:
        print('Not a valid list!')
        exit()

def middle(t_list):
    if type(t_list) == list and len(t_list) > 2:
        del t_list[0]
        del t_list[len(t_list) - 1]
        return t_list
    else:
        print('Not a valid list!')
        exit()

basic_list = [1,2,3]
# chop(basic_list)
print(middle(basic_list))