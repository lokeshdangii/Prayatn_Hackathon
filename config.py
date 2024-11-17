#  Mysql configuration
# Function to dynamically create db_config based on user input
def get_db_config(host, user, password):
    return {
        'host': host,
        'user': user,
        'password': password,
    }
