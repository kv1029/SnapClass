import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen
from src.ui.base_layout import style_layout_base,style_background_home


def main():
    if "login_type" not in st.session_state:
        st.session_state["login_type"] = "home"

    style_background_home()
    style_layout_base()
    match st.session_state["login_type"]:
        case "teacher":
            teacher_screen()

        case "student":
            student_screen()

        case "home":
            home_screen()



main()