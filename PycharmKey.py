import requests
import bs4
def get_response(url):
    headers = {

        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149,Safari/537.36",

        "Referer": "http://lookdiv.com/"
    }
    post_data = {
        "key": "lookdiv"
    }
    resp = requests.post(url, headers=headers, data = post_data)
    return resp.text
def parse_html(context):
    soup = bs4.BeautifulSoup(context, 'html.parser')
    return soup.select('textarea.form-control')[0].text.strip()


if __name__ == '__main__':

    url = "http://lookdiv.com/nssdh/sereas/sxclo/aloif/smxs/slak/pdoasj/ejekoq/ewqqzsd/wsdwwq/ers.html"
    html = get_response(url)
    licence = parse_html(html)

    with open('activate_code.txt','w') as file:
        file.write(licence)

