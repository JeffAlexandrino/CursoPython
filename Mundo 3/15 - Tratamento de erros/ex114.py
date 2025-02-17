import urllib.request

def check_website(url):
    try:
        response = urllib.request.urlopen(url)
        return True
    except:
        return False

url = "http://www.pudim.com.br"
if check_website(url):
    print(f"O site {url} está acessível.")
else:
    print(f"O site {url} não está acessível.")