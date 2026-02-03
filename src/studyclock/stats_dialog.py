from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout

from .util import format_hm


class StatsDialog(QDialog):
    def __init__(
        self, parent, focus_work_sec: int, paused_sec: int,
        microbreak_sec: int, total_open_sec: int
        ):
        super().__init__(parent)
        self.setWindowTitle("statistics")
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        total = max(1, int(total_open_sec))
        eff = int(round((int(focus_work_sec) / total) * 100))

        text = (
            f"Focus Active: {format_hm(focus_work_sec)}\n"
            f"Paused: {format_hm(paused_sec)}\n"
            f"Screen Break: {format_hm(microbreak_sec)}\n"
            f"\nEfficiency: {eff}%"
        )

        lbl = QLabel(text)
        lbl.setFont(QFont("Segoe UI", 10))
        lbl.setStyleSheet("color: #eee;")

        btns = QDialogButtonBox(QDialogButtonBox.Ok)
        btns.accepted.connect(self.accept)

        lay = QVBoxLayout(self)
        lay.addWidget(lbl)
        lay.addWidget(btns)
