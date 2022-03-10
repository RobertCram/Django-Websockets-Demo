"""
    Demo Models
"""
import time
import json
import random
from channels.generic.websocket import WebsocketConsumer

class PictureGenerator:
    """
        PictureGenerator
    """

    def __init__(self, websocket):
        '''init'''
        self.imagesGenerated = 0
        self.websocket = websocket

    def generate(self, number_of_pics):
        '''generate'''
        for i in range(0, number_of_pics):
            url = 'https://picsum.photos/400/600?id=' + str(random.randint(1, 1000))
            description = f'Server Image #{self.imagesGenerated+1}'
            picture = { 'src': url, 'desc': description }
            self.websocket.send(text_data=json.dumps(picture))
            self.imagesGenerated += 1
            time.sleep(1)


class GalleryConsumer(WebsocketConsumer):
    """GalleryConsumer"""

    def __init__(self):
        super().__init__()
        self.generator = None

    def connect(self):
        '''connect'''
        self.generator = PictureGenerator(self)
        self.accept()

    def disconnect(self, _close_node):
        '''disconnect'''
        self.generator = None

    def receive(self, text_data=None, _bytes_data=None):
        '''receive'''
        data_json = json.loads(text_data)
        self.generator.generate(data_json['pics'])
