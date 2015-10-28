python3 ~/code/bookmark-manager/bm/manage.py runserver 0.0.0.0:9000 >> ~/bmlogs 2>&1 &
python3 ~/code/scripts/notifier.py &

# Activate venv for clouder-lite
cd ~/code/clouder-lite
source venv/bin/activate
python3 server.py me >> ~/cllogs 2>&1 &
deactivate
cd ~
