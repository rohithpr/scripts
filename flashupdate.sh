#!/bin/sh
# Yes, it's for 64 bit!
sudo apt-get update
sudo apt-get purge adobe-flash{plugin,-properties-gtk}
sudo apt-get install adobe-flashplugin