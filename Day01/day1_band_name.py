# trim the school name or band name to 3 letters 
def trim_len(str1):
      return str1[:3]

# band name input 
print("So you came for a band name 👀 !!!")

city = input("Tell me the first 3 letters of the city you were born in: ")
first_half = trim_len(city)

school = input("The school where you spent most years (first 3 letters): ")
second_half = trim_len(school)

# checking for null input 
def band(first_half, second_half):
    if not first_half or not second_half:
        return "ERROR: Band name cannot be formed empty input received"
    elif len(first_half) < 3 or len(second_half) < 3:
        return "ERROR: Band name shorter than 3 letters in city or school input"
    return first_half + second_half

# output final 3 letter mash up of city and school band name 
band_name = band(first_half, second_half).upper()
print(f"Band name is {band_name}")
