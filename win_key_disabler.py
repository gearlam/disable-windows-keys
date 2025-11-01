import sys
import keyboard
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QIcon

class WinKeyDisabler(QMainWindow):
    def __init__(self):
        super().__init__()
        self.is_win_key_disabled = False
        self.win_keys = ['windows', 'left windows', 'right windows', 'command']
        self.initUI()
        
    def initUI(self):
        # 设置窗口属性
        self.setWindowTitle('Win键控制器')
        self.setFixedSize(300, 200)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建布局
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        # 创建标题标签
        title_label = QLabel('Win键控制器')
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont('Arial', 18, QFont.Bold)
        title_label.setFont(title_font)
        layout.addWidget(title_label)
        
        # 创建状态标签
        self.status_label = QLabel('Windows键状态：未禁用')
        self.status_label.setAlignment(Qt.AlignCenter)
        status_font = QFont('Arial', 12)
        self.status_label.setFont(status_font)
        layout.addWidget(self.status_label)
        
        # 创建控制按钮
        self.control_button = QPushButton('禁用Windows键')
        self.control_button.setFixedSize(200, 50)
        button_font = QFont('Arial', 12)
        self.control_button.setFont(button_font)
        self.control_button.clicked.connect(self.toggle_win_key)
        layout.addWidget(self.control_button)
        
        # 设置布局
        central_widget.setLayout(layout)
        
        # 设置样式
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
            QLabel {
                color: #333333;
                margin: 5px;
            }
        """)
        
        # 居中显示窗口
        self.center_window()
        
    def center_window(self):
        """将窗口居中显示"""
        screen = QApplication.desktop().screenGeometry()
        size = self.geometry()
        x = (screen.width() - size.width()) // 2
        y = (screen.height() - size.height()) // 2
        self.move(x, y)
        
    def toggle_win_key(self):
        """切换Windows键的禁用/解锁状态"""
        if not self.is_win_key_disabled:
            # 禁用Windows键
            self.disable_win_key()
        else:
            # 解锁Windows键
            self.enable_win_key()
            
    def disable_win_key(self):
        """禁用Windows键"""
        try:
            # 阻止所有Windows键
            for key in self.win_keys:
                keyboard.block_key(key)
            
            self.is_win_key_disabled = True
            self.status_label.setText('Windows键状态：已禁用')
            self.control_button.setText('解锁Windows键')
            self.control_button.setStyleSheet("""
                QPushButton {
                    background-color: #f44336;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #da190b;
                }
                QPushButton:pressed {
                    background-color: #b71c1c;
                }
            """)
            
        except Exception as e:
            self.status_label.setText(f'禁用失败：{str(e)}')
            
    def enable_win_key(self):
        """解锁Windows键"""
        try:
            # 解除所有Windows键的阻止
            for key in self.win_keys:
                keyboard.unblock_key(key)
            
            self.is_win_key_disabled = False
            self.status_label.setText('Windows键状态：未禁用')
            self.control_button.setText('禁用Windows键')
            self.control_button.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
                QPushButton:pressed {
                    background-color: #3d8b40;
                }
            """)
            
        except Exception as e:
            self.status_label.setText(f'解锁失败：{str(e)}')
            
    def closeEvent(self, event):
        """关闭窗口时确保解锁Windows键"""
        if self.is_win_key_disabled:
            self.enable_win_key()
        event.accept()

def main():
    app = QApplication(sys.argv)
    
    # 设置应用程序图标和样式
    app.setStyle('Fusion')
    
    # 创建主窗口
    window = WinKeyDisabler()
    window.show()
    
    # 运行应用程序
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()