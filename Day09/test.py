travel_log = {
    "France": {
        'cities': ['paris', 'Lille', 'Dujon'],
        'visted': 12,
              },
    "Germany": {'cities': ['frankfurt', 'stuttgart', 'Berlin'],
                'visited': 5,
               },
}

print(travel_log['Germany']['cities'][1]) # as tavel_log[France] is itself a list i can index it directly 
# think of it as frace named list - index 1 value is -Lillie
nested = ['A', 'B', ['C', 'D']]
print(nested[2][1])