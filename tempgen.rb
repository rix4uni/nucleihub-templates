# Valid8 YAML template generator POC
# Rutger Harmers

require 'sinatra'
require 'terrapin'
require 'pathname'
require 'json'

# Variables for the base templates
open_redirect_template = File.read("templates/openredirect.yaml")
phpinfo_template = File.read("templates/phpinfo.yaml")
rxss_template = File.read("templates/rxss.yaml")

# Method to capture user input for the target and payload variables
def capture_input(target, payload)
  return target, payload
end

# Sinatra route to the submission html page
get '/' do
  # return HTML page for the submission form
  return File.read("submission.html")
end
  
post '/template' do
  # This form lets the hacker choose the base template for their submission
  template =
    case params[:vuln_category]
    when "1" then rxss_template
    when "2" then open_redirect_template
    when "3" then phpinfo_template
    else
      return "Invalid selection. Exiting program."
    end

  # Captures the hacker's input for the target and payload variables
  target, payload = capture_input(params[:target], params[:payload])
  payload = payload.gsub('"', '\"')
  target = target.gsub('"', '\"')
  payload = payload.gsub("'", "\'")
  target = target.gsub("'", "\'")

  # Gets the current (start) time
  start_time = Time.now

  # Uses the input values to fill in the placeholder variables in the selected template
  template = template.gsub("{{target}}", target)
  template = template.gsub("{{payload}}", payload)

  # Generates the complete Nuclei YAML file
  nuclei_yaml = template

  # Gets the current (end) time
  end_time = Time.now

  # Saves the Nuclei YAML file to the current directory
  File.write("nuclei_template.yaml", nuclei_yaml)

  # Outputs the Nuclei YAML file to the terminal
  puts ""
  puts nuclei_yaml    
  puts ""

  # Calculates the elapsed time
  elapsed_time = (end_time - start_time)
  # Calculates the elapsed time in nanoseconds 
  elapsed_microseconds = elapsed_time.to_f * 1_000_000
  # Outputs the elapsed time
  puts "Generation time: #{elapsed_microseconds}μs"

  # Executes template and outputs result to terminal
  line = Terrapin::CommandLine.new("nuclei", "-t :template_file -u :target -silent -json")
  template_path = Pathname.new("nuclei_template.yaml").realpath.to_s

  puts "Running #{line.command(template_file: template_path, target: target)}..."

  begin
    result = line.run(template_file: template_path, target: target)
    json = JSON.parse(result)
  rescue JSON::ParserError
    puts "Nuclei returned invalid json!"
    send_file 'failed.html'
    puts JSON.pretty_generate(json)
    return
  end

  if json["matcher-status"]
    puts "SUCCESS! Matched line: #{json["matched-line"]}"
  else
    puts "FAILED! No match :("
  end

  puts "[DEBUG]"
  puts JSON.pretty_generate(json)
  
  # Display the succes page
  send_file 'success.html'
end
  
