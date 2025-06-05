import json
def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)
animals_data = load_data('animals_data.json')


with open('animals_template.html', 'r') as fileobj:
    content = fileobj.read()
output = ''  # define an empty string
for animal_data in animals_data:
    # append information to each string
    output += f"Name: {animal_data.get('name')}\n"
    output += f"Diet: {animal_data.get('characteristics', {}).get('diet')}\n"
    output += f"locations: {animal_data.get('locations', [])}\n"
    output += f"type: {animal_data.get('characteristics', {}).get('type')}\n"

print(output)

html_content = content.replace("__REPLACE_ANIMALS_INFO__", output)
with open('animals.html', 'w') as fileobj:
    fileobj.write(html_content)

#bring animal data into html