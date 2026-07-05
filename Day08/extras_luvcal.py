def love_calculator(name1, name2):
     
    # True Function 
     def true(n1, n2):
          total_true = 0
          namelist = [n1, n2]
          for name in namelist:
               for i in name:
                    if i in "true":
                         total_true += 1
          return total_true
     
     #Love Functuion
     def love(n1, n2):
          total_love = 0
          name_list = [n1, n2]
          for name in name_list:
               for i in name:
                    if i in "love":
                         total_love += 1
          return total_love
     
     love_total = love(name1, name2)
     true_total = true(name1, name2)
     final_total = int((true_total * 10) + love_total)
     return final_total

# user input
name1 = input(" Input Name 1 = ").lower()
name2 = input(" Input Name 2 = ").lower()

# function call
love_cal = love_calculator(name1, name2)
print(f"total % = {love_cal}")