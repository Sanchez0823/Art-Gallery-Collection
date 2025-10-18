import sys, json, csv, png, os
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
APP_TITLE = "My Art Collection"
DATA_FILE = "art_collections.json"

""" SETS """
@dataclass
class Comic:
  title: str
  year: int
  num_panels: int
  
@dataclass
class Doodle:
   title: str
   year: int
   medium: str #paper, pen/pencil/marker

class Painting:
    title: str
    year: int
    area: int

# Comic Pictures
class ComicDialogue(QDialog):
    def __init__(self, parent=None, comic: Comic):
        super().__init__(parent)
        self.setWindowTitle("My Art Collection")
        self.setMinimumWidth(400)
        self.title = QLineEdit()
        self.year = QLineEdit()
        self.num_panels = QLineEdit()
        if comic:
            self.title.setText(comic.title)
            self.year.setText(comic.year)
            self.num_panels.setText(comic.num_panels)

        form = QFormLayout()
        form.addRow("Title*", self.title)
        form.addRow("Year*", self.year)
        form.addRow("Num Panels", self.num_panels)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        lay = QVBoxLayout(self)
        lay.addLayout(form)
        lay.addWidget(buttons)

    def get_details(self) -> dict:
        return {"title": self.title.text().strip(),
                "year": self.year.text().strip(),
                "num_panels": self.num_panels.text().strip(),}

    # class DoodleDialog(QDialog):

