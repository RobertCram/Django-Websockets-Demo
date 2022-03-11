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
        self.images_generated = 0
        self.websocket = websocket

    def generate(self, number_of_pics, batchnumber):
        '''generate'''
        for _ in range(0, number_of_pics):
            url = 'https://picsum.photos/400/600?id=' + str(random.randint(1, 1000))
            description = f'Server Image #{batchnumber}-{self.images_generated+1}'
            picture = { 'src': url, 'desc': description }
            self.websocket.send(text_data=json.dumps(picture))
            self.images_generated += 1
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
        self.generator.generate(data_json['images'], data_json['batchnumber'])
