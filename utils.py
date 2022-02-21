class ThirdPartyError(Exception):
    message = "Error. Try again later."


class IncorrectArgType(Exception):
    message = "Error. You should use correct type."


class ConfigNoutFound(Exception):
    message = "Error. You should create config firstly."


class InvalidAwsKey(Exception):
    message = "Error. You should use correct AWS keys."
