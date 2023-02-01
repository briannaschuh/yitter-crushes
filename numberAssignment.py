def create_dict(data):
    numbers = {}
    number = 0
    response_list = []
    for response in data:
        temp = []
        for handle in response:
            if handle != '': 
                if handle[0] != "@":
                    handle = "@" + handle
                if handle.strip().lower() not in numbers:
                    numbers[handle.strip().lower()] = number
                    number += 1
                temp.append(handle.strip().lower())
        response_list.append(tuple(temp))
            
    return numbers, number, response_list
                
    
    