#!/bin/bash

# activate venv

# Start the challenges
echo "Starting login challenge";
cd login && gnome-terminal -- php -S 192.168.102.69:8001
cd ..


echo "Starting MIAM MIAM challenge"
cd miam && gnome-terminal -- php -S 192.168.102.69:8003
cd ..

echo "Starting message-me challenge"
cd message-me && gnome-terminal -- serve -s build -l 8004
cd API && gnome-terminal -- node api.js
cd ../..

echo "Starting Upload challenge"
cd Upload && gnome-terminal -- docker compose up
cd ..


echo "all challenges started"
