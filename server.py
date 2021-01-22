from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv','a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submint():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went Wrong!'


#@app.route('/about.html')
#def about():
    #return render_template('about.html')


#@app.route('/components.html')
#def components():
    #return render_template('components.html')

#@app.route('/contact.html')
#def contact():
    #return render_template('contact.html')

#@app.route('/work.html')
#def work():
    #return render_template('work.html')

#@app.route('/works.html')
#def works():
    r#eturn render_template('works.html')

#def blog():
    #return "These are my thoughts about this blog: "


#@app.route('/blog/2020/dogs')
#def blog2():
    #return "My dogs"










#export FLASK_APP=server.py
#flask run

#export FLASK_ENV=development
#flask run


#python3 -m venv venv
#. venv/bin/activate
#. 'folder name'/bin/activate
#on windows: py -3 -m venv venv
#venv\Scripts\activate


#. web\ server/bin/activate


#python3 -m venv web\ server
