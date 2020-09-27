import urllib.request
import urllib.error
import urllib.parse


def request(url):
    request = urllib.request.Request(url)

    request.add_header("USER_AGENT",
                       "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7")
    request.add_header("accept-language",
                       "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/85.0.4183.121 Safari/537.36")
    request.add_header("sec-fetch-dest",
                       "document")
    request.add_header("accept",
                       "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                       "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
    response = urllib.request.urlopen(request)
    content = response.read()

    return content.decode("utf-8")
