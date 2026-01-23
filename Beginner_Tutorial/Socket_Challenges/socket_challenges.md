At the 247/CTF, challenges are not shared with multiple players and VPNs are not required. Instead, you have the control to start and stop your own unique challenge instance at any time. Once you have launched a challenge, you can access the instance by clicking on the pop up which loads in the bottom right hand corner of every page.

Click the ‘START CHALLENGE’ button to the right of this text description to start a socket challenge. Once the challenge instance is launched, the pop up will contain either a tcp:// or udp:// link to access the socket hosting your challenge. Connect to the socket using a tool such as [netcat](https://en.wikipedia.org/wiki/Netcat) or [telnet](https://en.wikipedia.org/wiki/Telnet) and submit the flag!

Once you start the cahllenge and click on the pop up, you are taken to the challenge url (example: tcp://b2518cbde73f1183.247ctf.com:50484)

Install [MYSYS2](https://www.msys2.org/) if working on windows for executing netcat. Run **pacman -S netcat** to install netcat in mysys2.

Run nc or netcat followed by the url without the tcp:// and : before the port number (example: **nc b2518cbde73f1183.247ctf.com:50484**)