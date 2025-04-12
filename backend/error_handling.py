import logging
import traceback
import os

# Ensure the logs directory exists
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
os.makedirs(log_dir, exist_ok=True)

# Configure logger
logging.basicConfig(
    filename=os.path.join(log_dir, 'error.log'),
    level=logging.ERROR,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

def log_exception(e, context=""):
    """
    Logs an exception with optional context.
    """
    logging.error(f"{context} | {type(e).__name__}: {e}")
    traceback.print_exc()

def handle_api_error(response):
    """
    Handles errors returned from an API call.
    Returns a meaningful message if an error is detected.
    """
    if not response.ok:
        try:
            error_info = response.json()
        except Exception:
            error_info = response.text
        logging.error(f"API Error: {response.status_code} - {error_info}")
        return f"API Error {response.status_code}: {error_info}"
    return None
