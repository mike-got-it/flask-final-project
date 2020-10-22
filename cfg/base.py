class BaseConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Mikemike212@localhost:3306/final_project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'ThisIsHardestThing'
    JWT_SECRET_KEY = 'Dude!WhyShouldYouEncryptIt'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']