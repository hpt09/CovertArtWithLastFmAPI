import requests
#
# Pip install the client:
# pip install clarifai
#

# The package will be accessible by importing clarifai:

from clarifai.rest import ClarifaiApp
import csv

# The client takes the `API_KEY` you created in your Clarifai
# account. You can set these variables in your environment as:

# - `CLARIFAI_API_KEY`

# Instantiate a new Clarifai app by passing in your API key.
app = ClarifaiApp(api_key='4fcb124813d44f17b3d4f820382c9445')

# Choose one of the public models.
model = app.models.get('color')

response = model.predict_by_filename('/CoverArt/2.png');
print(response['outputs'][0]['data']['colors'][0]['w3c']['name']);
print(response['outputs'][0]['data']['colors'][1]['w3c']['name']);
print(response['outputs'][0]['data']['colors'][2]['w3c']['name']);

filename = '/home/nikhil/Downloads/Dataset_FINAL/Dataset.csv'

with open("Dataset.csv", "wb") as csv_file:
        writer = csv.writer(csv_file)
        for x in range(2,423):
            print(x);
            response = model.predict_by_filename('/CoverArt/2.png')
            A = response['outputs'][0]['data']['colors'][0]['w3c']['name']
            B = response['outputs'][0]['data']['colors'][1]['w3c']['name']
            try:
                C = response['outputs'][0]['data']['colors'][2]['w3c']['name']
            except IndexError:
                C = 'null'
            writer.writerow([A,B,C])
