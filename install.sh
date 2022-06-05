#!/bin/bash

echo "Downloading ngrok..."
sudo apt install gnome-terminal 
pip install colorama
pip3 install colorama
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
mv ngrok-v3-stable-linux-amd64.tgz1 ngrok.tgz
mv ngrok-v3-stable-linux-amd64.tgz ngrok.tgz
sudo tar xvzf ngrok.tgz -C /usr/local/bin
echo "Ngrok downloaded and installed!!"