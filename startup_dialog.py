
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'ui'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'aitoolkit'))

from aitoolkit.type_def import *
from aitoolkit.common import *
from aitoolkit.qt_pyside2 import *

from ui.ui_startup_dialog import Ui_StartupDialog

from dl_traning_window import DlTrainingWindow

class StartupDialog(QDialog):

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)

        # UI
        self.ui: Any = Ui_StartupDialog()
        self.ui.setupUi(self)

        # DL/RL
        self.dl_window: Optional[Any] = None
        self.rl_window: Optional[Any] = None

        # Signal/Slot
        # self._toolbar_connection()
        # self._menubar_connection()
        self._ui_connection()
        # self._custom_connection()

    def _toolbar_connection(self) -> None:
        """
        ToolBarに関するSignal/Slotの接続
        :return:
        """
        raise NotImplementedError("ToolBarに関するSignal/Slotの接続")
        

    def _menubar_connection(self) -> None:
        """
        MenuBarに関するSignal/Slotの接続
        :return:
        """
        raise NotImplementedError("MenuBarに関するSignal/Slotの接続")

    def _ui_connection(self) -> None:
        """
        UIに関するSignal/Slotの接続
        :return:
        """
        # raise NotImplementedError("UIに関するSignal/Slotの接続")

        # DL
        self.ui.pushButton_DeepLearning.clicked.connect(self.display_dl_window)

    def _custom_connection(self) -> None:
        """
        ユーザー定義のカスタムSignal/Slotの接続
        :return:
        """
        raise NotImplementedError("ユーザー定義のカスタムSignal/Slotの接続")

    def display_dl_window(self):
        self.dl_window = DlTrainingWindow(self)
        self.dl_window.show()
        self.hide()

    