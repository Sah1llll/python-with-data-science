#streamlit
import streamlit as st

st.title("simple calculator")
# st.write("this is a simple calculator app using streamlit.")
st.markdown(" this is a simple calculator app using streamlit ")
c1, c2 = st.columns(2)
first_num = c1.number_input("Enter first number", value=0, step=1)
second_num = c2.number_input("Enter second number", value=0, step=1)
option = ["add", "substract", "multiply", "divide", "exponemt"]
choice = st.radio("select operation", option)
button = st.button("calculate")
result = 0 

if button: 
    if choice == 'add':
        result = first_num+second_num
    elif choice ==  "substract":
        result = first_num-second_num
    elif choice == "multifly":
        result = first_num*second_num
    elif choice == "divide":
        if second_num != 0:
            result = first_num/second_num
        else:
            st.error("cannot divided by zero")
    elif choice == "exponent":
        result = first_num ** second_num

st.success(f"the result is: {result}")
