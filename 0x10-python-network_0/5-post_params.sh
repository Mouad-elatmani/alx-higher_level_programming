#!/bin/bash
# A header variable X-School-User-Id must be sent with the value 98
curl -sL -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
