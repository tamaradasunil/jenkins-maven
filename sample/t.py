#importing the regex module
import re

#defining the replace method
def replace(filePath, text, subs, flags=0):
    with open(file_path, "r+") as file:
        #read the file contents
        file_contents = file.read()
        text_pattern = re.compile(re.escape(text), flags)
        file_contents = text_pattern.sub(subs, file_contents)
        file.seek(0)
        file.truncate()
        file.write(file_contents)

    
file_path="sample/data.txt"
text="pyton"
subs="$patchnumber"
#calling the replace method
replace(file_path, text, subs)
