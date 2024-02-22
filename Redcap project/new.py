import gspread
from oauth2client.service_account import ServiceAccountCredentials
# Replace with your JSON key file path
service_account_file = 'client_secret.json'

# Use a scope that only grants read access to Google 
scopes = ''
# # scopes = ['https://spreadsheets.google.com/feeds',
#           'https://www.googleapis.com/auth/spreadsheets',
#           'https://www.googleapis.com/auth/drives']

# Use service account credentials for 
my_credentials = ServiceAccountCredentials.from_json_keyfile_name(filename='client_secret.json')
# gspread.use_service_account_file(service_account_file, scopes=scopes)
my_client = gspread.authorize(my_credentials)
# Open the Google Sheet by its title or URL
gc = my_client.open('https://docs.google.com/spreadsheets/d/1-J_R3OmEZUa7J8lpOF8aA41eJDVbfL5u565RQ6NyOLU/edit')

# Choose the worksheet you want to read (optional)
worksheet = gc.sheet1  # You can access a specific sheet by its title or index

# Get all values from the worksheet as a list of lists
all_values = worksheet.get_all_values()

# Print the contents (as you prefer)
print(all_values)  # Print the entire list of lists
# To access specific cells, use indexing: print(all_values[row][column])

# ... (process the data as needed)
