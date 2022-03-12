"""
    Consumers
"""
from channels.generic.websocket import WebsocketConsumer

from . import models


class GalleryConsumer(WebsocketConsumer):
    """GalleryConsumer"""

    def connect(self):
        '''connect'''
        models.GALLERYSOCKET = self
        self.accept()

    def disconnect(self, _close_node):
        models.GALLERYSOCKET = None
        '''disconnect'''

    def receive(self, text_data=None, _bytes_data=None):
        '''receive'''
