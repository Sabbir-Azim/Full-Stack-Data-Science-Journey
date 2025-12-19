defaults = {"theme": "light", 
            "audio": "on"}

user_pref = {"theme": "dark"}

print(f"For python 3.9+ (defaults | user_pref) :  {defaults | user_pref}")


defaults.update(user_pref)
print(f"For python 3.9- (update()) :  {defaults}")