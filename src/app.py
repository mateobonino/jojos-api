from flask import Flask, jsonify
from classes.serializer import Serializer

app = Flask(__name__)

serializer = Serializer()

serializer.load_data()

@app.route('/characters/<jojoname>', methods=['GET'])
def get_jojo(jojoname):
    result = serializer.search_character(jojoname)
    if result == None:
        return jsonify({'error': 'No character was found'})
    return result.toJson()

@app.route('/stands/<standname>', methods=['GET'])
def get_stand(standname):
    result = serializer.search_stand(standname)
    if result == None:
        return jsonify({'error': 'No stand was found'})
    return result.toJson()

@app.route('/season/<seasoname>', methods=['GET'])
def get_season(seasoname):
    result = serializer.search_season(seasoname)
    if result == None:
        return jsonify({'error': 'No season was found!'})
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)