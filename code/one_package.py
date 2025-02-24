'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''
import streamlit as st
import packaging 

st.title("process one pack")
'''
MEOWOOWOWOWOW 
'''
pack = st.text_input("enter pack data:")
if pack:
    parsed_pack = packaging.parse_packaging(pack)
    total = packaging.calc_total_units(parsed_pack)
    unit = packaging.get_unit(parsed_pack)
    st.text(parsed_pack)
    for item in parsed_pack:
        name = list(item.keys())[0]
        size = list(item.values())[0]
        st.info(f"{name} ➡️ {size}")
    st.success(f"Total 📦 Size: {total} {unit}")
