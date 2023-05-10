from flask import Flask, jsonify
from serializer import Serializer

app = Flask(__name__)

serializer = Serializer()

serializer.load_data()

@app.route('/characters/<jojoname>', methods=['GET'])
def get_jojo(jojoname):
    result = serializer.search_character(jojoname)
    if result == None:
        return jsonify({'error': 'No character was found'})
    else:
        return result.toJson()

#@app.route('/stands/<standname>', methods=['GET'])
#def get_stand(standname)


if __name__ == '__main__':
    app.run(debug=True)