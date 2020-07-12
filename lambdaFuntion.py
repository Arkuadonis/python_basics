#new way to represent a funtion - lambda funtion
#python allows nested data structure

NameAndAddress = [
    {"name": "arku", "address": "madurai"},
    {"name": "thosar", "address": "maharastra"},
    {"name": "chand", "address": "delhi"}
]

# NameAndAddress.sort() - TypeError '<' ** confusion to sort based on name or address?

#Solution 1
# def f(x):
#     return x["address"]
# NameAndAddress.sort(key=f)

#solution 2 using lambda funtion
NameAndAddress.sort(key = lambda x: x["address"])

print(NameAndAddress)