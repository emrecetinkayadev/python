# ### Task 5

# Write a class that represents a connection hook and takes as initialisation arguments access_id and access_key. Create a decorator to validate if access_key is valid for provided access_id. If not print an error message into console.


# ConnectionHook(access_id=“Jane@mail.com”, access_key=“cat_12_l”)

# >>> Authorization successful.


# ConnectionHook(access_id=“Jane@mail.com”, access_key=“cat_12_”)

# >>> Wrong key, access denied!
import json 

class validator:
    def __init__(self, func) -> None:
        self.func = func
        
    def __call__(self, *args: any, **kwds: any) -> any:
        f = open('access_key_valid.json')
        access_key_valid = json.load(f)
        print(access_key_valid)
        
        if access_key_valid == getattr(self.func, "access_key"):
            print(">>> Authorization successful.")
        else:
            print(">>> Wrong key, access denied!")

@validator
class ConnectionHook:
    def __init__(self, access_id = "", access_key = "") -> None:
        self.access_id = access_id
        self.access_key = access_key
        

connectionHook = ConnectionHook(access_id='Jane@mail.com', access_key='cat_12_l')

connectionHook()