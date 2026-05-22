from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <h1>Hello World</h1>
    <p>Nama : Maulana Abdul Aziz</p>
    <p>NPM : 50425612</p>
    <p>Kelas : 1IA04</p>
    <p>Jurusan : Informatika</p>
'''

if __name__ == '__main__':
    app.run(debug=True)