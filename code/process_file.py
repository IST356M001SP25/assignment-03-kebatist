'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''
import streamlit as st 
from io import StringIO 
import packaging
import json

st.title("process file")

file = st.file_uploader("upload file")
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