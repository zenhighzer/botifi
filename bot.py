import discord
import re
import requests
import os
import random

### Discord Bot
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

#### Unifi
UNIFI_API_URL = os.getenv("UNIFI_API_URL")
UNIFI_API_KEY = os.getenv("UNIFI_API_KEY")

# Erstelle eine Bot-Instanz mit Intents zum Lesen von Nachrichten
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

# Passwort-Kriterien
def is_secure_password(password):
    if any(umlaut in password for umlaut in "äöüÄÖÜß"):
        return False, "Umlauts are not allowed! Use ae, oe, ue, ss instead."
    if len(password) > 60:
        return False, "It's too long... (max 60 characters)."
    if len(password) < 10:
        return False, "It's too short... (minimum 10 characters)."
    if not re.search(r"\d", password):
        return False, "There must be at least one number like 4, 23, 420."
    if not re.search(r"[A-Z]", password):
        return False, "There must be at least one uppercase letter like A, B, C, ... "
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "There must be at least one special character like #, !, ?."
    return True, "Seems to be safe! :-)"

def is_not_in_dict_password(password):
    with open("dict.txt", 'r') as file:
        content = file.read()
        if password in content:
            return False, "This word was found in the dictionary :-(" 
        else:
            return True, "This word was not found in the dictionary :-) "

def update_unifi(password):
    HEADERS = {
        "X-API-KEY": UNIFI_API_KEY,
        "Content-Type": "application/json"
    }
    DATA = {"x_passphrase": password}
    try:
        response = requests.put(UNIFI_API_URL, headers=HEADERS, json=DATA, timeout=5, verify=False)
        http_rc = response.status_code
        print(f"Unifi HTTP Response Code: {http_rc}")
    except requests.RequestException as e:
        print(f"Error - request failed to Unifi: {e}")
        return False, "Couldn't connect to Unifi."

    if http_rc == 401:
        print("Error: Unauthorized Unifi / Maybe the token is expired...")
        return False, "Access Denied - Maybe Unifi Token expired?"
    elif http_rc == 200:
        print("Updated successfully on Unifi")
        return True, "Updated successfully"
    else:
        print(f"Error: Undefined error, HTTP_CODE={http_rc}")
        return False, "Unknown Error"

# Event: Bot ist bereit
@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

# Event: Nachrichten verarbeiten
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    words = message.content.split()
    if not words:
        return
    
    first_word = words[0]  # Nur das erste Wort prüfen
    print("Checking: ", first_word)
    
    # Hilfe-Menü
    if first_word.lower() == "help" or first_word.lower() == "hilfe":
        help_text = (
            "🤖 **Bot Befehle:**\n"
            "- `set <passwort>` - Sets a new passwort (must be safe), example: 'set S3cretPassw0rd!'\n"
            "- `dice` - Roll a dice 🎲\n"
            "- `slap <username>` - Slaps a user´s ass 🖐️\n"
            "- `bananenbrot` - yummy! 🍌🥖\n"
            "- `eggs <username>` - Put your Eggs on someones chin 🥚\n"
            "- `hilfe or help` - this help box ℹ️ \n"
        )
        await message.channel.send(help_text)
        return
    
    # Easter Egg: Geheime Nachricht für ein spezielles Passwort
    if first_word.lower() == "bananenbrot":
        await message.channel.send("🍌🥖 Bananenbrot ist das beste Brot! Hast du schon eins gebacken? 🤩")
        return
    
    # Easter Egg: Würfel werfen
    if first_word.lower() == "dice":
        dice_roll = random.randint(1, 6)
        await message.channel.send(f"🎲 You rolled a {dice_roll}!")
        return
    
    # Easter Egg: Slap
    if first_word.lower() == "slap" and len(words) > 1:
        target = words[1]
        await message.channel.send(f"🖐️😏 {message.author.display_name} slaps {target} on the ass! 🍑")
        return

   # Easter Egg: Egg
    if first_word.lower() == "eggs" and len(words) > 1:
        target = words[1]
        await message.channel.send(f"😏🥚🥚 {message.author.display_name} put his eggs on {target}´s chin 🫦")
        return 
    
    # Passwort nur setzen, wenn erstes Wort "set" ist
    if first_word.lower() == "set" and len(words) > 1:
        password = words[1]
        is_secure, msg_is_secure = is_secure_password(password)
        print(is_secure, msg_is_secure)
        is_not_in_dict, msg_is_in_dict = is_not_in_dict_password(password)
        print(is_not_in_dict, msg_is_in_dict)
        
        if is_secure and is_not_in_dict:
            await message.channel.send("✅ Secure password detected. Updating password...")
            updated_unifi, msg_updated_unifi = update_unifi(password)
            print(updated_unifi, msg_updated_unifi)
            if updated_unifi:
                await message.channel.send("✅ Updated successfully :-)")
            else:
                await message.channel.send(f"⚠️ {msg_updated_unifi}")
        else:
            if not is_secure:
                await message.channel.send(f"⚠️ {msg_is_secure}")
            if not is_not_in_dict:
                await message.channel.send(f"⚠️ {msg_is_in_dict}")

# Bot starten
bot.run(DISCORD_BOT_TOKEN)
