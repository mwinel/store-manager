from flask import jsonify, request


class RequestError:
    """
    This class defines a way to handle request exceptions.
    HTTP status codes must be provided when returning responses.
    """

    message = {
        'error_message': "{0}, '{1}'"
    }

    def not_found(self, error):
        """
        Returns a formatted 404 NOT FOUND error message.
        """
        return jsonify({"error": RequestError.message['error_message'].format(
            "404 Not Found: The requested URL was not found on the server",
            request.url
        )}), 404

    def method_not_allowed(self, error):
        """
        Returns a formatted 405 METHOD NOT ALLOWED message.
        """
        return jsonify({"error": RequestError.message['error_message'].format(
            error, request.url
        )}), 405
