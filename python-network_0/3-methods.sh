#!/bin/bash
# Displays all the HTTP methods the server accepts for a URL
curl -s -X OPTIONS -i "$1" | grep -i "^Allow:" | cut -d " " -f 2- | tr -d "\r"
