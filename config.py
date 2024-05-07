import os 

class Config:
    @property
    def data_file_path(self):
        value = os.getenv('SN08_DATA_FILE_PATH')
        if not value:
            raise ValueError("SN08_DATA_FILE_PATH not set")
        return value 
    
    @property
    def data_file_name(self):
        value = os.getenv('SN08_DATA_FILE_NAME')
        if not value:
            raise ValueError("SN08_DATA_FILE_NAME not set")
        return value
    
    @property
    def secret_key(self):
        value = os.getenv('SN08_DATA_SERVER_SECRET_KEY')
        if not value:
            raise ValueError("SN08_DATA_SERVER_SECRET_KEY not set")
        return value