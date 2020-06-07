from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask('server')
CORS(app)
app.config['SECRET_KEY'] = '199624f47e49f3fb1e3f66484f4f7814'


@app.route('/')
@app.route('/home')
def home():
    return "Server Home"


'''
# Rooms Part
'''

rooms = [{
    'id': i,
    'haveCheckIn': False,
    'name': '',
    'idCard': '',
    'checkInDate': '',
    'cost': 0,
    'expectTemp': 25,
    'speed': 'Low',
    'temp': 'Server says it is 23',
    'power': False,
    '_showDetails': False,
} for i in range(10)]

# 一个预入住的顾客，以便直接登录
rooms[3] = {
    'id': 3,
    'haveCheckIn': True,
    'name': 'Jon Snow',
    'idCard': '8',
    'checkInDate': '2000-01-01',
    'cost': 233,
    'expectTemp': 25,
    'speed': 'High',
    'temp': 30,
    'power': False,
}


@app.route('/rooms/')
def rooms_page():
    return jsonify(rooms)


@app.route('/rooms/checkIn', methods=['POST'])
def checkIn():
    room = request.get_json(force=True)
    print(room)
    id = room['id']
    rooms[id] = room
    rooms[id]['haveCheckIn'] = True
    rooms[id]['checkInDate'] = 'nowDate() in python'
    rooms[id]['cost'] = 0
    return rooms[id]


@app.route('/rooms/checkOut', methods=['POST'])
def checkOut():
    room = request.get_json(force=True)
    id = room['id']
    rooms[id]['name'] = ''
    rooms[id]['idCard'] = ''
    rooms[id]['haveCheckIn'] = False
    rooms[id]['checkInDate'] = ''
    rooms[id]['cost'] = 0
    rooms[id]['expectTemp'] = 25
    rooms[id]['speed'] = 'Low'
    rooms[id]['temp'] = 'Server says it is 23'
    rooms[id]['power'] = False
    rooms[id]['_showDetails'] = True
    return rooms[id]


'''
# Auth Part
'''

admins = []


@app.route('/auth/register', methods=['POST'])
def register():
    req = request.get_json(force=True)
    for admin in admins:
        if admin['email'] == req['email']:
            return jsonify({'error': True})
    admins.append(req)
    return jsonify({'error': False})


@app.route('/auth/loginAdmin', methods=['POST'])
def loginAdmin():
    req = request.get_json(force=True)
    for admin in admins:
        if admin['email'] == req['email']:
            return jsonify({'error': admin['pwd'] != req['pwd']})
    return jsonify({'error': True})


@app.route('/auth/login', methods=['POST'])
def login():
    req = request.get_json(force=True)
    print(req)
    if int(req['roomId']) < 0 or int(req['roomId']) >= len(rooms):
        return jsonify({'error': True})
    if 'idCard' not in rooms[int(req['roomId'])].keys():
        return jsonify({'error': True})
    return jsonify({'error': req['idCard'] != rooms[int(req['roomId'])]['idCard']})


'''
# Center Part 中央空调状态
'''

center = {
    'power': False,
    'state': 'Standby',
    'mode': 'Cold',
    'temp': 25,
}


@app.route('/center/')
def center_page():
    print(center)
    return jsonify(center)


@app.route('/center/flipPower', methods=['POST'])
def flipPower():
    center['power'] = not center['power']
    return center


@app.route('/center/setMode', methods=['POST'])
def setMode():
    req = request.get_json(force=True)
    print(req)
    center['mode'] = req['mode']
    center['temp'] = 25
    return center


@app.route('/center/temp_add', methods=['POST'])
def temp_add():
    req = request.get_json(force=True)
    print(req)
    center['temp'] += req['offset']
    return center


'''
# Slave Part 从控机状态，复用了rooms
'''


@app.route('/rooms/flipPower', methods=['POST'])
def slave_flipPower():
    req = request.get_json(force=True)
    id = int(req['id'])
    rooms[id]['power'] = not rooms[id]['power']
    rooms[id]['_showDetails'] = True
    return jsonify(rooms[id])


@app.route('/rooms/temp_add', methods=['POST'])
def slave_temp_add():
    print(request)
    req = request.get_json(force=True)
    print(req)
    id = int(req['id'])
    rooms[id]['expectTemp'] += int(req['offset'])
    rooms[id]['_showDetails'] = True
    return jsonify(rooms[id])


@app.route('/rooms/set_speed', methods=['POST'])
def slave_set_speed():
    req = request.get_json(force=True)
    id = int(req['id'])
    rooms[id]['speed'] = req['speed']
    rooms[id]['_showDetails'] = True
    return jsonify(rooms[id])


if __name__ == "__main__":
    app.run(debug=True)
