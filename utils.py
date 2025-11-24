import time

def timestamp_now():
    """Return current timestamp as string."""
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())