__author__ = 'caidong'

from birdy.twitter import UserClient, StreamClient

CONSUMER_KEY = 'G71DbvCIrrD7f5hjsIQMVFjn8'
CONSUMER_SECRET = 'X64HC5My9hNlF8wpnfpx5SlimpT0YgOk5n56GA8uzPgjaj4ocI'
ACCESS_TOKEN = '3125121605-trXm6IncsWccIkIOzbH2iZHzcrGlXKaMQplpsTM'
ACCESS_TOKEN_SECRET = 'H4aZoMobjQWgddZwcrY03zq9kJOFgcynE9etrsL7mQFqB'

client = UserClient(CONSUMER_KEY,
                    CONSUMER_SECRET,
                    ACCESS_TOKEN,
                    ACCESS_TOKEN_SECRET)

#response = client.api.users.show.get(screen_name='twitter')
#print response.data

#print


# stream = StreamClient(CONSUMER_KEY,
#                       CONSUMER_SECRET,
#                       ACCESS_TOKEN,
#                       ACCESS_TOKEN_SECRET)
# stream.
#
# client.api

response = client.api.statuses.update.post(
	status='@TobiasRijken - yr train [19:14 YRK-WAT] delayed by 13 minutes (69% chance). Enjoy a free wifi voucher while waiting: https://pbs.twimg.com/media/CBRNlC4WcAEhzxU.png:large')

#
# print response.data
print


