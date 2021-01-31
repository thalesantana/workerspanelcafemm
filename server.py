from flask import Flask, render_template, url_for, request, redirect
import csv
from database.mysql import MysqlConnection

app = Flask(__name__)


@app.route('/')
def my_home():
    db = MysqlConnection()
    db.connect_db()
    return render_template('index.html')  # if you want to render a .html file,
    # import render_template from flask and use
    # render_template("index.html") here.


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/workers ', methods=['GET', 'POST'])
def workers(query=None):
    def dictToQuery(d):
        query = ''
        for key in d.keys():
            query += str(key) + '=' + str(d[key]) + "&"
        return query
    db = MysqlConnection()
    db.connect_db()
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            if data['name'] == '' or data['title'] == '' or data['gender'] == '':
                return {'error': 'Deu merda!'}
            query = dictToQuery(data)
            print(query)
            query = """INSERT INTO workers (name,title,gender,link_github,link_linkedin,link_webpage) """
            query += """VALUES('%s',""" % (data['name'])
            query += """'%s',""" % (str(data['title']))
            query += """'%s',""" % (str(data['gender']))
            query += """'%s',""" % (str(data['github_url']))
            query += """'%s',""" % (str(data['linkedin_url']))
            query += """'%s')""" % (str(data['webpage_url']))
            db.run_insert_update(query)
            db.disconnect()
            return data
        except:
            db.disconnect()
            return 'did not save on database'
    else:
        db.disconnect()
        return 'It is a GET!'


def write_to_file(data):
    with open('database.txt', mode='w') as database:
        email = data['email']
        subject = data['subject']
        message = data['textarea']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='w') as database2:
        email = data['email']
        subject = data['subject']
        message = data['textarea']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


if __name__ == '__main__':
    app.debug = True
    app.run()  # go to http://localhost:5000/ to view the page.
