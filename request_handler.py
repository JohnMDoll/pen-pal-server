import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        """translates the request url into a 1 level deep path and attempts to parse id, if any"""
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2, expected to be an id value
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple

    def do_GET(self):
        """Handles GET requests to the server """
        self._set_headers(200)

        response = {}

        # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)

        if resource == "metals":
            if id is None:
                response = get_all_metals()
            else:
                response = get_single_metal(id)
        elif resource == "sizes":
            if id is None:
                response = get_all_sizes()
            else:
                response = get_single_size(id)

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Handles POST requests to the server """
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new things
        new_order = None

        if resource == "orders":
            # new_order = create_order(post_body)
            # Encode the new order and send in response
            self.wfile.write(json.dumps(new_order).encode())

    def do_PUT(self):
        """Handles PUT requests to the server """
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Update a single order from the list
        if resource == "orders":
            # update_order(id, post_body)

        # Encode the new item and send in response
        self.wfile.write("".encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                        'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                        'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_DELETE(self):
        """handles DELETE requests"""
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single entry from the respective list
        if resource == "orders":
            # delete_order(id)

        # Encode the new thing and send in response
        self.wfile.write("".encode())

# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()