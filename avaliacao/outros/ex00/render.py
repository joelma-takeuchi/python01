import sys

def main():
    dict_settings = {}
    settings = get_settings()
    suffix = sys.argv[1].split('.')[0]
    htmlfile = suffix + '.html'
    html = open(htmlfile, "w")
    template = open(sys.argv[1], "r")
    template_content = template.read()
    settings = settings.strip().split("\n")
    for var in settings:
        tmp = var.split("=")
        tmp[1] = tmp[1].strip('"')
        dict_settings[tmp[0]] = tmp[1]
    template_content = template_content.format(**dict_settings)
    html.write(template_content)

def get_settings():
    file = open("settings.py", "r")
    tmp = file.read()
    file.close()
    return tmp

def validate():
    files = ["settings.py"]
    files.append(sys.argv[1])
    argc = len(sys.argv)
    if argc != 2:
        sys.exit(1)
    elif not (sys.argv[1].endswith(".template")):
        sys.exit(1)
    for file in files:
        try:
            with open(file, "r") as f:
                file = f.read()
        except:
            sys.exit(1)


if __name__ == "__main__":
    validate()
    main()
