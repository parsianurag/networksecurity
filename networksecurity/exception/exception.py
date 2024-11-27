import sys
from networksecurity.logging.logger import get_logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        # Extract details about the exception
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return (
            "Error occurred in python script name [{0}] line number [{1}] error message [{2}]"
            .format(self.file_name, self.lineno, str(self.error_message))
        )
# networksecurity/logging/logger.py

if __name__ == '__main__':
    # Initialize the logger
    logger = get_logger()

    try:
        logger.info("Enter the try block")
        # Intentionally cause a ZeroDivisionError
        a = 1 / 0
        print("This will not be printed", a)
    except Exception as e:
        # Log the error and raise a custom exception
        logger.error("An error occurred", exc_info=True)
        raise NetworkSecurityException(e, sys)
