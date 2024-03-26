import json

import requests


def test_data_api():
    url = "https://us-east-1.aws.data.mongodb-api.com/app/application-0-lmzbw/endpoint/data/v1/action/findOne"

    payload = json.dumps(
        {
            "collection": "restaurants",
            "database": "sample_restaurants",
            "dataSource": "mongodb-atlas",
            "projection": {"_id": 1},
        }
    )
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Request-Headers": "*",
        # "api-key": "1vx4uecIgF94b7JWPtO2Vq1qk29MltDITaeYIDL1Ssyts44RUcbuSF936BQI1K5y",
        "Accept": "application/ejson",
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


#
#
# {"name": "Dominic"}
# DoNotDeleteAwsSummitDemo
# 1vx4uecIgF94b7JWPtO2Vq1qk29MltDITaeYIDL1Ssyts44RUcbuSF936BQI1K5y
#
#
#
# curl --location --request POST 'https://us-east-1.aws.data.mongodb-api.com/app/data-xbrmk/endpoint/data/v1/action/findOne' \
# --header 'Content-Type: application/json' \
# --header 'Access-Control-Request-Headers: *' \
# --header 'api-key: 1vx4uecIgF94b7JWPtO2Vq1qk29MltDITaeYIDL1Ssyts44RUcbuSF936BQI1K5y' \
# --header 'Accept: application/ejson' \
# --data-raw '{
# "collection":"<COLLECTION_NAME>",
#   "database":"<DATABASE_NAME>",
#   "dataSource":"Cluster0",
#   "projection": {"_id": 1}
# }'
#
#
