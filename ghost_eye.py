#!/usr/bin/env/python3
# This Python file uses the following encoding: utf-8

# ===== #
#   
# ▀█████████▄     ▄████████         Websites: HackingPassion.com | Bullseye0.com
#   ███    ███   ███    ███         Author: Jolanda de Koff | Bulls Eye
#   ███    ███   ███    █▀          GitHub: https://github.com/BullsEye0
#  ▄███▄▄▄██▀   ▄███▄▄▄             linkedin: https://www.linkedin.com/in/jolandadekoff
# ▀▀███▀▀▀██▄  ▀▀███▀▀▀             Facebook Group: https://www.facebook.com/groups/hack.passion/
#   ███    ██▄   ███    █▄          Facebook: https://www.facebook.com/profile.php?id=100069546190609
#   ███    ███   ███    ███         Twitter: https://twitter.com/bulls__eye
# ▄█████████▀    ██████████         LBRY: https://lbry.tv/$/invite/@hackingpassion:9
#          Bulls Eye..!
# ===== #

# ===== #
# Created July 2019 | Copyright (c) 2019 - 2021 Jolanda de Koff.
# Update April 2021
# ===== #

########################################################################

# A notice to all nerds and n00bs...
# If you will copy the developer's work it will not make you a hacker..!
# Respect all developers, we doing this because it's fun...

########################################################################

# install dnsutils
# install gnome-terminal
# install httpie
# install mtr

# sudo apt install dnsutils gnome-terminal httpie mtr
# sudo pacman -S dnsutils gnome-terminal httpie mtr

########################################################################

from collections import deque
from html.parser import HTMLParser
import json
import os
import re
import subprocess
import sys
import time
from time import gmtime, strftime
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlencode
import urllib.request


USER_AGENT = "GhostEye/3.14 (standard library)"


class LinkParser(HTMLParser):
    """Small HTML parser used instead of BeautifulSoup."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag.lower() == "a" and attributes.get("href"):
            self.links.append(attributes["href"])
        self._in_title = tag.lower() == "title"

    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def fetch(url, timeout=10, opener=None):
    """Fetch a URL using urllib and return text, bytes, and headers."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    client = opener or urllib.request
    with client.urlopen(request, timeout=timeout) as response:
        content = response.read()
        charset = response.headers.get_content_charset() or "utf-8"
        return content.decode(charset, errors="replace"), content, response.headers


def parse_html(content):
    parser = LinkParser()
    parser.feed(content)
    return parser


def banner():
    print(""" \033[1;34m
             ('-. .-.               .-')    .-') _            ('-.                 ('-.
            ( OO )  /     Ghost    ( OO ). (  OO) )         _(  OO)      Eye     _(  OO)
             ,----.    ,--. ,--. .-'),-----. (_)---\\_)/     '._       (,------. ,--.   ,--.(,------.
 '  .-./-') |  | |  |( OO'  .-.  '/    _ | |'--...__)       |  .---'  \\  `.'  /  |  .---'
 |  |_( O- )|   .|  |/   |  | |  |\\  :` `. '--.  .--'       |  |    .-')     /)  |  |
 |  | .--, \\|       |\\_) |  |\\|  | '..`''.)   |  |         (|  '--.(OO  \\   /.  (|  '--.
(|  | '. (_/|  .-.  |  \\ |  | |  |.-._)   \\   |  |          |  .--' |   /  /     |  .--'
 |  '--'  | |  | |  |   `'  '-'  '\\       /   |  |          |  `---.`-./  /      |  `---.
  `------'  `--' `--'     `-----'  `-----'    `--' V2       `------'  `--'       `------'
            \033[1;m
        \033[34mGhost Eye - Information Gathering Tool \033[0m
        \033[34mAuthor: Jolanda de Koff aka Bulls Eye \033[0m
        \033[34mGithub:  https://github.com/BullsEye0 \033[0m
        \033[34mWebsite: https://hackingpassion.com \033[0m

              Hi there, Shall we play a game..? 😃 """)


