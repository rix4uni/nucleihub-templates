#Simple Nuclei template generator
#Rutger Harmers

# This is a prefined Nuclei YAML template, other templates could be added later
template = """
id: HackerOne XSS checker

info:
  name: Reflected XSS
  author: Rutger Harmers

requests:
  - method: GET
    path:
      - "{{target}}"

    payloads:
      rce:
        - "{{payload}}"
"""

# Creating a method to capture user input for the target and payload variables
def capture_input():
  target = input("Enter the target URL: ")
  payload = input("Enter the payload: ")
  return target, payload

# Capture the user's input for the target and payload variables
target, payload = capture_input()

# Use the input values to fill in the placeholder variables in the Nuclei template
template = template.replace("{{target}}", target)
template = template.replace("{{payload}}", payload)

# Generate the complete Nuclei YAML xss file
nuclei_yaml = template

# Output the Nuclei YAML xss file to the console
print(nuclei_yaml)

# Save the Nuclei YAML template
with open("nuclei_xss.yaml", "w") as file:
  file.write(nuclei_yaml)

# Output confirmation that the Nuclei YAML file has been generated
print("You can now use this template to validate the hacker's submission!")
