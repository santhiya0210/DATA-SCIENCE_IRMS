import pandas as pd
import requests
import json

# Read college location file which is in csv format. 
df = pd.read_csv("data.csv")
# print(df)

#API Call and get the latitude & longitude values
for i,row in df.iterrows():
    apiAddress = str(df.at[i,'Name']) + ',' + str(df.at[i,'State']) + ',' + str(df.at[i,'Country'])
    print(apiAddress)
    
    parameters = {
        "key" : "cjsjyP4PHwGm9qzgSnLlqPmB7J9o6VqZ",
        "location" : apiAddress
    }
    
    response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params = parameters)
    # print(response.text)
    data = json.loads(response.text)['results']

    lat = data[0]['locations'][0]['latLng']['lat']
    lng = data[0]['locations'][0]['latLng']['lng']
    #print(lat , lng)
    
    df.at[i,'lat'] = lat
    df.at[i,'lng'] = lng
       
# #Saving the data to csv with geodata
df.to_csv('geodata.csv')