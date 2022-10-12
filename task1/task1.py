# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_str = "142578 45абв44 ооооабв 87654"

my_list = my_str.split(" ")

# result = ""

# for word in my_list:
#     if "абв" not in word:
#         result += word + " "

# print(result.strip())

result = []
for word in my_list:
    if "абв" not in word:
        result.append(word)

print(" ".join(result))