def menu():
    print("\n\033[1;34m[+] 1.   EtherApe – Graphical Network Monitor (root)\033[1;m")
    print("\033[1;34m[+] 2.   DNS Lookup\033[1;m")
    print("\033[1;34m[+] 3.   Whois Lookup \033[1;m")
    print("\033[1;34m[+] 4.   Nmap Port Scan\033[1;m")
    print("\033[1;34m[+] 5.   HTTP Header Grabber\033[1;m")
    print("\033[1;34m[+] 6.   Clickjacking Test - X-Frame-Options Header\033[1;m")
    print("\033[1;34m[+] 7.   Robots.txt Scanner\033[1;m")
    print("\033[1;34m[+] 8.   Cloudflare Cookie scraper\033[1;m")
    print("\033[1;34m[+] 9.   Link Grabber\033[1;m")
    print("\033[1;34m[+] 10.  IP Location Finder\033[1;m")
    print("\033[1;34m[+] 11.  Detecting CMS with Identified Technologies\033[1;m")
    print("\033[1;34m[+] 12.  Traceroute\033[1;m")
    print("\033[1;34m[+] 13.  Crawler target url + Robots.txt\033[1;m")
    print("\033[1;34m[+] 14.  Certificate Transparency log monitor\033[1;m")
    print("\033[1;34m[x] 15.  Exit\033[1;m\n")


