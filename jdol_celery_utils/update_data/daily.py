from jdol_celery_utils import app

class UpdateTickerFiles:
    def __init__(self):
        pass
    
    @app.task
    def update_indices(self, username, email):
        pass
    
    @app.task
    def update_ticker(self, symbol, eod):
        pass