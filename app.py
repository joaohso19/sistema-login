from flask import Flask,render_template,request

app = Flask (__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    user = request.form.get('user')
    password = request.form.get('password')

    if user == "joaohso_" and password == "01":
        return "Acesso Liberado!"
    else:
        return "Acesso Negado!"
    
if __name__ == '__main__':
    app.run("0.0.0.0", port=8000)