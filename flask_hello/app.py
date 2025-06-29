from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Flask Hello</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .container {
                text-align: center;
                background: white;
                padding: 3rem;
                border-radius: 20px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                max-width: 400px;
            }
            h1 {
                color: #333;
                font-size: 3rem;
                margin: 0;
                margin-bottom: 1rem;
            }
            p {
                color: #666;
                font-size: 1.2rem;
                margin: 0;
            }
            .emoji {
                font-size: 4rem;
                margin-bottom: 1rem;
                display: block;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <span class="emoji">🌸</span>
            <h1>Hello, Flask!</h1>
            <p>最小可运行 Flask 页面</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 