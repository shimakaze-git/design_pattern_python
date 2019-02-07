# -*- coding: utf-8 -*-

from report import HtmlReport, PlaneTextReport

def main():
    title = "Report Title"
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
