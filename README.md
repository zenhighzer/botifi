# botifi
Discord-Bot for setting password in unifi-wlan-settings (in my case unifi is running on a unifi ucg max)

- Invite your own bot to your discord server and let him set the wifi-password in a unifi-environment.
- This is useful to allow other people like my wife to set the kid´s wifi-password without accessing unifi-controller directly :)
- The python-script will check the provided password for complexicity (length, upper/lowercase, numbers and special chars, umlauts) and finally compares to well-known-passwords in a (german) dictionary. 
- if password-check is satisfied, the bot will update the wifi´s password.

![grafik](https://github.com/user-attachments/assets/388b4844-890d-4260-81ae-a3094d9a06a2)

![grafik](https://github.com/user-attachments/assets/1d2e34b1-ec9b-47fb-9181-f351dd89496a)

![grafik](https://github.com/user-attachments/assets/c56cdd97-1e0b-4990-aa4d-65c03857fac9)

![grafik](https://github.com/user-attachments/assets/d6797643-2ea7-4ba4-9158-5e8dbd4013ef)


- For creating a discord bot account/token, see https://discordpy.readthedocs.io/en/stable/discord.html
- !PLEASE you better secure your Discord-Channels properly! Only allow humans you trust and love to talk to the channel where your bot lives in. You dont want others to mess around with your wifi-password!
- For creating a unifi api token, take a look into unifi-documentation or ask the unifi-bot :-)
- in my case i use the unifi-default-self-signed cert and the bot is talking to the Unifi-API via "unifi.local", which points to my UCG on IP 192.168.x.y (Replace the IP in helper-script start_container.sh at "--add-host=192.168.x.y")
- You should replace the cert (unifi-local.crt) with yours.

In a nutshell: 
Just grab this project make some modifications, build and start a container: 
- replace unifi-local.crt with your ucg´s self-signed cert. 
- replace the IP of the UCG in "start_container.sh -> "--add-host=192.168.x.y")
- docker build -t botifi . 
- start container with helper-script "bash start_container.sh" 

This helper-script will ask for the discord-bot´s token, the unifi-api-token and the api-url to the specific wlan/ssid. 
![grafik](https://github.com/user-attachments/assets/cf6c5cdc-1577-4fa5-ae80-e0a4aedbcc3d)
