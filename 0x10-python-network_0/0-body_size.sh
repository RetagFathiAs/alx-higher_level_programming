#!/bin/bash
#send a GET stdout
curl -sI "$1" | grep -i "Content-Length" | cut -d ":" -f 2
