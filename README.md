# Ghost Eye
Ghost Eye - Information Gathering Tool

> **Fork notice:** This repository is a modified fork of the original
> [BullsEye0/ghost_eye](https://github.com/BullsEye0/ghost_eye) project.
> The original author and GPL-3.0 license are retained. This fork updates
> the code to use Python's standard library without pip-based dependencies
> and adds Python 3.14 compatibility improvements.

**Ghost Eye** New Release. Ghost Eye is an Information Gathering, Footprinting, Scanner, and Recon Tool I made in Python 3. Since the last release of Ghost Eye, I've tweaked, removed, and added some new features. So that Ghost Eye would become more of a whole. For me, it remains a game of options so that together you get a complete overview of your target.
****
Here you can read an article i wrote about Ghost Eye
https://hackingpassion.com/ghost-eye-informationgathering-footprinting-and-reconnaissance-tool-release/
****
## Ghost Eye gathers information data such as:
Hi there, Shall we play a game..? 😃
[+] 1.   EtherApe – Graphical Network Monitor (root)

[+] 2.   DNS Lookup

[+] 3.   Whois Lookup

[+] 4.   Nmap Port Scan

[+] 5.   HTTP Header Grabber

[+] 6.   Clickjacking Test - X-Frame-Options Header

[+] 7.   Robots.txt Scanner

[+] 8.   Cloudflare Cookie scraper

[+] 9.   Link Grabber

[+] 10.  IP Location Finder

[+] 11.  Detecting CMS with Identified Technologies

[+] 12.  Traceroute

[+] 13.  Crawler target url + Robots.txt

[+] 14.  Certificate Transparency log monitor

[x] 15.  Exit

[+] Enter your choice:

![Screenshot](featured-image.png)
  
## Video demo: Watch on LBRY/Odysee
**[Video](https://open.lbry.com/@hackingpassion:9/Ghost-Eye-Informationgathering-Footprinting-Scanner-and-Recon-Tool-Release:3)**

****

## Install and run on Linux

Ghost Eye uses only Python's standard library. No Python packages, `pip`, or
`requirements.txt` installation is needed.
  
* On Arch Linux and its distros: 
```bash
sudo pacman -S etherape nmap dnsutils gnome-terminal httpie mtr
```
  
* On Debian and its distros (Kali Linux, Parrot Security OS):
```bash
sudo apt update
sudo apt install python3 nmap dnsutils whois gnome-terminal httpie mtr etherape
```
After installing Etherape sometimes a GNOME error can occur, for which you install: (This will solve the common error)
```bash
apt install libgnomeui-0:amd64
```
****
    
## Installation Steps

1. **Clone the repository:**
```bash
git clone https://github.com/BullsEye0/ghost_eye.git
cd ghost_eye
```

2. **Check Python:**
```bash
python3 --version
```

Python 3.14 is recommended. If your distribution provides a separate
`python3.14` package, install it with `sudo apt install python3.14` and use
`python3.14` below.

3. **Run Ghost Eye:**

****

```bash
python3.14 ghost_eye.py
```

The Python code itself has no third-party package dependencies, so do not run
`pip install` or `pip3 install`. The menu features use the Linux programs
installed with `apt` above.

Have fun ..! 😃

****

# Contact to coder
Social Networks - Connect

* Website [HackingPassion.com](https://hackingpassion.com)

* [Facebook Personal](https://www.facebook.com/profile.php?id=100069546190609)

* [linkedin](https://www.linkedin.com/in/jolandadekoff/)

* [LBRY/Odysee](https://lbry.tv/$/invite/@hackingpassion:9)

* [Youtube](https://www.youtube.com/@HackingPassion)

* [Facebook Page](https://www.facebook.com/ethical.hack.group)

* [Facebook Group](https://www.facebook.com/groups/ethical.hack.group/)


***

## 💻 Support this project

If you find this tool useful, consider supporting my work:  
[❤️ Sponsor BullsEye](https://github.com/sponsors/BullsEye0)

Get the full hands-on course:  
**[Ethical Hacking Complete Course – Zero to Expert](https://www.udemy.com/course/ethical-hacking-complete-course-zero-to-expert/?couponCode=SEPTEMBER)**

(supports me directly as your instructor!)

Professional penetration testing. Zero to Expert.  
✅ Kali Linux + Parrot OS  
✅ Real-world hacking scenarios  
✅ All major tools & techniques  
✅ Beginner-friendly  

HACKING IS NOT A HOBBY, BUT A WAY OF LIFE 🎯

***

## Donate

I have developed Ghost Eye because I am passionate about this. 
Donations are one of the many ways to support what I do.

[Donate](https://hackingpassion.com/donate/)

BAT: Use [Brave](https://brave.com/bul891) and donate on any of my web pages/profiles

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=R96YN2PUS8V8W)
