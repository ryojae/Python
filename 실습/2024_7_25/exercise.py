# #no.1
# def most_frequent_word(filename):
#     try:
#         with open(filename,encoding="utf-8") as file:
#             text = file.read()
#             words = text.split()
#             word_count = {}
#             for word in words:
#                 if word in word_count:
#                     word_count[word] += 1
#                 else:
#                     word_count[word] = 1
#             most_frequent = max(word_count, key=word_count.get)
#         return most_frequent, word_count[most_frequent]
#     except FileNotFoundError:
#         return "File not found."
# # 함수 호출
# filename = "info.txt"
# result = most_frequent_word(filename)
# print(f"The most frequent word is '{result[0]}' with {result[1]} occurrences.")

# #no.2
# import string
# def remove_punctuation1(input_string):
#     sans_punctuation_documents = []
#     for i in input_string:
#     # TODO
#         sans_punctuation_documents.append(i.translate(str.maketrans('','',string.punctuation)))
#         print(sans_punctuation_documents)
#     return ''.join(sans_punctuation_documents)
# def remove_punctuation2(input_string):
#     return input_string.translate(str.maketrans('', '',string.punctuation))
# # 함수 호출
# sample_text = "Hello, world! How are you doing? It's a great day."
# clean_text1 = remove_punctuation1(sample_text)
# print("Clean text1:", clean_text1)

# #no.3
# def apply_discount(prices):
#     discount_rate = 0.20
#     discounted_prices = [price * (1 - discount_rate) for price in
#     prices]
#     return discounted_prices
# # 함수 호출 및 출력
# original_prices = [100, 200, 300, 400]
# discounted_prices = apply_discount(original_prices)
# print("할인된 가격들:", discounted_prices)

# #no.4
# def tally_votes(votes):
#     vote_count = {}
#     for vote in votes:
#         if vote in vote_count:
#             vote_count[vote] += 1
#         else:
#             vote_count[vote] = 1
#     winner = max(vote_count, key=vote_count.get)
#     return winner, vote_count[winner]
# # 함수 호출 및 출력
# votes = ["Alice", "Bob", "Alice", "Bob", "Alice", "Charlie","Alice", "Bob",
# "Alice", "Bob", "Alice", "Charlie","Alice", "Bob", "Alice", "Bob", "Alice",
# "Charlie","Alice", "Bob", "Alice", "Bob", "Alice", "Charlie","Alice",
# "Bob", "Alice", "Bob", "Alice", "Charlie","Alice", "Bob", "Alice", "Bob",
# "Alice", "Charlie","Alice", "Bob", "Alice", "Bob", "Alice",
# "Charlie","Alice", "Bob", "Alice", "Bob", "Alice", "Charlie","Alice",
# "Bob", "Alice", "Bob", "Alice", "Charlie","Alice", "Bob", "Alice", "Bob",
# "Alice", "Charlie","Alice", "Bob", "Alice", "Bob", "Alice",
# "Charlie","Alice", "Bob", "Alice", "Bob", "Alice", "Charlie","Alice",
# "Bob", "Alice", "Bob", "Alice", "Charlie","Alice", "Bob", "Alice", "Bob",
# "Alice", "Charlie"]
# winner, count = tally_votes(votes)
# print(f"승자는 {winner}이며, {count}표를 얻었습니다.")

# #no.5
# def calculate_average_temperatures(temperatures):
#     weekday_temps = temperatures[:5] # 월요일부터 금요일
#     weekend_temps = temperatures[5:] # 토요일과 일요일
#     weekday_average = sum(weekday_temps) / len(weekday_temps)
#     weekend_average = sum(weekend_temps) / len(weekend_temps)
#     return weekday_average, weekend_average
# # 함수 호출 및 출력
# week_temperatures = [31, 30, 30, 27, 31, 30, 31]
# weekday_avg, weekend_avg = calculate_average_temperatures(week_temperatures)
# print(f"지난주 전국 평일 평균 온도: {weekday_avg}도, 주말 평균 온도:{weekend_avg}도")

