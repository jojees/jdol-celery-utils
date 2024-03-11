from jdol_celery_utils import app

class ComputeStocks:
    def __init__(self):
        pass
    
    @app.task
    def getRsPositives(self, username, email):
        pass
    
    @app.task
    def getRsRatios(self, username, email):
        pass