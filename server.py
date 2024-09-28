from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ifttt_webhook', methods=['POST'])
def ifttt_webhook():
    data = request.json
    event_type = data.get('event')
    if event_type == "entered_home":
        # Logic for when phone enters the home geofence
        print("Phone entered home")
    elif event_type == "left_home":
        # Logic for when phone leaves the home geofence
        print("Phone left home")
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True)
