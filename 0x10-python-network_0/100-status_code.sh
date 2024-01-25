#!/bin/bash
# displa onse
curl -o /dev/null -sIw "%{http_code}" "$1"