def fun():
    choice = ("1")
    banner()

    while choice != ("12"):
        menu()
        choice = input("\033[1;34m[+]\033[1;m \033[1;91mEnter your choice:\033[1;m ")

        if choice == ("3"):
            try:
                target = input("\033[1;91m[+] Enter Domain or IP Address: \033[1;m").lower()
                os.system("reset")
                print("\033[34m[~] Searching for Whois Lookup: \033[0m".format(target) + target)
                time.sleep(1.5)
                command = ("whois " + target)
                proces = os.popen(command)
                results = str(proces.read())
                print(results + command)

            except Exception:
                pass

        elif choice == ("2"):
            try:
                target = input("\033[1;91m[+] Enter Domain or IP Address: \033[1;m").lower()
                os.system("reset")
                print("\033[34m[~] Searching for DNS Lookup: \033[0m".format(target) + target)
                time.sleep(1.5)
                command = ("dig " + target + " +trace ANY")
                proces = os.popen(command)
                results = str(proces.read())
                print(results + command)

            except Exception:
                pass

        elif choice == ("1"):
            try:
                os.system("reset")
                os.system("gnome-terminal -e 'bash -c \"sudo etherape; exec bash\"'")

            except Exception:
                pass

        elif choice == ("4"):
            try:
                target = input("\033[1;91m[+] Enter Domain or IP Address: \033[1;m").lower()
                os.system("reset")
                print("\033[34m[~] Scanning Nmap Port Scan: \033[0m" + target)
                print("This will take a moment... Get some coffee 😃 )\n")
                time.sleep(1.5)

                command = ("nmap -Pn " + target)
                process = os.popen(command)
                results = str(process.read())
                logPath = "logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())

                print(results + command + logPath)
                try:
                    version = subprocess.run(
                        ["nmap", "--version"], capture_output=True,
                        text=True, check=False,
                    ).stdout.splitlines()[0]
                except (FileNotFoundError, IndexError):
                    version = "nmap is not installed"
                print("\033[34mNmap Version: \033[0m", version)

            except KeyboardInterrupt:
                    print("\n")
                    print("[-] User Interruption Detected..!")
                    time.sleep(1)

        elif choice == ("5"):
            try:
                target = input("\033[1;91m[+] Enter Domain or IP Address: \033[1;m").lower()
                os.system("reset")
                print("\033[34m[~] Scanning HTTP Header Grabber: \033[0m\n" + target)
                time.sleep(1.5)
                command = ("http -v " + target)
                proces = os.popen(command)
                results = str(proces.read())
                print(results + command)

            except Exception:
                pass

        elif choice == ("6"):
            target = input("\033[1;91m[+] Enter the Domain to test: \033[1;m").lower()
            os.system("reset")

            if not (target.startswith("http://") or target.startswith("https://")):
                target = "http://" + target
            print("\033[1;34m[~] Testing Clickjacking Test: \033[1;m" + target)
            time.sleep(2)
            try:
                _, _, headers = fetch(target)
                print("\nHeader set are: \n")
                for item, xfr in headers.items():
                    print("\033[1;34m" + item + ":" + xfr + "\033[1;m")

                if "X-Frame-Options" in headers.keys():
                    print("\n[+] \033[1;34mClick Jacking Header is present\033[1;m")
                    print("[+] \033[1;34mYou can't clickjack this site !\033[1;m\n")
                else:
                    print("\n[*] \033[1;34mX-Frame-Options-Header is missing ! \033[1;m")
                    print("[!] \033[1;34mClickjacking is possible,this site is vulnerable to Clickjacking\033[1;m\n")

            except Exception as ex:
                print("\033[1;34mException caught: " + str(ex))

        elif choice == ("7"):
            try:
                target = input("\033[1;91m[+] Enter Domain: \033[1;m").lower()
                os.system("reset")
                print("\033[34m[~] Scanning Robots.txt Scanner: \033[0m\n" + target)
                time.sleep(1.5)

                if not (target.startswith("http://") or target.startswith("https://")):
                    target = "http://" + target
                robot = target + "/robots.txt"

                try:
                    bots, _, _ = fetch(robot)
                    print("\033[34m" + (bots) + "\033[1;m")
                except URLError:
                    print("\033[1;31m[-] Can\'t access to {page}!\033[1;m".format(page=robot))

            except Exception as ex:
                print("\033[1;34mException caught: " + str(ex))

        elif choice == ("8"):
            target = input("\033[1;91m[+] Enter Domain: \033[1;m").lower()
            if not (target.startswith("http://") or target.startswith("https://")):
              	target = "http://" + target
            os.system("reset")
            print("[+] Cloudflare cookie scraper ")
            time.sleep(1.5)

            try:
                print("[+] Target: " + target)
                cookie_jar = urllib.request.HTTPCookieProcessor()
                opener = urllib.request.build_opener(cookie_jar)
                text, _, _ = fetch(target, opener=opener)
                cookies = "; ".join(
                    f"{cookie.name}={cookie.value}"
                    for cookie in cookie_jar.cookiejar
                )
                print("[+] Print Cookie\n")
                print(f"Cookie: {cookies}\r\nUser-Agent: {USER_AGENT}")
                print("\n[+] Scraper\n")
                print(text)

            except (HTTPError, URLError) as ex:
                print(f"[X] Unable to fetch the page: {ex}")

        elif choice == ("9"):
            try:
                target = input("\033[1;91m[+] Enter Domain: \033[1;m").lower()
                os.system("reset")
                print("\033[34m[~] Scanning Link Grabber: \033[0m\n" + target)
                time.sleep(2)
                if not (target.startswith("http://") or target.startswith("https://")):
                    target = "http://" + target
                deq = deque([target])
                pro = set()

                try:
                    while len(deq):
                        url = deq.popleft()
                        pro.add(url)
                        print("[+] Crawling URL " + "\033[34m" + url + "\033[0m")
                        try:
                            response, _, _ = fetch(url)
                        except (ValueError, HTTPError, URLError):
                            continue

                        soup = parse_html(response)
                        for link in soup.links:
                            link = urljoin(url, link)
                            if not link in deq and not link in pro:
                                deq.append(link)
                            continue

                except KeyboardInterrupt:
                        print("\n")
                        print("[-] User Interruption Detected..!")
                        time.sleep(1)
                        print("\n \t\033[34m[!] I like to See Ya, Hacking Anywhere ..!\033[0m\n")

            except Exception:
                pass

        elif choice == ("10"):
            try:
                target = input("\033[1;91m[+] Enter Domain or IP Address: \033[1;m").lower()
                url = ("http://ip-api.com/json/")
                _, data, _ = fetch(url + target)
                jso = json.loads(data)
                os.system("reset")
                print("\033[34m[~] Searching IP Location Finder: \033[0m".format(url) + target)
                time.sleep(1.5)

                print("\n [+] \033[34mUrl: " + target + "\033[0m")
                print(" [+] " + "\033[34m" + "IP: " + jso["query"] + "\033[0m")
                print(" [+] " + "\033[34m" + "Status: " + jso["status"] + "\033[0m")
                print(" [+] " + "\033[34m" + "Region: " + jso["regionName"] + "\033[0m")
                print(" [+] " + "\033[34m" + "Country: " + jso["country"] + "\033[0m")
                print(" [+] " + "\033[34m" + "City: " + jso["city"] + "\033[0m")
                print(" [+] " + "\033[34m" + "ISP: " + jso["isp"] + "\033[0m")
                print(" [+] " + "\033[34m" + "Lat & Lon: " + str(jso['lat']) + " & " + str(jso['lon']) + "\033[0m")
                print(" [+] " + "\033[34m" + "Zipcode: " + jso["zip"] + "\033[0m")
                print(" [+] " + "\033[34m" + "TimeZone: " + jso["timezone"] + "\033[0m")
                print(" [+] " + "\033[34m" + "AS: " + jso["as"] + "\033[0m" + "\n")

            except URLError:
                print("\033[1;31m[-] Please provide a valid IP address!\033[1;m")

        elif choice == ("11"):
            try:
                target = input("\033[1;91m[+] Enter Domain: \033[1;m").lower()
                if not (target.startswith("http://") or target.startswith("https://")):
                 	target = "https://" + target
                os.system("reset")
                print("\033[34m[~] Detecting CMS with Identified Technologies and Custom Headers from target url: \033[0m")
                time.sleep(5)
                content, _, headers = fetch(target, timeout=10)
                technologies = []
                server = headers.get("Server")
                powered_by = headers.get("X-Powered-By")
                if server:
                    technologies.append("Server: " + server)
                if powered_by:
                    technologies.append("X-Powered-By: " + powered_by)
                signatures = {
                    "WordPress": ("/wp-content/", "wp-includes"),
                    "Joomla": ("/media/jui/", "joomla"),
                    "Drupal": ("drupal-settings-json", "sites/default/files"),
                }
                lower_content = content.lower()
                for name, markers in signatures.items():
                    if any(marker.lower() in lower_content for marker in markers):
                        technologies.append(name)
                sys.stdout.write("\n".join(technologies) or "No common CMS detected.")

            except Exception:
                pass

        elif choice == ("12"):
            try:
                target = input("\033[1;91m[+] Enter Domain or IP Address: \033[1;m").lower()
                os.system("reset")
                print("\033[34m[~] Searching for Traceroute \033[0m".format(target) + target)
                print(">> This will take a moment... Get some coffee << )\n")
                time.sleep(5)
                command = ("mtr " + "-4 -rwc 1 " + target)
                proces = os.popen(command)
                results = str(proces.read())
                print("\033[1;34m" + results + command + "\033[1;m")
                fun()

            except KeyError:
             	pass

        elif choice == ("13"):
            target = input("\033[1;91m[+] Enter Domain: \033[1;m").lower()
            os.system("reset")
            print("\033[34m[~] Start crawler... \033[0m")
            time.sleep(5)
            print("[+] Target: " + target)
            if not (target.startswith("http://") or target.startswith("https://")):
                target = "http://" + target
            try:
                content, _, _ = fetch(target)
                regex_t = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
                tit = re.findall(regex_t, content)

                regex_l = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
                link = re.findall(regex_l, content)

                robots, _, _ = fetch(target + "/robots.txt")

                print("[+] Title: " + "".join(tit) + "\n")
                print("[+] Extract links: \n" + "\n".join(link) + "\n")
                print("[+] Robots.txt: \n" + robots)

            except KeyError:
             	pass

        elif choice == ("14"):
            target = input("\033[1;91m[+] Enter Domain: \033[0m")
            os.system("reset")
            print("\033[34m[~] Scanning Certificate Transparency log monitor: \033[0m\n" + target)
            time.sleep(1.5)
            print("[+] Target: " + target)
            try:
                query = urlencode({"domain": target, "expand": "dns_names"})
                content, _, _ = fetch("https://api.certspotter.com/v1/issuances?" + query)
                issuances = json.loads(content)
                names = sorted({
                    name.lstrip("*.")
                    for issuance in issuances
                    for name in issuance.get("dns_names", [])
                    if target in name
                })
                print(*names, sep="\n")

            except (KeyError, HTTPError, URLError, json.JSONDecodeError) as ex:
                print(f"[-] Certificate lookup failed: {ex}")

        elif choice == ("15"):
            time.sleep(1)
            print("\n\t\033[34mBlue Eye\033[0m DONE... Exiting... \033[34mLike to See Ya Hacking Anywhere ..!\033[0m\n")
            sys.exit()

        else:
            os.system("reset")
            print("\033[1;31m[-] Invalid option..! \033[1;m")


# =====# Main #===== #

if __name__ == "__main__":
    fun()
