from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello! Successfully deployed via GitHub, Terraform, Ansible, Docker, K8s & Jenkins (Java 21)!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
