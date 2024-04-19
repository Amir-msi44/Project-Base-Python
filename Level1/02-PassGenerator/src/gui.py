import streamlit as st
from Main import PinGenerator, RandomPassGenerator, MemorablePassGenerator


st.title(':zap: Password Generator')
option = st.radio(
    'Select a password generator',
    ("Pin Code", 'Random', 'Memorable')
)

if option == 'Pin Code':
    length = st.slider('Select the lenght of the Pin Code', 8, 32)
    generator = PinGenerator(length)

elif option == 'Random':
    length = st.slider('Select the lenght of the Pin Code', 8, 32)
    include_numbers = st.toggle('Include Numbers')
    include_symbols = st.toggle('Include Symbols')
    generator = RandomPassGenerator(length, include_numbers, include_symbols)

elif option == 'Memorable':
    num_of_words = st.slider('Select the number of Words', 2, 10)
    capitalize = st.toggle('Capital')
    separator_type = st.text_input('Separator', value='-')
    generator = MemorablePassGenerator(num_of_words, capitalize, separator_type)
password = generator.generate()
st.write(fr"Your Password is: ``` {password} ``` ")