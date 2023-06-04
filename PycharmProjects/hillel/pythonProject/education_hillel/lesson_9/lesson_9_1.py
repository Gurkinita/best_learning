import json

def find_group_with_most_women(json_data):
    max_women_count = 0
    max_women_group_id = None


    for group in json_data:
        women_count = 0


        for participant in group['people']:

            if participant['gender'] == 'Female' and participant['year'] > 1977:
                women_count += 1

        if women_count > max_women_count:
            max_women_count = women_count
            max_women_group_id = group['id_group']

    return max_women_group_id, max_women_count

with open('/home/julia/Downloads/group_people.json') as file:

    data = json.load(file)


group_id, women_count = find_group_with_most_women(data)


print("Group ID:", group_id)
print("Women born after 1977:", women_count)
