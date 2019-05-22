import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    
    MOVIE_API_KEY = '2b26bd4ffdf5c1726b654804dcce7f92'

    SECRET_KEY ='0000'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
