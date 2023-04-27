# ------------------------------------
# Functions
# ------------------------------------

def build_full_name(first_name:str, last_name:str):
    full_name = first_name + " " + last_name
    return full_name.upper()

print(build_full_name("Jim", "McFly"))
print(build_full_name(first_name="Jim", last_name="McFly"))
print(build_full_name(last_name="McFly", first_name="Jim",))