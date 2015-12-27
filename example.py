import os
import logging
import hiplogging

# Set up a standard logger
logger = logging.getLogger('hipchat')
logger.setLevel(logging.DEBUG)
# Add the standard logging to stderr
logger.addHandler(logging.StreamHandler())

# Add the hipchat handler
# Get an access token from: https://<YOUR_HIPCHAT_NAME>.hipchat.com/admin/api
handler = hiplogging.HipChatHandler(os.environ['HIPCHAT_ACCESS_TOKEN'],
                                    os.environ['HIPCHAT_ROOM'])
# Additionally, you can add an optional third argument `environment`, if your
# host your HipChat server.
# i.e.: https//hipchat.yourdomain.com
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

# Try it out: messages will be visible both in the console and on hipchat.
logger.debug('debug - we are approaching the anomaly')
logger.info('info - shields up, red alert!')
logger.warn('warn - shield down to 15%')
logger.fatal('fatal - what shields?')

# You can set your own colors and the sender name using extra with logging.log.
# Valid colors are ["purple", "gray", "green", "yellow", "red"]
# The first argument is the log level:
#    https://docs.python.org/2/library/logging.html#logging-levels
#    https://docs.python.org/2/library/logging.html#logging.log
logger.log(20, "Another message", extra={'color':'purple', "sender":"FOOBAR"})
