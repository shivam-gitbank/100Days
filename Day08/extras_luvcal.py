def love_calculator(name1, name2):
    # True Function 
     def true(n1, n2):
          total_true = 0
          namelist = [n1, n2]
          for name in namelist:
               for i in name:
                    if i in "True":
                         total_true += 1
          return total_true
     true_total1 = true(name1, name2)
     return true_total1

true = int(love_calculator("Angela Yu", "Jack Brauer")) * 10
print(true)