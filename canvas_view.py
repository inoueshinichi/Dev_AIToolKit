"""画像表示用ビュー
"""
import os
import sys

sys.path.append("/".join([os.getcwd(), 'ui']))
sys.path.append("/".join([os.getcwd(), "aitoolkit"]))

from aitookkit.common import *

class CanvasView(QGraphicsView):

    def __init__(self, parent : Optional[QWidget] = None):
        super().__init__(parent)
        pass
    