import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidget, QVBoxLayout, QPushButton, QWidget
from pygame import mixer

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.playlist = QListWidget()
        self.load_button = QPushButton('Load Playlist')
        self.play_button = QPushButton('Play')
        self.stop_button = QPushButton('Stop')

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        layout.addWidget(self.playlist)
        layout.addWidget(self.load_button)
        layout.addWidget(self.play_button)
        layout.addWidget(self.stop_button)

        self.setCentralWidget(central_widget)

        self.load_button.clicked.connect(self.load_playlist)
        self.play_button.clicked.connect(self.play_music)
        self.stop_button.clicked.connect(self.stop_music)

        self.playlist.itemDoubleClicked.connect(self.play_selected)

        self.setWindowTitle('Simple Music Player')
        self.setGeometry(100, 100, 400, 300)

    def load_playlist(self):
        file_dialog = QFileDialog()
        files, _ = file_dialog.getOpenFileNames(self, 'Select Music Files', '', 'Audio Files (*.mp3 *.wav)')
        
        if files:
            self.playlist.addItems(files)

    def play_music(self):
        current_item = self.playlist.currentItem()
        if current_item:
            file_path = current_item.text()
            mixer.init()
            mixer.music.load(file_path)
            mixer.music.play()

    def stop_music(self):
        mixer.music.stop()

    def play_selected(self, item):
        self.playlist.setCurrentItem(item)
        self.play_music()


if __name__ == '__main__':
    app = QApplication([])
    window = MusicPlayer()
    window.show()
    app.exec_()
