# print("🌟Website Rating🌟")
# print()
# web_name = input("Input the website name: ")
# print()
# url = input("Input the URL: ")
# print()
# description = input("Input your a description: ")
# print()
# rating = input("Input the a star rating out 5:")

website = {"websitename":None,"Url":None, "descripton":None, "rating":None}

for name, value in website.items():
    website[name] = input(f"{name}: ")

print()
for name, value in website.items():
    print(f"{name}: {value}")
    