python3 ~/code/bookmark-manager/bm/manage.py runserver 0.0.0.0:9000 >> ~/bmlogs 2>&1 &
python3 ~/scripts/notifier.py &

# Activate venv for clouder-lite
source ~/code/clouder-lite/venv/bin/activate
python3 ~/code/clouder-lite/server.py me >> ~/cllogs 2>&1 &
deactivate
