from app import app, socketio

socketio.run(app, port=5000, debug=True, use_reloader=True)
