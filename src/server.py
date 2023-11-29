import logging

from src.main import App

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app_instance = App()
    app_instance.app.run(host='0.0.0.0', port=5000, debug=True)
