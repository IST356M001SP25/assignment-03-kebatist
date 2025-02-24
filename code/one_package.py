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
'''
def main():
    st.title("Package Data Input")
    package_data = st.text_area("Enter package data string:")

    if package_data:

        package_info = parse_package_data(package_data)

        # Display the package info
        st.subheader("Package Info")
        st.write(package_info)

        # Calculate the total package size
        total_size = sum(item['size'] for item in package_info)
        st.subheader("Total Package Size")
        st.write(total_size)

if __name__ == "__main__":
    main()

def parse_package_data(data):
    # This is a placeholder function. Replace with actual parsing logic.
    # Assuming the data is a list of dictionaries with 'size' as one of the keys.
    return [
        {"name": "item1", "size": 10},
        {"name": "item2", "size": 20},
        {"name": "item3", "size": 30},
    ]
def parse_package_data(data):
    # This is a placeholder function. Replace with actual parsing logic.
    # Assuming the data is a list of dictionaries with 'size' as one of the keys.
    return [
        {"name": "item1", "size": 10},
        {"name": "item2", "size": 20},
        {"name": "item3", "size": 30},
    ]
'''