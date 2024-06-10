import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *
class Ex(QMainWindow):
    #constructor
    def __init__(self,parent=None):
        super(Ex,self).__init__(parent)
        #app = QApplication(sys.argv)
        win =QWidget() #for maximize and close btn 
        win.setGeometry(100,100,600,400)
        #setting title
        self.setWindowTitle("ExPlayer")
        #setting Icon
        self.setWindowIcon(QIcon('EXplayerProject/ExPlayericon.png'))
        #media player QtWidget
        self.media_player=QMediaPlayer(None, QMediaPlayer.VideoSurface)
        #video QtWidget
        self.video_player=QVideoWidget()
        #video_player.move(250,80)
        #play pause skip buttons
        self.play_btn=QPushButton()#play btn
        self.play_btn.setIcon(QIcon(QPixmap("EXplayerProject/play_btn.png")))#play image to btn
        self.play_btn.setToolTip("Play")
        self.play_btn.setStatusTip('play')
        self.play_btn.clicked.connect(self.play)
        
        #play_btn.move(50,50)
        #pause btn
        self.pause_btn= QPushButton()
        self.pause_btn.setIcon(QIcon(QPixmap("pause_btn.png")))# pause image to btn
        self.pause_btn.setToolTip("Pause")
        self.pause_btn.setStatusTip('pause')
        
        # Create a widget for window contents
        win = QWidget(self)
        self.setCentralWidget(win)
        #pause_btn.move(100,50)
        self.f_skip= QPushButton(win)# forwar skip btn
        self.f_skip.setIcon(QIcon(QPixmap("EXplayerProject/f_skip_btn.png")))#f_skip image to btn
        self.f_skip.setToolTip("X2")
        self.f_skip.setStatusTip('x2')
        #f_skip.move(150,50)
        self.b_skip= QPushButton(win)#backward skip btn
        self.b_skip.setIcon(QIcon(QPixmap("EXplayerProject/b_skip_btn.png")))#f_skip image to btn
        self.b_skip.setToolTip("X2")
        self.b_skip.setStatusTip('X2')
        #Error Message
        self.error = QLabel()
        self.error.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        
        #seeker bar
        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)
        
        #file to play b_skip_btnopenButton = QPushButton("Open Video") 
        self.file_btn = QPushButton("Browse Video")  
        self.file_btn.setToolTip("Browse Video")
        self.file_btn.setStatusTip("Browse Video")
        self.file_btn.setFixedHeight(24)
        self.file_btn.clicked.connect(self.openFile)
        
        #layouts to add btns 
        buttonsLayout = QHBoxLayout()
        buttonsLayout.setContentsMargins(0, 0, 0, 0)
        #top menu HLayout
        Topmenu=QHBoxLayout()
        #adding file_btn to menu
        Topmenu.addWidget(self.file_btn)
        #slider layout
        sliderLayout=QHBoxLayout()
        #add slider to sliderLayout
        sliderLayout.addWidget(self.positionSlider)
        #video layout
        videolayout=QHBoxLayout()
        videolayout.addWidget(self.video_player)
        #player laout
        playerLayout=QVBoxLayout()
        #playerLayout.setAlignment(Qt.AlignTop|Qt.AlignLeft)
        #adding btns to buttonsLayout
        buttonsLayout.addWidget(self.play_btn)
        buttonsLayout.addWidget(self.pause_btn,1)
        buttonsLayout.addWidget(self.f_skip,2)
        buttonsLayout.addWidget(self.b_skip,3)
        
        
        
        #add sliderLayout and buttonsLayout to playerLayout
        playerLayout.addLayout(Topmenu)
        playerLayout.addStretch()
        playerLayout.addLayout(videolayout,1)
        playerLayout.addStretch()
        playerLayout.addWidget(self.error)
        playerLayout.addLayout(sliderLayout,2)
        playerLayout.addStretch()
        playerLayout.addLayout(buttonsLayout,3)
        
        #setting playerLayout to win
        win.setLayout(playerLayout)
        #media player
        self.media_player.setVideoOutput(self.video_player)
        self.media_player.stateChanged.connect(self.mediaStateChanged)
        self.media_player.positionChanged.connect(self.positionChanged)
        self.media_player.durationChanged.connect(self.durationChanged)
        self.media_player.error.connect(self.handleError)
        
    #functions
    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self,"Select File",QDir.homePath())

        if fileName != '':
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.play_btn.setEnabled(True)

    def exitCall(self):
        sys.exit(self.app.exec_())

    def play(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    def mediaStateChanged(self, state):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.play_btn.setIcon(
                    QIcon(QPixmap("EXplayerProject/pause_btn.png")))
        else:
            self.play_btn.setIcon(
                    QIcon(QPixmap("EXplayerProject/play_btn.png")))

    def positionChanged(self,position):
        self.positionSlider.setValue(position)

    def durationChanged(self,duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self,position):
        self.media_player.setPosition(position)

    def handleError(self):
        self.play_btn.setEnabled(False)
        self.error.setText("Error: " + self.media_player.errorString())
    

    
app = QApplication(sys.argv)
videoplayer = Ex()
videoplayer.resize(640, 480)
videoplayer.show()
sys.exit(app.exec_())