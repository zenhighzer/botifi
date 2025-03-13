#!/bin/bash

read -s -p "Discord BOT Token: " DISCORD_BOT_TOKEN
echo
read -s -p "UNIFI API Key: " UNIFI_API_KEY
echo
read -s -p "UNIFI API URL / WLAN, i.e: https://192.168.1.1/proxy/network/api/s/default/rest/wlanconf/76sdf04sdf4234fsdsf233ed: " UNIFI_API_URL
echo

export DISCORD_BOT_TOKEN
export UNIFI_API_KEY
export UNIFI_API_URL

docker run -e DISCORD_BOT_TOKEN=$DISCORD_BOT_TOKEN -e UNIFI_API_KEY=$UNIFI_API_KEY -e UNIFI_API_URL=$UNIFI_API_URL --restart always --name botifi -dit botifi

export DISCORD_BOT_TOKEN=null
export UNIFI_API_KEY=null
export UNIFI_API_URL=null
