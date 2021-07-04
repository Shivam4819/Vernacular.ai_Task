
# Assumptions:
# 1. If pick_first = true then support_multiple is false 
# 2. If pick_first = false then support_multiple is true

def validate_finite_values_entity(values, supported_values,invalid_trigger, key, support_multiple, 
    pick_first):

    # response object
    response = {
        'filled' : 'true',
        'partially_filled' : 'false',
        'trigger' : "",
        "parameters" : {
            key: []
        }
    }

    # list to store valid supported ids
    ids_stated = []
    result = True

    # check if values array len
    if len(values) > 0:
        # traverse the array to fetch each id 
        for val in values:
            # check if id is present in supported value array
            if val["value"] in supported_values:
                ids_stated.append(val["value"].upper())
            else:
                response["filled"] = 'false'
                response["partially_filled"] = 'true'
                response["trigger"] = invalid_trigger
                response["parameters"] = {}
                result = False
                break
    else:
        response["filled"] = 'false'
        response["partially_filled"] = 'false'
        response["trigger"] = invalid_trigger
        response["parameters"] = {}
        result = False

    if result: 
        if pick_first:
            response["parameters"][key] = ids_stated[0]
        else:
            response["parameters"][key] = ids_stated

    return response


# Assumptions: 
# 1. contraints will be of valid length or zero
# 2. If contraint len =0 and values len = 0 then 
# res = {
#   "filled": "true",
#   "partially_filled": "false",
#   "trigger": "",
#   "parameters": {
#       "age_stated": {}
#   }
# }  
# 3. If pick_first = true then support_multiple is false 
# 4. If pick_first = false then support_multiple is true

def validate_numeric_entity(values, invalid_trigger, key,support_multiple, pick_first, 
    constraint, var_name):

    # response object
    response = {
        'filled' : 'true',
        'partially_filled' : 'false',
        'trigger' : "",
        "parameters" : {
            key: []
        }
    }

    # if constraint is present
    if len(constraint) >0:
        # if value array is empty
        if len(values)==0:
            response["filled"] = 'false'
            response["partially_filled"] = 'false'
            response["trigger"] = invalid_trigger
            response["parameters"][key] = {}
            return response
        
        # Array to store valid numbers stasifying the constraint
        valid_numbers = []
        
        # traverse the array to fetch each number
        for val in values:
            number = val["value"]
            # replace the var_name with the number passed
            new_constraint = constraint.replace(var_name,str(number))

            # used eval function to check the constraint result
            if eval(new_constraint) :
                valid_numbers.append(number)
            else:
                response["filled"] = 'false'
                response["partially_filled"] = 'true'
                response["trigger"] = invalid_trigger

        if pick_first:
            if len(valid_numbers)==0: 
                response["parameters"][key] = {}
            else:   
                response["parameters"][key] = valid_numbers[0]
        else:
            response["parameters"][key] = valid_numbers 

    # if constraint is not present
    else:
        if pick_first:
            if len(values)==0: 
                response["parameters"][key] = {}
            else:
                response["parameters"][key] = values[0]["value"]
        else:
            valid_numbers = []
            for val in values:
                valid_numbers.append(val["value"])

            response["parameters"][key] = valid_numbers 
    
    return response