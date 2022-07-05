# -*- coding: utf-8 -*-

from . import server

if __name__ == '__main__':
    # Running app in debug mode
    server.api.run(debug=True,host='0.0.0.0')