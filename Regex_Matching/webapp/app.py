from flask import Flask, request, render_template
import re
from validate_email import validate_email

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    reg = request.form.get("regexpression")
    usrtxt = request.form.get("usrtext")
    find = re.findall(str(reg),str(usrtxt))
    length=len(find)
    if (reg == '') or (usrtxt == ''):
        return render_template('empty.html')
    elif ' ' in find:
        return render_template('home.html', length=length)
    elif find == []:
        return render_template('home.html', length=length)
    return render_template('home.html', find=find, length=length)

@app.route('/email', methods=['POST'])
def valid():
    email = request.form.get("mail")
    test = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    com = re.compile(test) 
    if email =='':
        return render_template('empty.html')
    elif not re.match(com, email):
        return render_template('invalid.html')
    else:
        return render_template('home.html', com=com)



if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')

