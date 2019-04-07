import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    fact = get_fact()

    url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
    body = {'input_text': str(fact)}
    headers = {'Host': 'hidden-journey-62459.herokuapp.com',
               'Connection': 'keep-alive',
               'Content-Length': '30',
               'Cache-Control': 'max-age=0',
               'Origin': 'https://hidden-journey-62459.herokuapp.com',
               'Upgrade-Insecure-Requests': '1',
               'Content-Type': 'application/x-www-form-urlencoded',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/73.0.3683.86 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/'
                         'xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                         'application/signed-exchange;v=b3',
               'Referer': 'https//hidden-journey-62459.herokuapp.com/',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'en-US,en;q=0.9'}

    r = requests.request('POST', url, data=body, headers=headers,
                         allow_redirects=False)
    link = r.headers['Location']
    template = "<html>" \
               "<body>" \
               "<p>Link for Pig Latin Conversion:</p>" \
               "<a href='{}'>{}</a>" \
               "</body>" \
               "</html>".format(link, str(fact))

    return template


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

