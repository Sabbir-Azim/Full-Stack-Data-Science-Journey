user = {"id" : 1}
print(print(user["email"]))

# safe method
print(user.get("email", "No email found"))
