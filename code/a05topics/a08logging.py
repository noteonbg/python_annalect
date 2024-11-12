import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum severity level to DEBUG
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.FileHandler("app.log")  # Log to a file
    ]
)

# Example of logging messages with different severity levels
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# Custom loggers and more detailed configuration
logger = logging.getLogger('my_custom_logger')
logger.setLevel(logging.WARNING)

# Log using the custom logger
logger.debug("This message will not show, as the level is set to WARNING")
logger.warning("This is a warning message from the custom logger")

"""
Logging Levels:

DEBUG: Detailed, diagnostic information, generally only useful for developers.
INFO: Regular operational information, such as the flow of the application.
WARNING: Indicates a potential problem or something unusual that might require attention.
ERROR: A more serious issue that has affected the program’s functionality.
CRITICAL: A very serious error that likely causes the program to terminate.
Log Handlers:

StreamHandler: Sends logs to the console.
FileHandler: Sends logs to a file, which is great for persistent log storage.
Custom Loggers: You can create separate loggers for different parts of your application to control logging behavior more precisely.
"""