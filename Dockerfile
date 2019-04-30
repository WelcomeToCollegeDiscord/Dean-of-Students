FROM gorialis/discord.py:3.7-rewrite-extras

WORKDIR /app

RUN sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl && \
 sudo chmod a+rx /usr/local/bin/youtube-dl && \
 sudo rm -r /usr/local/lib/python3.7/site-packages/youtube-dl && \
 sudo pip3 install feedparser markovify youtube-dl && \
 sudo apt-get update && \
 sudo apt-get install units -y



COPY . .

CMD ["./run-owl.sh"]
