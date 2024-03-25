import streamlit as st
from utils import connect_to_google_sheets
import time


def add_jobs_page() -> None:
    """
    The add jobs page of the App.
    """

    st.title('Job Application Tracker')

    # Date, Job Title, State, Note, Resume
    date = st.date_input('Date')
    job_title = st.text_input('Job Title')
    state = st.selectbox('State', ['Applied', 'Screened', 'Shortlisted', 'Interview in Progress', 'Offered', 'Other'])
    # If state is 'Other', allow user to enter a custom state
    if state == 'Other':
        other_state = st.text_input('Other State')

    note = st.text_input('Note (Optional)')

    # Upload resume (PDF or DOCX)
    uploaded_resume = st.file_uploader('Upload Resume', type=['pdf', 'docx'])

    # Button action to add job
    if st.button('Add'):
        if job_title.strip() == '':
            st.error('Job title cannot be blank!')
        else:
            # convert date to string
            date_str = date.strftime('%Y-%m-%d')
            # Store data in Google Sheets
            sheet = connect_to_google_sheets()

            # allow user to enter a custom state
            if state == 'Other':
                state = other_state

            # Get the next ID
            existing_data = sheet.get_all_records()
            next_id = max(int(row["ID"]) for row in existing_data) + 1 if existing_data else 1

            # Add the job to the Google Sheet
            sheet.append_row([next_id, date_str, job_title, state, note])
            # Display success message
            st.success('Job added successfully!')
            time.sleep(1.25)
            st.rerun()


        # TODO: Store resume

if __name__ == '__main__':
    add_jobs_page()