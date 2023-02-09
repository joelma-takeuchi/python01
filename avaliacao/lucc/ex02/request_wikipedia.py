import requests, sys, dewiki, json


def get_search_wikipedia(search_text):

    session = requests.Session()

    url = "https://en.wikipedia.org/w/api.php"


    params = {
        "action": "parse",
        "prop": "wikitext",
        "page": search_text,
        "redirects": True,
        "format": "json"
    }

    result = session.get(url=url, params=params)
    if result.status_code == 200:
        data = result.json()
        try:
            content = data["parse"]["wikitext"]["*"]
        except:
            print("A pesquisa não retornou dados para esse termo")
            return False, ""
        return True, dewiki.from_string(content)
    else:
        print("Erro na chamada da API")
        return False, ""

def write_file(filename,text):

    with open(f"{filename}.wiki", "w") as file:
        file.write(text)   

    print(f"Arquivo {filename}.wiki gerado com sucesso")

def main():
    if len(sys.argv) == 2:
        result = get_search_wikipedia(sys.argv[1])
        if result[0]:
            write_file(filename=sys.argv[1].strip().replace(" ", ""),text=result[1])
    else:
        print("Número de parâmetros incorreto")
if __name__ == '__main__':
    main()