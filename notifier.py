import notify2
import time

notify2.init('20 minute reminder')
messages = ['20', '40', '60']

while True:
    for i in range(3):
        time.sleep(20*60)
        n = notify2.Notification(messages[i], '')
        n.show()
