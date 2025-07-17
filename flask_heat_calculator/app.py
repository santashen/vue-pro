from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

def get_specific_heat(t1, t2):
    """计算给定温度范围内的平均比热容 (kJ/kg·°C)"""
    temps = np.linspace(min(t1, t2), max(t1, t2), 10)
    specific_heats = []
    for t in temps:
        c = 4.214 - 2.286e-3 * t + 4.991e-5 * t**2 - 4.519e-7 * t**3
        specific_heats.append(c)
    return np.mean(specific_heats)

@app.route('/toy/heat/')
def index():
    return render_template('index.html')

@app.route('/toy/heat/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        flow = float(data['flow'])
        t_in = float(data['t_in'])
        t_out = float(data['t_out'])
        flow_unit = data['flow_unit']

        if not (0 <= t_in <= 100 and 0 <= t_out <= 100):
            return jsonify({'error': '温度必须在0-100°C范围内！'}), 400

        if flow_unit == "m³/h":
            flow_kgh = flow * 1000
            flow_m3h = flow
            flow_lmin = flow * 1000 / 60
        elif flow_unit == "L/min":
            flow_kgh = flow * 60
            flow_m3h = flow * 60 / 1000
            flow_lmin = flow
        else:  # kg/h
            flow_kgh = flow
            flow_m3h = flow / 1000
            flow_lmin = flow / 60

        c = get_specific_heat(t_in, t_out)
        q = flow_kgh * c * abs(t_out - t_in)  # kJ/h

        return jsonify({
            'heat': round(q, 2),
            'heat_kw': round(q / 3600, 2),
            'heat_w': round(q * 1000 / 3600, 2),
            'specific_heat': round(c, 4),
            'flow_kgh': round(flow_kgh, 2),
            'flow_m3h': round(flow_m3h, 3),
            'flow_lmin': round(flow_lmin, 2),
            'input_flow': round(flow, 3),
            'input_unit': flow_unit,
            't_in': t_in,
            't_out': t_out
        })

    except ValueError:
        return jsonify({'error': '请输入有效的数值！'}), 400
    except Exception as e:
        return jsonify({'error': f'计算出错：{str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
