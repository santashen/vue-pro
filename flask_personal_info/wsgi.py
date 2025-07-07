import os
from app import create_app, db
from app.models import PersonInfo

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'PersonInfo': PersonInfo}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002) 