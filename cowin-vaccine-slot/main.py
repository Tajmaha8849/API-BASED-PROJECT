"""

@author:Shubham Prajapati
Date:02 Feb 2024

API for Checking covid vaccination facility available nearby.
This will help a lot to get data easily whether slot are available or not on your input date and pincode.

"""

import requests

PINCODE="0"
while(len(PINCODE)!=6):
    PINCODE=input("Enter the Pincode:")
    if(len(PINCODE))<6:
        print("Enter a valid pincode.")
    elif len(PINCODE)>6:
        print("Length of a pincode is greater .")
REQ_DATE=input("Enter the date in the format dd-mm-yyyy)=>")
request_link = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={PINCODE}&date={REQ_DATE}"
header = {'User-Agent': 'Chrome/84.0.4147.105 Safari/537.36'}

response = requests.get(request_link, headers = header)
raw_JSON = response.json()
print(raw_JSON)

Total_centers=len(raw_JSON['centers'])

print()
print("                *>>>>>>  RESULTS     <<<<<<*                          ")
print("----------------------------------------------------------------------")
print(f"Date:{REQ_DATE} | Pincode:{PINCODE}")


if Total_centers!=0:
    print(f"Total centers in your area is:{Total_centers}")
else:
    print(f"Unfortunately !! Seems like no center in this area/ Kindly re-check the pincode.")

print("-------------------------------------------------------------------------")
print()


for cent in range(Total_centers):
    print()
    print(f"[{cent+1}] Center Name:",raw_JSON['centers'][cent]['name'])
    fee_val=raw_JSON['centers'][cent]['fee_type']
    print("----------------------------------------------------------------------")
    print()
    print()
    print("Date VaccineType   VaccineFee   Minimum Age   Available slot")
    print()
    print()
    print("----------------------------------------------------------------------")
    this_session=raw_JSON['centers'][cent]['sessions']
