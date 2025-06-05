import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

# Load JSON data
animals_data = load_data('animals_data.json')

# Load HTML template
with open('animals_template.html', 'r') as fileobj:
    content = fileobj.read()
def serialize_animal(animal_obj):
    output = ''
    output += '<li class="cards__item">'
    output += f"Name: {animal.get('name', 'Unknown')}<br/>\n"
    output += f"Diet: {animal.get('characteristics', {}).get('diet', 'Unknown')}<br/>\n"
    output += f"Locations: {', '.join(animal.get('locations', []))}<br/>\n"
    output += f"Type: {animal.get('characteristics', {}).get('type', 'Unknown')}<br/>\n"
    output += '</li>' #
    return output
# Build the output string with animal info
output = ''
for animal in animals_data:
    output += serialize_animal(animal)

print(output)

# Replace the placeholder with the actual animal info
html_content = content.replace("__REPLACE_ANIMALS_INFO__", output)

# Write to a new HTML file
with open('animals.html', 'w') as fileobj:
    fileobj.write(html_content)


#improve card item html