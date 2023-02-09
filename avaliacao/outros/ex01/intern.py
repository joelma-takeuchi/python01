#!/usr/bin/python3

def main():
    mark = Intern("Mark")
    intern = Intern()
    print(mark.name)
    print(intern.name)
    print(mark.make_coffee())
    try:
        intern.work()
    except Exception as err:
        print(err)

class Intern:
    def __init__(self, name: str = "My name? I'm nobody, an intern, I have no name"):
        self.name = name

    def __str__(self):
        return self.name

    class Coffee:
        def __init__(self):
            pass

        def __str__(self):
            return "This is the worst coffee you ever tasted"

    def work(self):
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self):
        return self.Coffee()


if __name__ == "__main__":
    main()
