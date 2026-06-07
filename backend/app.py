from flask import Flask,request

from services.dns import get_dns_records
from db.init import init_db
from db.ops import create_investigation, get_investigation

app = Flask(__name__)


init_db()
@app.route('/api/investigations/<int:id>', methods=['GET'])
def handle_get(id):
    return get_investigation(id)

@app.route('/api/investigations', methods=['POST'])
def handle_post():
    data=request.get_json
    target=data.get('target')
    return create_investigation(target)

@app.route('/api/')
def home():
    return {'hello':'world'}
if __name__ == "__main__":
    app.run(debug=True)