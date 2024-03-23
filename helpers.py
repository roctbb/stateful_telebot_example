from infrastructure import users

def get_or_create_user(user_id):
    if user_id not in users:
        users[user_id] = {
            "state": "start"
        }

    return users[user_id]