# Utility for printing user and timestamp in plots

def get_user():
    import os
    return os.environ['USER']
    
def get_timestamp():
    import time
    return time.strftime('%Y-%m-%d')