from elem import Elem, Text

def main():
    html = Html ([Head(Title(Text(r"\"Hello Ground!\""))), Body([H1(Text(r"\"Oh no, not again!\"")), Img({"src" : "http://i.imgur.com/pfp3T.jpg"})])])
    print(html)

class Html(Elem):
    def __init__(self, content=[], attr={}):
        super().__init__(tag='html', attr=attr, content=content)

class Head(Elem):
    def __init__(self, content=[], attr={}):
        super().__init__(tag='head', attr=attr, content=content)

class Body(Elem):
    def __init__(self, content=[], attr={}):
        super().__init__(tag='body', attr=attr, content=content)

class Title(Elem):
    def __init__(self, content=[], attr={}):
        super().__init__(tag='title', attr=attr, content=content)

class Meta(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='title', attr=attr, tag_type="simple")

class Img(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='img', attr=attr, tag_type="simple")

class Table(Elem):
    def __init__(self, content=[], attr={}):
        super().__init__(tag='table', content=content, attr=attr)

class Th(Elem):
    def __init__(self, content=[], attr={}):
        super().__init__(tag='th', content=content, attr=attr)

class Tr(Elem):
    def __init__(self, content=[], attr={}):
        super().__init__(tag='tr', content=content, attr=attr)

class Ul(Elem):
    def __init__(self, content=[], attr={}):
        super().__init__(tag='ul', content=content, attr=attr)

class Ol(Elem):
    def __init__(self, content=[], attr={}):
        super().__init__(tag='ol', content=content, attr=attr)

class Li(Elem):
    def __init__(self, content=[], attr={}):
        super().__init__(tag='li', content=content, attr=attr)

class H1(Elem):
    def __init__(self, content=[], attr={}):
        super().__init__(tag='h1', content=content, attr=attr)

class H2(Elem):
    def __init__(self, content=[], attr={}):
        super().__init__(tag='h2', content=content, attr=attr)

class P(Elem):
    def __init__(self, content=[], attr={}):
        super().__init__(tag='p', content=content, attr=attr)

class Div(Elem):
    def __init__(self, content=[], attr={}):
        super().__init__(tag='div', content=content, attr=attr)

class Span(Elem):
    def __init__(self, content=[], attr={}):
        super().__init__(tag='span', content=content, attr=attr)

class Hr(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='hr', tag_type="simple", attr=attr)

class Br(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='br', tag_type="simple", attr=attr)

if __name__ == "__main__":
    main()
