import unittest
from unittest.mock import patch
import streamlit as st
import pandas as pd
from view_jobs import view_jobs_page
from add_jobs import add_jobs_page
from utils import connect_to_google_sheets


class TestMainApp(unittest.TestCase):

    def setUp(self):
        # Start patching the connect_to_google_sheets function
        self.sheet_mock = patch('utils.connect_to_google_sheets').start()

    def tearDown(self):
        # Stop all patches
        patch.stopall()

    @patch.object(st, 'button', return_value=True)
    @patch.object(st, 'success')
    def test_add_job_success(self, mock_success, mock_button):
        # Mock user inputs and function calls
        with patch.object(st, 'date_input', return_value=pd.Timestamp('2024-03-25')):
            with patch.object(st, 'text_input', return_value='Software Engineer'):
                with patch.object(st, 'selectbox', return_value='Applied'):
                    with patch.object(st, 'file_uploader', return_value=None):
                        add_jobs_page()
                        # Check if success message is displayed
                        mock_success.assert_called_with('Job added successfully!')

    @patch.object(st, 'button', return_value=True)
    @patch.object(st, 'success')
    def test_add_job_failure(self, mock_success, mock_button):
        # Mock user inputs and function calls
        with patch.object(st, 'date_input', return_value=pd.Timestamp('2024-03-25')):
            with patch.object(st, 'text_input', return_value=' '):  # Blank job title
                with patch.object(st, 'selectbox', return_value='Applied'):
                    with patch.object(st, 'file_uploader', return_value=None):
                        add_jobs_page()
                        # Check if success message is not called
                        mock_success.assert_not_called()

    @patch.object(st, 'button', return_value=True)
    @patch.object(st, 'checkbox', return_value=True)
    def test_delete_job_success(self, mock_checkbox, mock_button):
        # Mock DataFrame with one job record
        df = pd.DataFrame({'ID': [1], 'Date': ['2024-03-25'], 'Title': ['Software Engineer'], 'State': ['Applied']})
        self.sheet_mock.return_value.get_all_records.return_value = df.to_dict('records')
        # Simulate user interaction
        with patch.object(st, 'selectbox', return_value=1):
            with patch.object(st, 'button', return_value=True):
                view_jobs_page()
                # Check if checkbox is called
                mock_checkbox.assert_called()

    @patch.object(st, 'button', return_value=True)
    @patch.object(st, 'checkbox', return_value=True)
    def test_delete_job_failure(self, mock_checkbox, mock_button):
        # Mock DataFrame with no job records
        df = pd.DataFrame(columns=['ID', 'Date', 'Title', 'State', 'Note'])
        self.sheet_mock.return_value.get_all_records.return_value = df.to_dict('records')
        # Simulate user interaction
        view_jobs_page()
        # Ensure that the checkbox function is called
        mock_checkbox.assert_called_once()


if __name__ == '__main__':
    unittest.main()
