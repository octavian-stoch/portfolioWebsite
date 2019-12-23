from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saystuff')
def saystuff():
   return render_template('saystuff.html')

@app.route('/projects')
def projects():
   return render_template('projects.html')

@app.route('/java')
def javaPrograms():
   return render_template('javaProjects.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/python')
def python():
   return render_template('pythonProjects.html')

@app.route('/sql')
def sql():
   return render_template('sqlProjects.html')

if __name__ == '__main__':
   app.run(debug = True)