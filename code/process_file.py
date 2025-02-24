'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''
import streamlit as st 
from io import StringIO 
import packaging
import json

def process_file(file):
    # Read the file
    file.seek(0)
    text = StringIO(file.read().decode('utf-8'))
    # Parse the file
    packages = {}
    for line in text:
        package, size = line.split()
        if package in packages:
            packages[package] += int(size)
        else:
            packages[package] = int(size)
    # Output the parsed package and total package size
    for package, size in packages.items():
        st.write(f'Package: {package}, Size: {size}')

def main():
    st.title('Package Information')
    file = st.file_uploader('Upload a file', type='txt')
    if file:
        process_file(file)