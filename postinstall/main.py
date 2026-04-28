import webview, subprocess, time

if __name__ == '__main__':
    subprocess.Popen(["python", "-m", "http.server", "8000"])
    time.sleep(0.05)
    window = webview.create_window('setup', 'http://localhost:8000')
    webview.start(lambda x: x.toggle_fullscreen(), window)
