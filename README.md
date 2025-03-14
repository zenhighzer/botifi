# botifi
Discord-Bot for setting password in unifi-wlan-settings (in my case unifi is running on a unifi ucg max)

Invite your own bot to your discord server and let him set the wifi-password in a unifi-environmen. 
This is useful to allow other people like my wife to set the kid´s wifi-password without accessing unifi-controller directly :)
The python-script will check the provided password for complexicity and compares to well-known-passwords in a dictionary, if checks are good the bot will update the wifi´s passwort 

![grafik](https://github.com/user-attachments/assets/388b4844-890d-4260-81ae-a3094d9a06a2)

![grafik](https://github.com/user-attachments/assets/1d2e34b1-ec9b-47fb-9181-f351dd89496a)

![grafik](https://github.com/user-attachments/assets/c56cdd97-1e0b-4990-aa4d-65c03857fac9)

![grafik](https://github.com/user-attachments/assets/d6797643-2ea7-4ba4-9158-5e8dbd4013ef)




For creating a discord bot account/token, see https://discordpy.readthedocs.io/en/stable/discord.html
For creating a unifi api token, take a look into unifi-documentation or ask the unifi-bot :-)

Just grab this project and build a container: 
docker build -t botifi . 

start container with helper-script "bash start_container.sh" 
this script will ask for the discord-bot´s token, the unifi-api-token and the api-url to the specific wlan/ssid

