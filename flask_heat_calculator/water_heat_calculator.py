import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                           QHBoxLayout, QLabel, QLineEdit, QPushButton,
                           QComboBox, QMessageBox)
from PyQt6.QtCore import Qt
import numpy as np

class WaterHeatCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("水换热量计算器")
        self.setFixedSize(400, 300)
        
        # 创建中心部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # 流量输入
        flow_layout = QHBoxLayout()
        self.flow_input = QLineEdit()
        self.flow_unit = QComboBox()
        self.flow_unit.addItems(["kg/h", "m³/h"])
        flow_layout.addWidget(QLabel("流量:"))
        flow_layout.addWidget(self.flow_input)
        flow_layout.addWidget(self.flow_unit)
        layout.addLayout(flow_layout)
        
        # 温度输入
        temp_in_layout = QHBoxLayout()
        self.temp_in_input = QLineEdit()
        temp_in_layout.addWidget(QLabel("入口温度 (°C):"))
        temp_in_layout.addWidget(self.temp_in_input)
        layout.addLayout(temp_in_layout)
        
        temp_out_layout = QHBoxLayout()
        self.temp_out_input = QLineEdit()
        temp_out_layout.addWidget(QLabel("出口温度 (°C):"))
        temp_out_layout.addWidget(self.temp_out_input)
        layout.addLayout(temp_out_layout)
        
        # 计算按钮
        calc_button = QPushButton("计算换热量")
        calc_button.clicked.connect(self.calculate_heat)
        layout.addWidget(calc_button)
        
        # 结果显示
        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.result_label)
        
    def get_specific_heat(self, t1, t2):
        """计算给定温度范围内的平均比热容 (kJ/kg·°C)"""
        # 在0-100°C范围内，水的比热容近似值
        temps = np.linspace(min(t1, t2), max(t1, t2), 10)
        specific_heats = []
        
        for t in temps:
            # 使用简化的水比热容计算公式（近似值）
            c = 4.214 - 2.286e-3 * t + 4.991e-5 * t**2 - 4.519e-7 * t**3
            specific_heats.append(c)
            
        return np.mean(specific_heats)
    
    def calculate_heat(self):
        try:
            # 获取输入值
            flow = float(self.flow_input.text())
            t_in = float(self.temp_in_input.text())
            t_out = float(self.temp_out_input.text())
            
            # 检查温度范围
            if not (0 <= t_in <= 100 and 0 <= t_out <= 100):
                QMessageBox.warning(self, "警告", "温度必须在0-100°C范围内！")
                return
            
            # 如果输入为m³/h，转换为kg/h（假设水密度为1000kg/m³）
            if self.flow_unit.currentText() == "m³/h":
                flow = flow * 1000
            
            # 计算平均比热容
            c = self.get_specific_heat(t_in, t_out)
            
            # 计算换热量 (kJ/h)
            q = flow * c * abs(t_out - t_in)
            
            # 显示结果
            self.result_label.setText(f"换热量: {q:.2f} kJ/h\n"
                                   f"({q/3600:.2f} kW)\n"
                                   f"平均比热容: {c:.4f} kJ/(kg·°C)")
            
        except ValueError:
            QMessageBox.warning(self, "错误", "请输入有效的数值！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"计算出错：{str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WaterHeatCalculator()
    window.show()
    sys.exit(app.exec()) 