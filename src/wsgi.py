import os
from waitress import serve
from server import app, PORT

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=PORT)

