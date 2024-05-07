from flask import Flask, request, send_from_directory, abort
import jwt
from config import Config

app = Flask(__name__)
config = Config()

@app.route('/download')
def download_file():
    # Get the JWT from the 'token' query parameter
    token = request.args.get('token')
    if not token:
        abort(401)  # Unauthorized if no token is provided

    try:
        # Decode the JWT using the secret key
        jwt.decode(token, config.secret_key, algorithms=["HS256"])
    except jwt.InvalidTokenError:
        abort(401)  # Unauthorized if token is invalid

    # Send the file
    return send_from_directory(config.data_file_path, config.data_file_name, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
