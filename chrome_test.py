import pychrome
import os
import base64
import time
#google-chrome --headless --disable-gpu --remote-debugging-port=9222
os.system("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe --headless --disable-gpu --remote-debugging-port=9222")

# create a browser instance
browser = pychrome.Browser(url="http://127.0.0.1:9222")

# create a tab
tab = browser.new_tab()

# register callback if you want
def request_will_be_sent(**kwargs):
    print("loading: %s" % kwargs.get('request').get('url'))

tab.Network.requestWillBeSent = request_will_be_sent

# start the tab
tab.start()

# call method
tab.Network.enable()
# call method with timeout
tab.Page.navigate(url="https://github.com/fate0/pychrome", _timeout=5)

# wait for loading
tab.wait(5)
data  = tab.Page.captureScreenshot()
with open("%s.png" % time.time(), "wb") as fd:
    fd.write(base64.b64decode(data['data']))
# stop the tab (stop handle events and stop recv message from chrome)
tab.stop()

# close tab
browser.close_tab(tab)