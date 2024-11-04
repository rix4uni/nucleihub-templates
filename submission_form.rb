# YAML template generator POC
# Rutger Harmers, Intern at HackerOne

# Define the Nuclei YAML xss template
template = <<-YAML
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
YAML

# Create a method to capture user input for the target and payload variables
def capture_input
  puts "Enter the target URL:"
  target = gets.chomp

  puts "Enter the payload:"
  payload = gets.chomp

  return target, payload
end

# Capture the user's input for the target and payload variables
target, payload = capture_input()

# Use the input values to fill in the placeholder variables in the Nuclei YAML xss template
template = template.gsub("{{target}}", target)
template = template.gsub("{{payload}}", payload)

# Generate the complete Nuclei YAML xss file
nuclei_yaml = template

# Output the Nuclei YAML xss file to the console
puts nuclei_yaml

# Save the Nuclei YAML xss file for submission to HackerOne
File.write("nuclei_xss.yaml", nuclei_yaml)

# Output confirmation that the Nuclei YAML xss file has been generated
puts "This template is generated correctly, use it to validate the hacker's submission!"
