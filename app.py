from flask import Flask, render_template, request
import black

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def format_code():
    code = '# Write your code here\nprint("Hello, World!")'
    formatted_code = None
    if request.method == 'POST':
        code = request.form['code']
        try:
            formatted_code = black.format_str(code, mode=black.FileMode())
        except Exception as e:
            formatted_code = str(e)
    return render_template('index.html', code=code, formatted_code=formatted_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5100)