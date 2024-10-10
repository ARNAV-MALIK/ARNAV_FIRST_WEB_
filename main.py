import streamlit as st
st.title("WELCOME! TO ARNAV'S WEBSITE !")
st.header("ARNAV'S GRADE CALCULATOR CODE")
st.code ("""
a = int(input("ENTER THE MARKS : "))
if (a >= 90 ):
     print("A1")
elif (a >= 80 and a<= 89):
    print("A2")
elif (a >= 70 and a<=79):
    print("B1")
elif (a >= 60 and a<=69):
    print("B2")
else :
    print("D")
""")

