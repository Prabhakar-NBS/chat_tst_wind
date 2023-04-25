import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from Chat import get_replys

appl = Flask(__name__)
CORS(appl)

@appl.route("/")
def index_get():
    return render_template("E:\chat_test-1\static\index.html")

@appl.route("/predictt", methods=['POST'])
def predictt():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    resp = get_replys(text)
    message = {"answer": resp}
    return jsonify({"query": message})

if __name__ == "__main__":
    appl.run(debug=True,port=5000)
    '''
    # Get the dynamically assigned port number from the environment variable
    port = int(os.environ.get('PORT', 3013))
    # Run the Flask app on the dynamically assigned port number
    appl.run(host='0.0.0.0', port=port, debug=True)
    '''