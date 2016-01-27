from twitter import *
import sys
import datetime

def tweet():
	t = Twitter(auth=OAuth(token, token_key, con_secret_key, con_secret))
	dm = datetime.datetime.now().strftime('%x %H:%M:%S') + " Help!!!"
	t.direct_messages.new(user="scalene", text=dm)
	#t.direct_messages.new(user="bioemformatics", text=dm)
	t.direct_messages.new(user="pathogenomenick", text=dm)
	t.direct_messages.new(user="robot_alerts", text=dm)
	t.direct_messages.new(user="masonry_stoves", text=dm)
	t.direct_messages.new(user="DrTimothyWells", text=dm)
	print 'Sent direct message... %s' %dm

if __name__ == '__main__':
	tweet()
