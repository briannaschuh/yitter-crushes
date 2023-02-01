def create_edges(data, numbers_dict):
    list_edges = []
    temp = []
    temp.append('responder')
    temp.append('crush')
    list_edges.append(temp)
    for response in data:
        responder = numbers_dict[response[0]]
        for i in range(1, len(response)):
            temp = []
            temp.append(responder)
            temp.append(numbers_dict[response[i]])
            list_edges.append(temp)

            #list_edges.append((responder, numbers_dict[response[i]]))
    return list_edges
            
    