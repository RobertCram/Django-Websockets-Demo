"""
    Demo Models
"""
import time
import json
import random

GALLERYSOCKET = None

class PictureGenerator:
    """
        PictureGenerator
    """

    def __init__(self):
        '''init'''
        self.images_generated = 0

    def generate(self, number_of_pics, batchnumber):
        '''generate'''
        for _ in range(0, number_of_pics):
            url = 'https://picsum.photos/400/600?id=' + str(random.randint(1, 1000))
            description = f'Server Image #{batchnumber}-{self.images_generated+1}'
            picture = { 'src': url, 'desc': description }
            if GALLERYSOCKET is None:
                print(f'Websocket UNAVAILABLE - #{__file__}')
                break
            GALLERYSOCKET.send(text_data=json.dumps(picture))
            self.images_generated += 1
            time.sleep(1)
