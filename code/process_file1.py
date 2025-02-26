'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.
#ur mom
Screenshot available as process_file.png
'''
import streamlit as st
import packaging 
from io import StringIO   
import json 

st.title("process file") 

file = st.file_uploader("Upload package file:") 

if file: 
    filename=file.name 
    json_filename = filename.replace(".txt",".json") 
    packages = []
    text = StringIO(file.getvalue().decode("utf-8")).read() 
    for line in text.split("\n"): 
        line = line.strip() 
        pack = packaging.parse_packaging(line) 
        total = packaging.calc_total_units(pack) 
        unit = packaging.get_unit(pack) 
        packages.append(pack) 
        st.info(f"{line} ➡️ Total 📦 Size: {total} {unit}") 
        count = len(packages) 
    with open(f"./data/{json_filename}", "w") as f: 
        json.dump(packages, f, indent=4) 
    st.success(f"{count} packages written to {json_filename} ", icon="💾")
'''
DRAFT TWO 
file = st.file_uploader("upload file")
filename = file.name
json_filename = filename.replace(".txt",".json")
packages = []
text = StringIO(file.getvalue().decode("utf-8")).read()
for line in text.split("\n"):
    line = line.strip()
    pack = packaging.parse_packaging(line)
    total = packaging.calc_total_units(pack)
    unit = packaging.get_unit(pack)
    packages.append(pack)
    st.info(f"{line} ➡️ Total 📦 Size: {total} {unit}")
count = len(packages)
with open(f"./data/{json_filename}", "w") as f:
    json.dump(packages, f, indent=4)
st.success(f"{count} packages written to {json_filename}", icon="💾")
'''
'''
DRAFT ONE
if file:
    file.seek(0)
    file_contents = file.read().decode("utf-8")
    file.seek(0)
    parsed_file = packaging.parse_packaging(file_contents)
    total = packaging.calc_total_units(parsed_file)
    unit = packaging.get_unit(parsed_file)
    st.text(parsed_file)
    for item in parsed_file:
        name = list(item.keys())[0]
        size = list(item.values())[0]
        st.info(f"{name} ➡️ {size}")
    st.success(f"Total 📦 Size: {total} {unit}")

    count += 1
    '''