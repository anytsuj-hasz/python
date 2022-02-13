class Result():

    def __init__(self, message, value=None):
        self.isSucces = None
        self.message = message
        self.value = value

    def is_ok(self):
        return self.isSucces


class Ok(Result):

    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.isSucces = True


class Error(Result):

    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.isSucces = False
  