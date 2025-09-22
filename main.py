import sys, json, csv, """jpeg,""" os
from dataclasses import dataclass, asdict
from typing import List, Dict

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QStackedWidget, QToolBar, QStatusBar,
    QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QLineEdit,
    QFormLayout, QDialog, QDialogButtonBox, QMessageBox, QFileDialog, QSpinBox,
    QAbstractItemView, QFrame
)

# App title and files
APP_TITLE = "My Art Collections"
DATA_FILE = "art_collec.json"

""" SETS """
@dataclass
class Comics:
  title: str
  year: int
  """ Comming soon:
  medium: str #paper, pen/pencil/marker
  artist: str
  """
  
@dataclass
class Doodle:
   title: str
   year: int
   """ Comming soon:
   medium: str #paper, pen/pencil/marker
   artist: str
   """
# Comic Pictures
class ComicPics(QDialog)
