#dag

Domain At Glance, aka dag

Quick and concise dig and whois to get a quick overview of a domain's information for the purpose of troubleshooting hosting issues with domains.

NOTE: If you are using an Ubuntu-based distro such as Linux Mint, be aware that starting Ubuntu 6.10, the default system shell, /bin/sh, was changed to /bin/dash. This means that certain extensions, such as test [[ ]] do not work and that means this Bash script will not work. If you want to read into Dash:

https://wiki.ubuntu.com/DashAsBinSh

So either you have to use the full bash command 'bash dag somedomain.com' or you can change the sh symlink back to bash:

To see if your running dash run:

ls -al /bin/sh

To change the symlink for sh back to bash:

sudo rm /bin/sh

sudo ln -s /bin/bash /bin/sh
