import streamlit as st
from mainnew import Student

st.set_page_config(page_title="Student Management System")

st.title("🎓 Student Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    ["Create Account", "Fetch Details", "Update Details", "Delete Account"]
)

# CREATE
if menu == "Create Account":
    st.subheader("Create New Account")

    name = st.text_input("Name")
    branch = st.text_input("Branch")
    year = st.text_input("Academic Year")
    roll = st.text_input("Roll Number")
    email = st.text_input("Email ID")

    if st.button("Create"):
        student = Student.create(name, branch, year, roll, email)
        st.success("Account created successfully 🎉")
        st.code(f"Registration Number: {student['registration_number']}")

# FETCH
elif menu == "Fetch Details":
    st.subheader("Fetch Student Details")
    reg = st.text_input("Registration Number")

    if st.button("Fetch"):
        student = Student.find_by_reg(reg)
        if student:
            st.json(student)
        else:
            st.error("Student not found")

# UPDATE
elif menu == "Update Details":
    st.subheader("Update Student Details")
    reg = st.text_input("Registration Number")

    field = st.selectbox(
        "Select Field",
        ["name", "roll_no", "email_id"]
    )
    value = st.text_input("New Value")

    if st.button("Update"):
        success = Student.update(reg, field, value)
        if success:
            st.success("Details updated")
        else:
            st.error("Student not found")

# DELETE
elif menu == "Delete Account":
    st.subheader("Delete Student Account")
    reg = st.text_input("Registration Number")

    if st.button("Delete"):
        success = Student.delete(reg)
        if success:
            st.success("Account deleted")
        else:
            st.error("Student not found")
