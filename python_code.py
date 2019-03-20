## Python code for reading, parsing, and uploading data to Thingspeak.com

import requests
import serial
import time

# Read and record the data
data =[] # initialize and empty list to store the data
while True:
    ser = serial.Serial('COM4', 9600)    # set up the serial connection with arduino
    time.sleep(1)
    
    b = ser.readline() # read a byte string line from the Arduino's serial output
    b_string = b.decode() # decode byte string into regular Python string
    string = b_string.rstrip() # remove \n and \r from the string
    flt = float(string) # convert the string to a float
    
    #https://api.thingspeak.com/update?api_key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&field1=0
    base_url = "https://api.thingspeak.com/update?api_key="
    api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    mid_url_1 ='&field1='     # field number, if only one field use 1
    url = base_url + api_key + mid_url_1 + string   # data_point
    #print(url)    # prints url to screen for feedback on when/what data is uploaded
    r = requests.get(url)    # upload data point to thingspeak channel
    time.sleep(15)    # delays loop for thingspeak upload rate
   
    ser.close()    # closes the serial connection with arduino

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Python code for reading, parsing, and plotting data from Thingspeak

# import
import time
import numpy as np
import requests
import json
import matplotlib.pyplot as plt
%matplotlib inline

# ask user for number of data points
results_num = input('How many data points?:')

## Read data stored on ThingSpeak.com
# https://api.thingspeak.com/channels/714132/fields/1.json?api_key=XXXXXXXXXXXXXXXXXXXXXXXXXX&results=2
base_url = 'https://api.thingspeak.com/channels/'
channel_num = '714132'
mid_url = '/fields/'
field_num = '1'
next_url = '.json?'
# api_url = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
end_url = 'results='
results_num        #number of datapoints, saved as a string

url = base_url + channel_num + mid_url + field_num + next_url + end_url + results_num
url


#use the requests library to pull down the data from thingspeak into a variable
r = requests.get(url)
json_data = r.json()
#print(json_data)


# Test Code

#print(json_data['feeds'][0]['field1'])
#feeds = json_data["feeds"]

# iterate over the list:
#for feed in feeds:
    # get the value for the "field1" key
    #print (feed["field1"])

# Store data into lists data, time

feeds = json_data["feeds"]
data = []
time = []
for feed in feeds:
    # get the value for the "field1" key
    data.append(feed["field1"])
    time.append(feed["created_at"])
    #print (feed["field1"])
    #print(feed["created_at"])
    
    
# Read Data and build graph
# plot the data
fig, ax = plt.subplots()

ax.plot(time, data,'r',linewidth=0.8)
ax.set_xlabel('Time')
ax.set_xticklabels(time, rotation=-45, ha='left')
ax.set_ylabel('PH from Sensor')
ax.invert_yaxis()
ax.set_title('Ph Sensor from fish tank')

plt.tight_layout()
#save plot image
plt.savefig('phsensor.png', dpi=72)
plt.show()
