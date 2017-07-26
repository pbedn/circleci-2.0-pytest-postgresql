class DBlogin():
    def __init__(self, database, user, password, host):
        self.database = database
        self.user = user
        self.password = password
        self.host = host

db_login_dict = {"circleci": DBlogin("circle_test", "ubuntu", "", "localhost")}
