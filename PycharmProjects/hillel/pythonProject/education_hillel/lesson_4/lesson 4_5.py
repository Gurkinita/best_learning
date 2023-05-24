subjects = {
            'science':{
                      'phisics': ['nuclear phisics', 'optics', 'thermodynamics'],
                      'computer science': {},
                      'biology': {}
            },
            'humanities':{},
            'public':{}
            }

for key in subjects['science'].keys():
    print(key)


for value in subjects['science']['phisics']:
    print(value)

