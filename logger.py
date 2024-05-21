import logging

class AppLogger:
    def __init__(self, filename='application.log', filemode='a', level=logging.WARNING):
        """
        Initialize the logger with a specific file and configuration.
        """
        logging.basicConfig(
            filename=filename,  # Log file path
            filemode=filemode,  # Append mode; use 'w' to overwrite each time instead
            level=level,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def info(self, msg):
        """
        Log an informational message.
        """
        logging.info(msg)

    def debug(self, msg):
        """
        Log an debug message.
        """
        logging.debug(msg)

    def warning(self, msg):
        """
        Log a warning message.
        """
        logging.warning(msg)

    def error(self, msg):
        """
        Log an error message.
        """
        logging.error(msg)
