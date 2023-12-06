import requests
import json

def get_todo(post_id):
    try:
        response = requests.get(f'https://jsonplaceholder.typicode.com/todos/{post_id}')
        response.raise_for_status()

        content = response.json()
        print(json.dumps(content, indent=4))
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Error:", err)

post_id = 1
get_todo(post_id)

class ToDo:
    def __init__(self, user_id, title, completed):
        self.user_id = user_id
        self.title = title
        self.completed = completed

new_todo = ToDo(1, 'My new task', False)

def create_todo(todo):
    try:
        response = requests.post('https://jsonplaceholder.typicode.com/todos', json=todo.__dict__)
        response.raise_for_status()

        content = response.json()
        print(json.dumps(content, indent=4))
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Error:", err)

create_todo(new_todo)

new_todo.title = 'My updated task'

def update_todo(todo, post_id):
    try:
        response = requests.put(f'https://jsonplaceholder.typicode.com/todos/{post_id}', json=todo.__dict__)
        response.raise_for_status()

        content = response.json()
        print(json.dumps(content, indent=4))
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Error:", err)

post_id = 101
update_todo(new_todo, post_id)

