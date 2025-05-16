#!/bin/bash

if find test/ -name "*.py" | grep -q .; then
    pytest test/ -v
else
    echo "No tests!"
    exit 0
fi