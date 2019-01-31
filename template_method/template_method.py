# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class AbstractReport(metaclass=ABCMeta):

    def __init__(self, title, text_list):
        self.title = title
        self.text_list = text_list

    @abstractmethod
    def pprint(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def end(self):
        pass

    def display(self):
        self.start()
        self.pprint()
        self.end()


class HtmlReport(AbstractReport):

    def pprint(self):
        for text in self.text_list:
            print('<p>'+text+'</p>')

    def start(self):
        title = "<html><head>"
        title += "<title>"+self.title+"</title>"
        title += "</head><body>"
        print(title)

    def end(self):
        title = "</body></html>"
        print(title)


class PlaneTextReport(AbstractReport):
    
    def pprint(self):
        for text in self.text_list:
            print(text)

    def start(self):
        title = "**** #"+self.title+" ****"
        print(title)

    def end(self):
        pass


def main():
    title = "Html Report Title"
    text = [
        "report line 1",
        "report line 2",
        "report line 3"
    ]

    html_report = HtmlReport(title, text)
    html_report.display()
    print()

    plane_report = PlaneTextReport(title, text)
    plane_report.display()
    print()


if __name__ == '__main__':
    main()
