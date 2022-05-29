from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///device_database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# create database class
# it is data model


class Device(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(200), nullable=False)
    mgmt_ip = db.Column(db.String(200), nullable=False)
    device_sno = db.Column(db.String(200), nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)

# home page
#

@app.route('/')
def index():
    all_devices = Device.query.all()
    return render_template('index.html', all_devices=all_devices)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        hostname = request.form['hostname']
        mgmt_ip = request.form['mgmt_ip']
        device_sno = request.form['device_sno']
        device = Device(hostname=hostname, mgmt_ip=mgmt_ip, device_sno=device_sno)
        db.session.add(device)
        db.session.commit()
        return redirect("/")
    all_devices = Device.query.all()
    return render_template('add.html', all_devices=all_devices)

# delete end point


@app.route('/delete/<int:sno>')
def delete(sno):
    device_delete = Device.query.filter_by(sno=sno).first()
    db.session.delete(device_delete)
    db.session.commit()
    return redirect("/")

# end point - update
# primary key is sno, update happens based on sno, so sno needs to passed along with function
# update comes through form via POST method so decorator should have POST


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        hostname = request.form['hostname']
        mgmt_ip = request.form['mgmt_ip']
        device_sno = actual_sno(hostname)
        #device_sno = request.form['device_sno']
        date_time = datetime.utcnow()
        device_update = Device.query.filter_by(sno=sno).first()
        device_update.hostname = hostname
        device_update.mgmt_ip = mgmt_ip
        device_update.device_sno = device_sno
        device_update.date_time = date_time
        db.session.add(device_update)
        db.session.commit()
        return redirect("/")

    device_update = Device.query.filter_by(sno=sno).first()
    return render_template('update.html', device_update=device_update)


def actual_sno(hostname):
    devicelist = [hostname]
    for device in devicelist:
        return(f"{device} serial_number_x")

# ensure you you update device name, below is CL31
# ensure junkins_url ip address
# refer flask-jenkins-github-ansible-arista pipeline in centos jenkins vm created local

@app.route('/jenkins', methods=['GET', 'POST'])
def jenkins_trigger():
    #jenkins_job_name = "URL-test2"
    #jenkins_job_name = "Flask-to-Jenkins-Name-Print"
    jenkins_job_name = "Flask-Jenkins-Github-Ansible-Arista"
    Jenkins_url = "http://192.168.181.204:8080"
    jenkins_user = "admin"
    jenkins_pwd = "admin"
    buildWithParameters = True
    jenkins_params = {'token': 'Token_Ravi',
                      'result2':'success',
                      'result1': 'success',
                      'name': 'CL33'
                      }

    try:
        auth= (jenkins_user, jenkins_pwd)
        crumb_data= requests.get("{0}/crumbIssuer/api/json".format(Jenkins_url),auth = auth,headers={'content-type': 'application/json'})
        if str(crumb_data.status_code) == "200":

            if buildWithParameters:
                data = requests.get("{0}/job/{1}/buildWithParameters".format(Jenkins_url,jenkins_job_name),auth=auth,params=jenkins_params,headers={'content-type': 'application/json','Jenkins-Crumb':crumb_data.json()['crumb']})
            else:
                data = requests.get("{0}/job/{1}/build".format(Jenkins_url,jenkins_job_name),auth=auth,params=jenkins_params,headers={'content-type': 'application/json','Jenkins-Crumb':crumb_data.json()['crumb']})

            if str(data.status_code) == "201":
                print ("Jenkins job is triggered")
            else:
                print ("Failed to trigger the Jenkins job")

        else:
            print("Couldn't fetch Jenkins-Crumb")
            #raise

    except Exception as e:
        print ("Failed triggering the Jenkins job")
        print ("Error: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)
