# #no.1
# people=[{'name':'John', 'age':45},
#         {'name':'Diana', 'age':32},
#         {'name':'Tom', 'age':20}]

# sorted_people = sorted(people,key = lambda x: x['age'])
# print(sorted_people)

# #no.2
# from functools import reduce

# numbers=[5,8,6,10,9,2]
# max_num=reduce(lambda x,y: x if x>y else y,numbers)
# print(max_num)

# #no.3
# numbers=[3,5,7,10,2,6]
# lst = list(filter(lambda x: x > 5,numbers))
# print(lst)

# #no.4
# words = ['hello','world','python','programming']
# capitalized_words=list(map(lambda word: word.capitalize(), words))
# print(capitalized_words)

# #no.5
# products=[{'name':'Product A','price':150,'stock':5},
#           {'name':'Product B','price':120,'stock':12},
#           {'name':'Product C','price':50,'stock':20},
#           {'name':'Product D','price':200,'stock':9}]
# lst = list(filter(lambda x: x['price']>100 and x['stock']>=10,products))
# print(lst)

# #no.6
# from functools import reduce
# scores = [88,92,78,90,84,100,95]
# average_scores = reduce(lambda x, y: x+y,scores)/len(scores)
# print(average_scores)

# #no.7
# words = ['apple','pear','banana','cherry','kiwi']
# lst = list(filter(lambda x: len(x)>=5 , words))
# print(lst)

# #no.8
# numbers=[1,2,3,4,5]
# lst=list(map(lambda x: x**2,numbers))
# print(lst)

# #no.9
# products = [
# {"name": "Keyboard", "price": 150, "stock": 25},
# {"name": "Mouse", "price": 70, "stock": 90},
# {"name": "Monitor", "price": 200, "stock": 50},
# {"name": "USB cable", "price": 10, "stock": 150}
# ]
# lst=list(filter(lambda x: x['price']>= 100 and x['stock']>=50 , products))
# print(lst)

# #no.10
# words = ['hello','world','python','code']
# lst=list(map(lambda x: len(x), words))
# print(lst)

# #no.11
# from functools import reduce
# scores=[88,92,78,90,84,100,95]
# aver = reduce(lambda x, y: x+y,scores)/len(scores)
# print(aver)
# lst= list(filter(lambda x: x>aver, scores))
# print(lst)
