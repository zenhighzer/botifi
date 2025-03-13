FROM alpine
RUN apk update && apk add --no-cache python3 py3-pip
RUN pip3 install --break-system-packages --root-user-action=ignore requests discord.py
RUN wget https://github.com/danielmiessler/SecLists/raw/refs/heads/master/Passwords/Common-Credentials/Language-Specific/German_common-password-list.txt -O dict.txt
COPY ./bot.py ./bot.py
CMD ["python3", "./bot.py"]
