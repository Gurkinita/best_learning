import argparse
import re
import requests


class UrlAnalyzer:
    def __init__(self, url=None):
        if url:
            self.url = url
        else:
            self.url = self.user_input()
        self.link_analyzer = LinkAnalyzer(self.url)

    @staticmethod
    def user_input():
        parser = argparse.ArgumentParser()
        parser.add_argument('-url', type=str, help='Please set URL for parsing')
        args = parser.parse_args()
        if args.url:
            if not args.url.startswith('http://') and not args.url.startswith('https://'):
                args.url = 'http://' + args.url
            return args.url
        else:
            url = input('Please set URL for parsing: ')
            if not url.startswith('http://') and not url.startswith('https://'):
                url = 'http://' + url
            return url

    def parse_html_page(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            links = self.get_links_from_url(response.text)
            self.link_analyzer.check_links(links)
        else:
            print(f"Failed to retrieve the HTML page. Status code: {response.status_code}")

    def get_links_from_url(self, html) -> list:
        base_url = self.url.split('/', 3)[:3]
        links = re.findall(r'<a href="(.*?)"', html)
        absolute_links = []
        for link in links:
            if link.startswith('/'):
                absolute_link = base_url[0] + '//' + base_url[2] + link
                absolute_links.append(absolute_link)
            else:
                absolute_links.append(link)
        return absolute_links


class LinkAnalyzer:
    def __init__(self, url):
        self.url = url

    def check_link(self, link):
        try:
            response = requests.get(link)
            if response.status_code == 200:
                with open('valid_links.txt', 'a') as file:
                    file.write(link + '\n')
            else:
                with open('broken_links.txt', 'a') as file:
                    file.write(link + '\n')
        except requests.exceptions.MissingSchema:
            with open('broken_links.txt', 'a') as file:
                file.write(link + '\n')

    def check_links(self, links):
        for link in links:
            self.check_link(link)



if __name__ == "__main__":
    url = UrlAnalyzer()
    url.parse_html_page()
