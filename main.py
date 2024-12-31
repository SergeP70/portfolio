import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Serge Pille")
    content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam molestie velit velit. 
    Vivamus consequat in urna ut convallis. Nunc non erat ultrices, lacinia erat eget, maximus tortor. Pellentesque maximus vitae enim et volutpat. 
    Donec euismod non felis at lobortis. Donec eget hendrerit massa. In hac habitasse platea dictumst. Vivamus malesuada dui vehicula faucibus ultricies. 
    Quisque et tellus cursus risus blandit vehicula faucibus sed erat. Duis non mauris massa. 
    Curabitur ornare erat eu lectus finibus, vitae suscipit quam fringilla."""
    st.info(content)