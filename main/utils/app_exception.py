class AppException(Exception):
    def __init__(self, message, data, status_code):
        self.body = {'message': message}
        if data is not None:
            self.body['data'] = data
        self.status_code = status_code

    def __str__(self):
        return self.body['message']