import streamlit as st
import csv

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=450)

with col2:
    st.title("Serge Pille")
    content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam molestie velit velit. 
    Vivamus consequat in urna ut convallis. Nunc non erat ultrices, lacinia erat eget, maximus tortor. Pellentesque maximus vitae enim et volutpat. 
    Donec euismod non felis at lobortis. Donec eget hendrerit massa. In hac habitasse platea dictumst. Vivamus malesuada dui vehicula faucibus ultricies. 
    Quisque et tellus cursus risus blandit vehicula faucibus sed erat. Duis non mauris massa. 
    Curabitur ornare erat eu lectus finibus, vitae suscipit quam fringilla."""
    st.info(content)

content2= """ "Below you can find some of the apps I have built in Python. Feel free to contact me!"""
st.write(content2)

cols = st.columns(2)
cols_index = 0
with open("data.csv", "r") as file:
    csv_reader = csv.DictReader(file, delimiter=';')
    for row in csv_reader:
        with cols[cols_index]:
            print(row['title'])
            img_url = "images/" + row['image']
            st.subheader(row['title'])
            st.write(row['description'])
            st.image(img_url, width=200)
            st.write(f"[Source Code]({row['url']})")
            cols_index += 1
            if cols_index >= len(cols):
                cols_index = 0

