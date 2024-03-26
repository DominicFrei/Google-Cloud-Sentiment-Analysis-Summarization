#!/bin/bash

query="This was an amazing evening. Food, service, interior great."

invoke_url=https://qz3pgn7nd5.execute-api.us-east-1.amazonaws.com/PROD/sentiment

curl -X POST -H "Content-Type: application/json" -d "{\"query\":\"$query\"}" "$invoke_url"

echo ""
