from pymongo import MongoClient
import logging
import json
import pandas as pd
from Insurance.logger import logging
from Insurance.exception import InsuranceException
import sys

if __name__ == '__main__':
#making connection to the monogodb database through url
    try:
        logging.info((f"Making connectivity to the mongodbdatabase online version"))
        client = MongoClient("mongodb+srv://rohit28:sharma@rohitcluster1.jyclaup.mongodb.net/?retryWrites=true&w=majority")
        logging.info((f"connection successful"))
    except Exception as e:
        raise InsuranceException(e, sys)

    #creating database in mongodb
    try:
        logging.info((f"creating database"))
        db = client['Project']
        logging.info((f"database created"))
    except Exception as e:
        raise InsuranceException(e, sys)

    # Collection name 
    try:
        logging.info((f"creating the collection"))
        collection = db['insurance_prediction']
        logging.info((f"collection created"))
    except Exception as e:
        raise InsuranceException(e, sys)

    # Reading the data from the system insurance.csv
    df = pd.read_csv("insurance.csv")
    print(f"rows and columns: {df.shape}")

    # Converting dataframe into json so that it can be dumped into mongodb
    df.reset_index(drop=True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #dumping the datainto the mongodb database
    try:
        logging.info((f"dumping datainto mongodb database"))
        collection.insert_many(json_record)
        logging.info((f"data dumped"))
    except Exception as e:
        raise InsuranceException(e, sys)

    # Verify the data insertion:
    result = collection.find()
    for document in result:
        print(document)

    #retrieving the dumped data from the mongodb database as Dataframe
    try:
        logging.info((f"Retrieving the data from mongodb database"))
        data = collection.find({}, {'_id': 0})
        logging.info((f"Data Retrieved"))
    except Exception as e:
        raise InsuranceException(e, sys)

    #now save the retrieved data as csv file 
    try:
        # Create DataFrame
        logging.info((f"Saving the data as dataframe"))
        df = pd.DataFrame(data)
        df.to_csv('data.csv', index=False)
        logging.info((f"Data saved"))
    except Exception as e:
        raise InsuranceException(e, sys)