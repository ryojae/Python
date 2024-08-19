# #no.1
# def component(number):
#     lst=[]
#     for i in range(1,number+1):
#         if number % i ==0:
#             lst.append(i)
#     return lst
# def gcd(numbers):
#     lst1=component(numbers[0])
#     lst2=component(numbers[1])
#     lst3=component(numbers[2])
#     lst4=component(numbers[3])
#     for i in lst1:
#         if i in lst2 and lst3 and lst4:
#             max = i
#     return max
    
# numbers = [48, 64, 16, 32]
# max=gcd(numbers)
# print(f'최대공약수: {max}')

# #no.2
# numbers = [48, 64, 16, 32]
# lst=list(map(lambda x: [i for i in range(1,x+1) if x%i ==0] , numbers))
# result = lambda x: [i for i in x[0] if i in x[1] and x[2] and x[3]]
# print(f'최대공약수: {max(result(lst))}')

# #no.3
# data = {'apple': 5, 'banana': 2, 'orange': 8, 'kiwi': 3}
# sorted_data= sorted(data, key= lambda x: data[x])
# result={key: data[key] for key in sorted_data}
# print(result)

#no.4
def sortint(data):
    def value_key(item):
        return item[1]
    sorted_items = sorted(data.items(),key=value_key)
    sorted_data={k:v for k,v in sorted_items}
    return sorted_data
data = {'apple': 5, 'banana': 2, 'orange': 8, 'kiwi': 3}
print(sortint(data))