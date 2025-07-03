
# Filename: thread_and_microservice_demo.py

import threading
import time
from flask import Flask, jsonify, request

# ------------------ 1. MULTITHREADING DEMO ------------------

def print_numbers():
    for i in range(1, 6):
        print(f"[{threading.current_thread().name}] Number: {i}")
        time.sleep(1)

def print_letters():
    for c in ['A', 'B', 'C', 'D', 'E']:
        print(f"[{threading.current_thread().name}] Letter: {c}")
        time.sleep(1)

def run_threads():
    print("\n--- Multithreading Demo Started ---")
    t1 = threading.Thread(target=print_numbers, name="Thread-Numbers")
    t2 = threading.Thread(target=print_letters, name="Thread-Letters")

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("--- Multithreading Demo Finished ---\n")


# ------------------ 2. MICROSERVICE DEMO USING FLASK ------------------

app = Flask(__name__)

# Fake database
users = {
    1: {"name": "Praful", "role": "Engineer"},
    2: {"name": "Sonal", "role": "Manager"}
}

@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(users)

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

@app.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = max(users) + 1
    users[user_id] = data
    return jsonify({'id': user_id, 'user': data}), 201

def run_flask_app():
    print("Starting Flask Microservice on http://127.0.0.1:5000/")
    app.run(debug=False)


# ------------------ MAIN DRIVER ------------------

if __name__ == "__main__":
    # 1. Run threading example
    run_threads()

    # 2. Run Flask Microservice
    # NOTE: Uncomment the line below to run the microservice
    # run_flask_app()

    # Keep this file clean to prevent Flask auto-running
    print("Comment/uncomment `run_flask_app()` to run the Flask server.")
# ```

# ---

# ### 📌 Output & Features

# #### 🧵 **Multithreading Output**

# ```txt
# [Thread-Numbers] Number: 1
# [Thread-Letters] Letter: A
# ...
# --- Multithreading Demo Finished ---
# ```

# #### 🌐 **Microservice API (if run)**

# * `GET /users` → Returns all users
# * `GET /user/1` → Returns user with ID 1
# * `POST /user` → Add a new user (JSON input)

# > Run Flask API:
# > Uncomment `run_flask_app()`
# > Then run: `python thread_and_microservice_demo.py`
# > Use Postman or browser to hit `http://localhost:5000`

# ---

# ### 📎 Tools & Libraries Used

# | Feature        | Library     |
# | -------------- | ----------- |
# | Multithreading | `threading` |
# | API Server     | `flask`     |

# ---

# Would you like me to:

# * Package this as a **Docker-ready microservice**?
# * Add **asynchronous (asyncio)** version?
# * Convert it into a **FastAPI**-based microservice instead of Flask?

# Let me know!
