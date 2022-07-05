from curses.ascii import isdigit
import os
import re
from config import client
from bson.json_util import dumps
from flask import request, jsonify
from importlib.machinery import SourceFileLoader
from flask import Flask

# Import the helpers module
helper_module = SourceFileLoader('*', './api/helpers.py').load_module()

api = Flask(__name__)

# Select the database
db = client['lamz-net']
# Select the collection
collection_artwork = db['artwork']
collection_scrapbook = db['scrapbook']

@api.route("/api/v1/art", methods=['GET'])
def fetch_art():
    try:
        
        # process query string into parts
        # get results for 'search' query and/or 'tags' query
        
        #if good results return json 'dumps' of them else return 404 code

        # If dictionary is empty
        
        # # Call the function to get the query params
        # query_params = helper_module.parse_url(request.url)
        # # Check if dictionary is not empty
        # if query_params:

        #     # Try to convert the value to int
        #     query = {k: int(v[0]) if v[0].isdigit() else None for k, v in query_params.items()}

        #     # Check if there are any records
        #     if collection_artwork.count_documents(query) > 0:
        #         # Fetch all the record(s)
        #         records_fetched = collection_artwork.find(query)
                
        #         # Prepare the response
        #         return dumps(records_fetched)
        #     else:
        #         # No records are found
        #         return "", 404

        # If dictionary is empty
        else:
            # return bad request code
            return "No request was made.", 400
    except Exception as e:
        # relay python exception
        return f"Something fatal occured within the server. {os.linesep}{os.linesep}{e}", 500