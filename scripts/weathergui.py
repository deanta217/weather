import tkinter, requests, json, time
import tkinter as tk
root = tk.Tk()
root.title("Alert Checker")
def showAlert(number):
    alertWindow = tk.Toplevel(root)
    alertWindow.title("Alert " + str(number+1) + " Info")
    Issuer = tk.Label(alertWindow, text='Sent By: ' + alerts.json()['features'][number]['properties']['senderName'])
    Issuer.pack(pady=5)
    Event = tk.Label(alertWindow, text='Event Type: ' + alerts.json()['features'][number]['properties']['event'])
    Event.pack(pady=5)
    Severity = tk.Label(alertWindow, text='Severity: ' + alerts.json()['features'][number]['properties']['severity'])
    Severity.pack(pady=5)
    Description = tk.Label(alertWindow, text=alerts.json()['features'][number]['properties']['description'])
    Description.pack(pady=5)
def listGen():
    global loopnum, varia
    loopnum = 0
    while loopnum <= alertsNum - 1:
        varia = int(loopnum) + 1
        label = tk.Label(root, text='Alert ' + str(varia) + ": " + alerts.json()['features'][loopnum]['properties']['headline'])
        label.pack(pady=5)
        button = tk.Button(root, text='Find more about this Alert.', command=lambda loopnum=loopnum: showAlert(loopnum))
        button.pack(pady=5)
        print("went through" + str(loopnum))
        loopnum = int(loopnum) + 1
def stateChoose():
    global stateEntry, entryInfo, chooseButton
    entryInfo = tk.Label(root, text='Enter your State Abbrevation.')
    entryInfo.pack(pady=5)
    stateEntry = tk.Entry(root)
    stateEntry.pack(pady=5)
    chooseButton = tk.Button(root, text='Submit your state selection.', command=fetchState)
    chooseButton.pack(pady=5)
def fetchState():
    global state, url, alerts
    validStates = {
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME',
    'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA',
    'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'DC', 'PR' }
    state = stateEntry.get().strip().upper()
    if state not in validStates:
        entryInfo.config(text="Please enter a valid 2 letter, state abbrevation.")
        return
    else:
        entryInfo.destroy()
        stateEntry.destroy()
        chooseButton.destroy()
        url = "https://api.weather.gov/alerts/active?area=" + state
        alerts = requests.get(url)
        listSetup()
        listGen()
def listSetup():
    global alertsNum
    alertsNum = len(alerts.json()['features'])
    if alertsNum == 0:
        NoAlerts = tk.Label(root, text='No alerts.')
        NoAlerts.pack(pady=5)
        restart = tk.Button(root, text='Check another state.', command=restartCheck)
        restart.pack(pady=5)
        return
    title = tk.Label(root, text=alerts.json()['title'])
    title.pack(pady=10)
    restart = tk.Button(root, text='Check another state.', command=restartCheck)
    restart.pack(pady=5)
def restartCheck():
    for widget in root.winfo_children():
        widget.destroy()
    stateChoose()
stateChoose()


root.mainloop()