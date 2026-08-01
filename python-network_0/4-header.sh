#!/bin/bash
# Sends a GET request with a custom header and displays the response body
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
