# YAML template generator POC
# Rutger Harmers, Intern at HackerOne

# Define the Nuclei YAML templates for different vulnerability categories (just two for now)
xss_template = <<-YAML
id: Reflected XSS check

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

    checks:
      - type: regex
        target: body
        pattern: "{{payload}}"
YAML

open_redirect_template = <<-YAML
id: Open Redirect checker

info:
  name: Open redirect
  author: Rutger Harmers

requests:
  - method: GET
    path:
      - "{{target}}"

    checks:
      - type: regex
        target: location
        pattern: "{{payload}}"
YAML

# Create a method to capture user input for the target and payload variables
def capture_input
  puts ""
  puts "Enter the target URL:"
  target = gets.chomp

  puts ""
  puts "Enter the payload:"
  payload = gets.chomp

  return target, payload
end

# Ask the user to choose a vulnerability category
puts ""
puts "Please choose a vulnerability category (1, 2):"
puts "-------------------"
puts "1. Reflected XSS"
puts "2. Open Redirect"
puts "-------------------"
vuln_category = gets.chomp

# Select the right template based on user input
if vuln_category == "1"
  template = xss_template
elsif vuln_category == "2"
  template = open_redirect_template
else
  puts ""
  puts "Please choose a category from the list above, these are currently the only supported vulnerability categories."
  exit
end

# Capture the user's input to use for the target and payload variables
target, payload = capture_input()

# Use the input values to fill in the placeholder variables in the selected template
template = template.gsub("{{target}}", target)
template = template.gsub("{{payload}}", payload)

# Generate the complete Nuclei YAML file
nuclei_yaml = template

# Output the Nuclei YAML file to the console
puts ""
puts "-------------------"
puts nuclei_yaml
puts "-------------------"

# Save the Nuclei YAML file for submission to Nuclei
File.write("nuclei_#{vuln_category}.yaml", nuclei_yaml)

# Output confirmation that the Nuclei YAML file has been generated
puts ""
puts "This template is generated correctly, now use it to validate the hacker's submission!"
