import logging
import hipchat


class HipChat(object):

    def __init__(self, admin_token, default_room):
        self.api = hipchat.HipChat(token=admin_token)
        self.default_room = default_room
        self.room_ids_cache = {}

    def find_room_id(self, name):
        room_id = self.room_ids_cache.get(name)
        if not room_id:
            room_id = self.api.find_room('Pastebin')['room_id']
            self.room_ids_cache[name] = room_id
        return room_id

    def send_message(self, message, sender='log', color='yellow', room=None):
        if not room:
            room = self.default_room
        response = self.api.method(
            'rooms/message',
            method='POST',
            parameters={
                'room_id': self.find_room_id(room),
                'from': sender,
                'color': color,
                'message': message
            }
        )


class HipChatHandler(logging.Handler):

    def __init__(self, admin_token, room, sender=''):
        logging.Handler.__init__(self)
        self.sender = sender
        self.api = HipChat(admin_token, room)

    def emit(self, record):
        self.api.send_message(
            self.format(record),
            sender='-'.join([n for n in [self.sender, record.levelname] if n]),
            color=self.__color_for_level(record.levelno)
        )

    def __color_for_level(self, levelno):
        if levelno > logging.WARNING:
            return 'red'
        if levelno == logging.WARNING:
            return 'yellow'
        if levelno == logging.INFO:
            return 'green'
        if levelno == logging.DEBUG:
            return 'gray'
        return 'purple'
