import serial
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
ser = serial.Serial("/dev/ttyACM0")


@app.route("/aq")
def aq_route():
    ok = False
    while not ok:
        line = ser.readline().decode("utf-8")
        if not line: continue
        aq = line.split(":")[1]
        if aq: ok = True
        return aq
    
@app.route("/")
def index():
    data = get_data()
    return "\n".join(data)

def get_data():
    data = []
    while len(data) <= 50:
        entry = ser.readline()
        entry = fmt_data(entry)
        if entry:
            data.append(entry)
    return data
def fmt_data(entry):
    entry = entry.decode("utf-8")
    entry.replace("\n", "")
    items = entry.split(",")

    type = items[0]
    if type == 'beacon':
        fmtstr = "Type: Beacon\t SSID: {}\t MAC: {}\t Channel# {}\t Signal Strength: {}\n".format(items[1], items[2], items[3], items[4])
    elif type == 'client':
        fmtstr = "Type: Client\t MAC: {}\t WAP: {}\t MAC Dest: {}\t RSSI: {}\t Signal Strength: {}\n".format(items[1], items[2], items[3], items[4], items[5])
    else:
        return None
    return "<p> {} </p>".format(fmtstr)
        
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

    
