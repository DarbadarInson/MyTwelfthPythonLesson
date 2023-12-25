#Dictionaries
programming = {"bug" : "A software bug is an error, flaw or fault in the design, development, or operation of computer software that causes it to produce an incorrect or unexpected result, or to behave in unintended ways."}
uzbek_eng = {"olma" : "apple", 
             "qulupnay": "strawberry",
             "shaftoli": "peachr"}
number = {13 : "this is my really love number"}
print(programming["bug"])
print(uzbek_eng["olma"])
print(number[13])

#Adding new items to dictionary
uzbek_eng["o'rik"] = "apricot"
print(uzbek_eng)
#Edit Dictionary item [""]
uzbek_eng["shaftoli"] = "peach"
print(uzbek_eng["shaftoli"]) 

print("------------------------------------------")

for key in uzbek_eng:
    print(key)
    print(uzbek_eng[key])


student_scores = {
    "Harry": 81,
    "Johnny": 89,
    "Dora": 99,
    "DevanaDeveloper": 78,
    "Rustam": 82
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student]  = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

dictionary = {
    "key" : "List",
    "key2" : "Dict"
}

#Nesting

capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}
travel_log = {
    "France"  : {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany"  : {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
    "Germany" : {"Berlin", "Hamburg"}
}

#Nesting Dictionary in a list
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
     },

    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
     }
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia",2, ["Moscow", "Sant Peterburg"])
print(travel_log)






























