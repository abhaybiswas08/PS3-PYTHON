import os

import webbrowser

print("Enter the App You Want to Open: ")

app_name = input()

if (app_name == "browser"):
	webbrowser.open_new_tab("www.google.com")
elif (app_name == "spotify"):
	webbrowser.open_new_tab("www.spotify.com")
else:
	print("Nothing is Opened.....")
