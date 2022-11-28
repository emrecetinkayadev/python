import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 80, "name": "Joe", "views": 100000},
        {"likes": 1000, "name": "How to make REST API", "views": 80000},
        {"likes": 35, "name": "Tim", "views": 2000}]

# response = requests.get(BASE + "helloworld/bill")
# print(response.json())

# response = requests.put(BASE + "helloworld/jessica",
#                         {"age": 15, "gender": "female"})
# print(response.json())

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

# response = requests.get(BASE + "video/6")
# print(response.json())

response = requests.get(BASE + "video/1")
print(response.json())

response = requests.delete(BASE + "video/1")
print(response)

response = requests.get(BASE + "video/1")
print(response.json())

# response = requests.get(BASE + "video/1")
# print(response.json())

# response = requests.get(BASE + "video/6")
# print(response.json())
