from app import app
from app.views import *
from config import *

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug= DEBUG)
