import streamlit as st


def main():
    st.title("Welcome to My First Streamlit App")
    st.write("This is a simple example of a Streamlit app.")
    st.write("Here, you can see how to display text, images, and interactive widgets.")

    # Adding a slider
    age = st.slider("What is your age?", 1, 100, 25)

    # Adding a text input
    name = st.text_input("What is your name?", "John Doe")

    # Adding a selectbox
    occupation = st.selectbox("What is your occupation?", ["Engineer", "Data Scientist", "Teacher", "Other"])

    # Showing the selected values
    st.write(f"Your age is: {age}")
    st.write(f"Your name is: {name}")
    st.write(f"Your occupation is: {occupation}")

if __name__ == "__main__":
    main()