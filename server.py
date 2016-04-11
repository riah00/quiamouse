from flask import Flask, render_template, request, url_for, redirect
import tasks


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('hometemplate.html')


@app.route('/qm', methods=['GET', 'POST'])
def quiamouse():
    return render_template('quiamousetemplate.html')


@app.route('/qms', methods=['POST'])
def qms():
    if request.method == 'POST':
        tasks.quiamouse.delay(request.form['time'], request.form['username'], request.form['password'],
                              request.form['link'], request.form['gametype'])
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

