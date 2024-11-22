#!/usr/bin/env python3

def array_of_names(persons):
    full_names = []
    for first_name, last_name in persons.items():
        
        full_names.append(f"{first_name.capitalize()} {last_name.capitalize()}")
    return full_names


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
