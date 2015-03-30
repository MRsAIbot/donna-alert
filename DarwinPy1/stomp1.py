
import stomp, gzip, StringIO, xml

class MyListener(object):
	#
	# def __init__ (self, conn):
	# 	self._conn = conn

	def on_error(self, headers, message):
		print('received an error %s' % message)

	def on_message(self, headers, message):
		fp = gzip.GzipFile(fileobj = StringIO.StringIO(message))
		text = fp.readlines()
		fp.close()
		print('%s\n' % text)

	#	self._conn.ack(id=headers['message-id'], subscription=headers['subscription'])

conn = stomp.Connection([('datafeeds.nationalrail.co.uk', 61613)])

conn.set_listener('', MyListener())
conn.start()
conn.connect(username = 'd3user', passcode = 'd3password', wait=False)

conn.subscribe(destination='/queue/D35526ffe7-39ee-45ef-b7a3-84f956568dcc', id=1, ack='auto')

#conn.send(body=' '.join(sys.argv[1:]), destination='')

mydata = raw_input('Prompt :')

conn.disconnect()











# http://nrodwiki.rockshore.net/index.php/Python_Examples
# # !/usr/bin/env python
#
# import logging
# from time import sleep
#
# import stomp
#
# NETWORK_RAIL_AUTH = ('username', 'password')
#
#
# class Listener(object):
# 	def __init__(self, mq):
# 		self._mq = mq
#
# 	def on_message(self, headers, message):
# 		print headers
# 		print message
# 		self._mq.ack(id=headers['message-id'], subscription=headers['subscription'])
#
#
# mq = stomp.Connection(host_and_ports=[('datafeeds.networkrail.co.uk', 61618)],
#                       keepalive=True,
#                       vhost='datafeeds.networkrail.co.uk',
#                       heartbeats=(10000, 5000))
#
# mq.set_listener(, Listener(mq))
#
# mq.start()
# mq.connect(username=NETWORK_RAIL_AUTH[0],
#            passcode=NETWORK_RAIL_AUTH[1],
#            wait=True)
#
# mq.subscribe('/topic/VSTP_ALL', 'test-vstp', ack='client-individual')
#
# while mq.is_connected():
# 	sleep(1)