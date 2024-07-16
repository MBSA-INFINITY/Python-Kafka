from flask import Flask, render_template, request
from flask_sse import sse

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/push', methods=['POST'])
def publish_message():
    json_data = dict(request.json)
    message = json_data.get("message")
    sse.publish({"message": message}, type='greeting')
    return "Message sent!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)