import gspread
from oauth2client.service_account import ServiceAccountCredentials


def connect_to_google_sheets(
    spreadsheets_name: str = "test_app", 
) -> gspread.worksheet.Worksheet :
    """
    Connect to Google Sheets using the credentials.json file.

    Args:
        spreadsheets_name (str): The link to the Google Sheets document.

    Returns:
        gspread.worksheet.Worksheet: The Google Sheets worksheet.
    """

    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    gc = gspread.authorize(credentials)

    return gc.open(spreadsheets_name).sheet1

if __name__ == '__main__':
    connect_to_google_sheets()