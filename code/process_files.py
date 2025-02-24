'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''
import streamlit as st 
from io import StringIO 
import packaging
import json

st.title("process file")
count = 0
total_lines = 0
st.title("process file")

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