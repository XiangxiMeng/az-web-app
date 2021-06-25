#!/usr/bin/env bash

cat >/etc/motd <<EOL

  _____
  /  _  \ __________ _________   ____
 /  /_\  \\___   /  |  \_  __ \_/ __ \
/    |    \/    /|  |  /|  | \/\  ___/
\____|__  /_____ \____/ |__|    \___  >
        \/      \/                  \/

A P P   S E R V I C E   O N   L I N U X

Documentation: http://aka.ms/webapp-linux

EOL
cat /etc/motd

sed -i "s/SSH_PORT/$SSH_PORT/g" /etc/ssh/sshd_config
service ssh start

# Get environment variables to show up in SSH session
eval $(printenv | sed -n "s/^\([^=]\+\)=\(.*\)$/export \1=\2/p" | sed 's/"/\\\"/g' | sed '/=/s//="/' | sed 's/$/"/' >> /etc/profile)

# Start Flask app
gunicorn -t 120 -w 3 -b 0.0.0.0:8000 --chdir=/src --log-level debug application:app
