#return multiple variable using ','
def multiple():
    operation="Sum"
    result=5+10
    return [operation,result]

result_list = multiple()
print(result_list[1])