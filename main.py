import streamlit as st

from utils import connect_to_google_sheets
from view_jobs import view_jobs_page
from add_jobs import add_jobs_page


def main():
    st.sidebar.title('Navigation')
    app_mode = st.sidebar.radio('Go to', ['Add Jobs', 'View Jobs'])

    if app_mode == 'Add Jobs':
        add_jobs_page()
    elif app_mode == 'View Jobs':
        view_jobs_page()

if __name__ == '__main__':
    main()

