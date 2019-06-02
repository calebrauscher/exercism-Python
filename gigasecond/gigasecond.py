from datetime import timedelta

def add_gigasecond(moment):
    ''' Find the time a person turns 1 gigasecond old. '''
    gigasecond = timedelta(seconds=10**9)
    return gigasecond + moment
