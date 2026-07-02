def life_in_weeks(age):
    max_life = 90
    years_left = max_life - age
    week_left = years_left * 52 # as average weeks are 52
    return week_left
    
#age in weeks
age = int(input("Hi whats your age "))
print(f"life left in weeks {life_in_weeks(age)}")
