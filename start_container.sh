#!/bin/bash

read -s -p "Discord BOT Token: " DISCORD_BOT_TOKEN
echo
read -s -p "UNIFI API Key: " UNIFI_API_KEY
echo
read -s -p "UNIFI API URL, like https://unifi.local/proxy/network/api/s/default/rest/wlanconf/234lkjl234aasda: " UNIFI_API_URL
echo

export DISCORD_BOT_TOKEN
export UNIFI_API_KEY
export UNIFI_API_URL

docker run --add-host unifi.local:192.168.100.100 -e DISCORD_BOT_TOKEN=$DISCORD_BOT_TOKEN -e UNIFI_API_KEY=$UNIFI_API_KEY -e UNIFI_API_URL=$UNIFI_API_URL --restart always --name botifi -dit botifi

export DISCORD_BOT_TOKEN=null
export UNIFI_API_KEY=null
export UNIFI_API_URL=null
