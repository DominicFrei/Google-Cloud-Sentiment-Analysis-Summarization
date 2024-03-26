#!/bin/bash

query="This was an amazing evening. Food, service, interior great."
encoded_query=$(echo -n "$query" | jq -sRr @uri)

invoke_url="https://qz3pgn7nd5.execute-api.us-east-1.amazonaws.com/PROD/sentiment?query=$encoded_query"
echo "$invoke_url"

curl -X GET "$invoke_url"
