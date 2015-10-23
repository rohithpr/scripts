import threading
import time
import Tkinter
import tkMessageBox
import transmissionrpc

SHUTDOWN = True # Set to False if user clicks on Cancel

def show_message_box():
    global SHUTDOWN
    temp = Tkinter.Tk()
    temp.withdraw()
    SHUTDOWN = tkMessageBox.askokcancel(
            title="All torrents downloaded", 
            message="Computer is about to be shutdown.\
             Press cancel to abort!")
    return

def get_download_status():
    tc = transmissionrpc.Client('localhost', port=9091)
    torrents = tc.get_torrents()
    for torrent in torrents:
        if torrent.status == 'downloading':
            return False
    return True

def main():
    all_done = get_download_status()
    if not all_done: # Shutdown
        t = threading.Thread(target=show_message_box)
        t.start()
        time.sleep(3)
        return SHUTDOWN
    else: # Don't shutdown
        return not SHUTDOWN

if __name__ == '__main__':
    action = main()
    print action
