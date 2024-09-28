from flask import Flask, request, jsonify

app = Flask(__name__)

# Global variable to store the latest event
latest_event = {"event": None, "timestamp": None}

@app.route('/ifttt_webhook', methods=['POST'])
def ifttt_webhook():
    global latest_event
    try:
        # Get the JSON data sent by IFTTT
        data = request.json
        print(f"Received webhook data: {data}")
        
        # Update the global variable with the latest event
        event_type = data.get('event')
        if event_type == "entered_home":
            print("IFTTT Webhook triggered: You have entered the home geofence.")
            latest_event = {"event": "entered_home", "timestamp":data.get('timestamp')}  # You can use the current time
        elif event_type == "exited_home":
            print("IFTTT Webhook triggered: You have left the home geofence.")
            latest_event = {"event": "left_home", "timestamp": data.get('timestamp')}  # Add a timestamp if needed
        else:
            print("Unknown event.")
        
        # Return success response to IFTTT
        return jsonify({"status": "success"}), 200
    
    except Exception as e:
        print(f"Error processing webhook: {e}")
        return jsonify({"status": "failure"}), 500

# New route to serve the latest event data to the ESP32
@app.route('/latest_event', methods=['GET'])
def get_latest_event():
    global latest_event
    # Return the latest event as JSON
    return jsonify(latest_event), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)

