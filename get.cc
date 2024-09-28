#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "your-SSID";
const char* password = "your-PASSWORD";
const char* serverName = "http://140.238.145.138:5000/latest_event";

void setup() {
  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  // Check if connected to WiFi
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    
    // Make the GET request to the Flask server
    http.begin(serverName);
    int httpResponseCode = http.GET();
    
    if (httpResponseCode > 0) {
      // Parse the response
      String response = http.getString();
      Serial.println("Received response from Flask:");
      Serial.println(response);

      // Here you can process the response and take action based on the event
    } else {
      Serial.print("Error in GET request: ");
      Serial.println(httpResponseCode);
    }
    
    http.end();  // Free resources
  }

  delay(1000);  // Wait for 1 seconds before the next request
}

