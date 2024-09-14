medical_costs = {}

# Adding the first people seperately
medical_costs['Marina'] = 6607.0
medical_costs['Vinay'] = 3225.0

# Using update to add three more people
medical_costs.update({'Connie':8886.0, 'Isaac': 16444.0, 'Valentina': 6420.0})
print(medical_costs)

# Updating Vinay's insurance cost
medical_costs['Vinay'] = 3325.0
print(medical_costs)

# Calculating the total cost
total_cost = 0
for cost in medical_costs.values():
    total_cost += cost
print(f'Total cost: {total_cost}.')

# Calculating the average cost
average_cost = total_cost / len(medical_costs)
print(f'Average Insurance Cost: {average_cost}')

# Creating lists for names and ages, so we can map patient's names to their ages
names = ['Marina', 'Vinay', 'Connie', 'Isaac', 'Valentina']
ages = [27, 24, 43, 35, 52]

# Creating a variable that holds the zipped lists
zipped_ages = zip(names, ages)

# Creating a dictionary by itarating through zipped_ages
names_to_ages = {key: value for key, value in zipped_ages}
print(names_to_ages)

# Getting the value of Marina's age and storing it in a variable
marina_age = names_to_ages.get('Marina', None)
print(f'Marina\'s age is {marina_age}')

# Creating a medical database using a dictionary
medical_records = {'Marina': {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}}

# Adding Vinay
medical_records['Vinay'] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
# Adding Connie
medical_records['Connie'] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
# Adding Isaac
medical_records['Isaac'] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
# Adding Valentina
medical_records['Valentina'] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}

print(medical_records)

# Accessing a specific piece of data
print(f'Connie\'s insurance cost is {medical_records["Connie"]["Insurance_cost"]} dollars.')

# Removing Vinay from medical_records, since he moved to a new country
medical_records.pop('Vinay')

# Iterating through the items of medical_records and printing them out
for name, record in medical_records.items():
    print(f'{name} is a {str(record["Age"])} year old {record["Sex"]} {record["Smoker"]} with a BMI of {str(record["BMI"])} and insurance cost of {str(record["Insurance_cost"])}')

# Creating a function that adds new data to medical_records or updates existing ones
def update_medical_records(name, records):
    if name in medical_records:
        print(f'{name} already exists in medical_records. Updating their information')
    else:
        print(f'Adding {name} to medical_records...')
    
    # Updating or adding the new data
    medical_records[name] = records
    print(f'{name} added successfully!')


# Testing 

# New data to be added
new_person = {
    "Age": 30, 
    "Sex": "Male", 
    "BMI": 22.4, 
    "Children": 1, 
    "Smoker": "Non-smoker", 
    "Insurance_cost": 7000.0
}
# Adding a person in the records
update_medical_records('Alex', new_person)
print(medical_records)

# New data to update Connie's record
updated_connie = {
    "Age": 44,  # Changing Connie's age
    "Sex": "Female", 
    "BMI": 25.5,  # Updated BMI
    "Children": 3, 
    "Smoker": "Non-smoker", 
    "Insurance_cost": 8900.0  # Updated insurance cost
}

# Updating Connie's record
update_medical_records('Connie', updated_connie)
print(medical_records)