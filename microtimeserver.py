from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime
from zoneinfo import ZoneInfo


# Define the request handler class
class TimeServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/time":
            # Get the current time
            current_time = datetime.now(tz=ZoneInfo("Europe/Amsterdam"))

            # Prepare the JSON response
            response = {
                "current_time": current_time.isoformat(),
                "date": current_time.strftime("%Y-%m-%d"),
                "time": current_time.strftime("%H:%M:%S"),
                "offset": current_time.strftime("%z"),
                "timezone": current_time.strftime("%Z"),
                "timestamp": current_time.timestamp(),
            }

            # Send response status code
            self.send_response(200)

            # Send headers
            self.send_header("Content-type", "application/json")
            self.end_headers()

            # echo the JSON response on stdout
            print(json.dumps(response))

            # Send the JSON response
            self.wfile.write(json.dumps(response).encode())
        else:
            # Send 404 for other paths
            self.send_response(404)
            self.end_headers()


# Set up the server
def run_server():
    port = 54321
    server_address = ("", port)
    httpd = HTTPServer(server_address, TimeServer)
    print(f"Server running on port {port}...")
    httpd.serve_forever()


# Run the server
if __name__ == "__main__":
    run_server()
