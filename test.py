import datetime

def get_epoch_time(time_string):
	utc=datetime.datetime.strptime(time_string, "%Y-%m-%d")
	return (utc-datetime.datetime(1970, 1, 1)).total_seconds()