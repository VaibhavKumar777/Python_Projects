def commands(binary_str):
    actions = ["wink", "double blink", "close your eyes", "jump"]
    result = []
    for i in range(4):
        if binary_str[-(i+1)] == "1":
            result.append(actions[i])

    if len(binary_str) >=5 and binary_str[0] == "1":
        result.reverse()
    return result
    
