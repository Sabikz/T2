myDict = {
    "postId": 1,
    "id": 1,
    "name": "id labore ex et quam laborum",
    "email": "Eliseo@gardner.biz",
    "body": "laudantium enim quasi est quidem magnam voluptate ipsam eostempora quo necessitatibus"
}

# 1) Вывести на экран "name"
print(myDict["name"])
# 2) Вывести длину значения "email"
print(len(myDict["email"]))
# 3) Вывести все ключ
print(myDict.keys())
# 4) Вывести все значения
print(myDict.values())
# 5) Вывести длину значения под ключом "body"
print(len(myDict["body"]))
# 6) Заменить пару "email" на "justcode@gmail.com" или на любую другую
myDict["email"] = "justcode@gmail.com"
print(myDict)
# 7) Добавить пару дата и ее значение (14.05.2022)
myDict["data"] = "14.05.2022"
print(myDict)
# 8) Увеличить значение id на +1
myDict["id"] +=1
print(myDict)
# 9) Удалить пару "postId"
del myDict["postId"]
print(myDict)