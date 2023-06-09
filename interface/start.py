from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


current_position = [0,0]
target_position = [0,0]

@app.route('/')
def home():
    return render_template('index.html', current_position=current_position, target_position=target_position)

@app.route('/marker', methods=['POST'])
def receive_marker():
    location = request.get_json()
    latitude = location['lat']
    longitude = location['lng']
    global target_position
    target_position = [latitude, longitude]
    return jsonify(success=True, target_position=target_position)

if __name__ == '__main__':
    app.run()
