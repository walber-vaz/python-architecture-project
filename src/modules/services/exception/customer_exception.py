class EmailAlreadyExists(Exception):
    def __init__(self, message: str = "Email already exists"):
        super().__init__(message)
