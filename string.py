#string are immutable (unchangeable)
name = "Justin Bieber"

actor = "Ryan Reynolds"
print(actor[5:])

address = "816 Granville ST, Vancouver, BC"
print(address.upper())
print(address.lower())
print(address.capitalize())

# find - if not found, give negative one
# index - if not found, give error
print(address.find("Vancouver"))

user_id = "19b243"
if user_id.isdigit():
    print("Valid User ID")
elif user_id.isalpha() or user_id.isalnum():
    print("Invalid User ID: use number only")

street_address = "816 Granville ST"
city = "Vancouver"
province = "BC"

full_message = f"I live in {street_address}, {city}, {province}."
print(full_message)

cities = ["Vancouver", "Burnaby", "Richmond", "West Vancouver", "North Vancouver", "Surrey"]

#join : string option so before you put join, make sure data type is string
print(" !! ".join(cities))