import subprocess
import webbrowser
import time
import os


def start_app():
    path = './role_auth'
    try:
        os.chdir(path)
        subprocess.Popen(['python', 'manage.py', 'runserver'])
        print("Django server is running....")
    except Exception as e:
        print(f"Error:",str(e))


def open_url():
    url = 'http://localhost:8000/'
    time.sleep(5)
    webbrowser.open(url)
    print(f"Starting app in your default browser...")


if __name__ == '__main__':
    start_app()
    open_url()

