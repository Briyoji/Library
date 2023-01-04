import requests

# Make a GET request
response = requests.get('https://library.plaksha.edu.in/cgi-bin/koha/opac-detail.pl?biblionumber=9990')

# Check the status code
print(response.status_code)

if response.status_code == 404:
    print('Page not found')
