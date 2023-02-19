"""共通ライブラリ
"""

import os
import sys
import time
import datetime as dt
import re
import math
import glob
import pathlib
import shutil
import ctypes
import platform
import abc
import functools
import inspect
import threading
import copy
import json
import csv



from collections import (
    deque,
    Counter,
    defaultdict,
    OrderedDict,
    ChainMap,
)

import numpy as np
np.set_printoptions(suppress=True) # 指数表記を禁止

import scipy as sp
import cv2
import PIL
import pandas as pd
import tqdm
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import qimage2ndarray as qn;
import openpyxl


"""モジュールの読み込み
"""

sys.path.append("/".join([os.getcwd(), "internal"]))
from internal.type_def import *   # typingによる型ヒント
from internal.qt_pyside2 import * # Qt
from internal.pytorch import *    # Pytorch 

sys.path.append("/".join([os.getcwd(), "camera"]))
from camera.thread_camera_controller import *
from camera.thread_camera_frame_reader import *




