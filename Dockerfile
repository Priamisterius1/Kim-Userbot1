# KIM USERBOT
FROM biansepang/weebproject:buster

# Dockerfile
# KIM
# Dockerfile
RUN git clone -b Kim-Userbot https://github.com/abdurrohimbontro/Kim-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/abdurrohimbontro/Kim-Userbot/Kim-Userbot/requirements.txt

CMD ["python3","-m","userbot"]
