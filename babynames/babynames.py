
#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  file_content = open(filename, 'r').read()
  
  year = extract_year(file_content)
  name_directory = extract_names_with_rank(file_content)
  return build_name_list_for_year(year, name_directory)
  
def extract_year(text):
  match = re.search('Popularity in (\d{4})', text)
  if match:
    return match.groups(0)
  else:
    return 'unknown'

def extract_names_with_rank(text):
  matches = re.findall('<td>(\d+)</td><td>([a-zA-Z]+)</td><td>([a-zA-Z]+)</td>', text)
  name_directory = {}
  for match in matches:
    (rank, boy, girl) = match
    name_directory[boy] = rank
    name_directory[girl] = rank
  
  return name_directory

def build_name_list_for_year(year, name_rank_dict):
  name_list_for_year = [year];
  for name, rank in sorted(name_rank_dict.items()):
    name_list_for_year.append('%s %s' % (name, rank))
  return name_list_for_year
  
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  for file in args:
    names_of_year = extract_names(file)
    
    output = 'Year: %s\n' % names_of_year[0]
    for name in names_of_year[1:]:
      output = output + '\t%s\n' % name
	  
    if summary:
      summary_file = open(file + '.summary', 'w')
      summary_file.write(output)
    else:
      print(output)

if __name__ == '__main__':
  main()
