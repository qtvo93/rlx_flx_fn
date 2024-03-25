import streamlit as st
from utils import connect_to_google_sheets
import pandas as pd
import gspread
import time


def view_jobs_page() -> None:
    """
    The view jobs page of the App.
    """
    
    st.title('View Jobs')
    sheet = connect_to_google_sheets()
    existing_data = sheet.get_all_records()

    if existing_data:
        st.write('Job Data:')
        df = pd.DataFrame(existing_data)
        st.dataframe(df)
        # Option to delete a job
        st.subheader('Delete Job')
        job_to_delete = st.selectbox('Select Job ID to Delete', df['ID'].tolist())
        job_name = df[df['ID'] == job_to_delete]['Title'].values[0] # Get job name

        if st.checkbox('🗑️ Delete'):
            # Get confirmation 
            st.warning(f'You are going to delete job ID: {job_to_delete} - name: {job_name}, action cannot be undone. Please confirm.')
            if st.button('Confirm'):
                # Convert job_to_delete to integer as sheet.delete_rows() requires integer indices
                job_to_delete = int(job_to_delete)
                sheet.delete_rows(job_to_delete)  # Delete the selected row
                st.success('Job deleted successfully!')
                time.sleep(1.25)
                # Refresh the page to display updated data
                st.cache_data.clear()
                st.cache_resource.clear()
                st.rerun()

    else:
        st.write('No jobs found.')


if __name__ == '__main__':
    view_jobs_page()
