# coding: utf-8

import os

base_path = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    import sys
    sys.path.append(
        os.path.join(base_path, '../..')
    )


from tests import BaseTestCase
from app.image_processing.utils import reverse_gif


class ImageProcessingUtilsTestCase(BaseTestCase):

    def test_reverse_gif_util(self):
        image_path = os.path.join(base_path, './pikachu.gif')
        reverse_gif(image_path)
        image_path = os.path.join(base_path, './handshake.gif')
        reverse_gif(image_path)


if __name__ == '__main__':
    import unittest
    unittest.main()
