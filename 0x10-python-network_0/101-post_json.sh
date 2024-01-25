#!/bin/bash
# Send JSON  args
curl -d "$(cat "$2")" -s -X POST --header "Content-Type: application/json" "$1"
