# SOLUTION-1
knapsack = [{"name": 'map', "weight": 9, "value": 150}, {"name": 'compass', "weight": 13, "value": 35}, {"name": 'water', "weight": 153, "value": 200}, {"name": 'sandwich', "weight": 50, "value": 160}, {
    "name": 'glucose', "weight": 15, "value": 60}, {"name": 'tin', "weight": 68, "value": 45}, {"name": 'banana', "weight": 27, "value": 60}, {"name": 'apple', "weight": 39, "value": 40}]
max_weight = 100
value_weight_dict = {}
for obj in knapsack:
    value_weight_dict[obj["value"]] = obj["weight"]
value_weight_list = sorted(value_weight_dict.items())
value_weight_list.reverse()
total_weight = 0
total_value = 0
for pair in value_weight_list:
    if pair[1] > max_weight:
        continue
    else:
        weight_after_item_added = total_weight + pair[1]
        if weight_after_item_added > max_weight:
            continue
        else:
            total_weight = weight_after_item_added
            total_value += pair[0]
print(total_value)


#SOLUTION - 2

ord_dict = {ord("["): ord("]"), ord("{"): ord("}"), ord("("): ord(")")}


def check_first_condition(string_brackets):
    is_pair_found = False
    for i in range(len(string_brackets)-1):
        if i % 2 == 0:
            if(ord_dict[ord(string_brackets[i])] == ord(string_brackets[i+1])):
                is_pair_found = True
            else:
                is_pair_found = False
                break
    return is_pair_found


def check_second_condition(string_brackets):
    is_pair_found = False
    neg_index = -1
    for i in range(len(string_brackets)//2):
        if(ord_dict[ord(string_brackets[i])] == ord(string_brackets[neg_index])):
            is_pair_found = True
        else:
            is_pair_found = False
            break
        neg_index -= 1
    print(is_pair_found)


string_brackets = input()

if len(string_brackets) % 2 != 0:
    print(False)
else:
    first_condition = check_first_condition(string_brackets)
    if first_condition:
        print(True)
    else:
        check_second_condition(string_brackets)
