import gspread
from google.oauth2.service_account import Credentials

# Replace with your JSON key file path
service_account_file = 'client_auth.json'

# Use a scope that only grants read access to Google 

scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly',
          'https://www.googleapis.com/auth/drive']


# Use service account credentials for 
my_credentials = Credentials.from_service_account_file(filename=service_account_file, scopes=scopes)
# gspread.use_service_account_file(service_account_file, scopes=scopes)
my_client = gspread.authorize(my_credentials)
# Open the Google Sheet by its title or URL
# my_client.open_by_key('1Ch1RQSdFRA9DKW65blywOPyHnR2G8SPsVPFzo-OPvWI')
gc = my_client.open_by_key('1H8MV-JCC7OfPY1jt18mISAyYhk7lBI4-GqzvKZCAxkU')

# Choose the worksheet you want to read (optional)
worksheet = gc.sheet1  # You can access a specific sheet by its title or index

# Get all values from the worksheet as a list of lists
all_values = worksheet.get_all_values()

# Print the contents (as you prefer)
# print(all_values[:11])  # Print the entire list of lists
# To access specific cells, use indexing: print(all_values[row][column])
# my_dict = dict(all_values[:11])
# ... (process the data as needed)
all_values[0][0] = 'letter'
number = [all_values[0][i] for i in range(13)]
alpha = [all_values[i][0] for i in range(9)]
value = all_values[:][:9]
# value = dict(value)
# my_dict = {all_values[0][i]:all_values[:][i] for i in range(13)}
sequence = [(all_values[0][0], all_values[0][:9])]
# print(number)
# print(alpha)


# for i in range(12):

# for i in range(11):
#     for j in range(8):
#         if i == j:
#             key.append(all_values[i][j])

# print(key)