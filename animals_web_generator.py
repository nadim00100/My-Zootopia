import json
def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)
animals_data = load_data('animals_data.json')
# Iterate through each animal and print the required fields
for animal in animals_data:
    name = animal.get('name')
    diet = animal.get('characteristics', {}).get('diet')
    locations = animal.get('locations', [])
    animal_type = animal.get('characteristics', {}).get('type')

    if name:
        print(f"Name: {name}")
    if diet:
        print(f"Diet: {diet}")
    if locations:
        print(f"Location: {locations[0]}")
    if animal_type:
        print(f"Type: {animal_type}")

    print()  # Blank line between animals

#access data from json file”