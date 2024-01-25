#!/bin/bash
# send a custom header
curl -s -X GET --header "X-School-User-Id: 98" "$1"
