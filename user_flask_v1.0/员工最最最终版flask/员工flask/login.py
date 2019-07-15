from flask import Flask,render_template,request,session,redirect,url_for
import os
import pymysql
import time
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=1) #设置session的保存时间。

@app.route('/')
def login():
   return render_template('login.html')


@app.route('/main/', methods=['post','get'])
def yanzheng():
       nameid = request.form['login']
       ps = request.form['password']
       conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='ci', charset='utf8')
       cur = conn.cursor()
       sql = "SELECT `name`, `password` FROM `information` WHERE name_id ="+nameid
       cur.execute(sql)
       realps = cur.fetchall()
       conn.close()

       conn1 = pymysql.connect(host='127.0.0.1', user='root', password='', db='ci', charset='utf8')
       cur1 = conn1.cursor()
       sqll = "SELECT `date`, `sign_in_status`, `late`, `sign_in_time` FROM `sign_in` WHERE name_id =" + nameid
       cur1.execute(sqll)
       u1 = cur1.fetchall()
       conn1.close()

       conn2 = pymysql.connect(host='127.0.0.1', user='root', password='', db='ci', charset='utf8')
       cur2 = conn2.cursor()
       sqlll = "SELECT `date`, `type`, `result` FROM `message` WHERE name_id =" + nameid
       cur2.execute(sqlll)
       u2 = cur2.fetchall()
       conn2.close()

       u= {
              'u1': u1,
              'u2': u2
       }

       session.permanent = True  # 默认session的时间持续31天
       session['name_id'] = nameid
       session['name_name'] = realps[0][0]
       if ps == realps[0][1] :
           return render_template('index.html',**u)
       else:
           return render_template('login.html')

'''
@app.route('/index/')
def gerenjilu():
       name_id = session.get('name_id')
       conn1 = pymysql.connect(host='127.0.0.1', user='root', password='', db='ci', charset='utf8')
       cur1 = conn1.cursor()
       sqll = "SELECT `date`, `sign_in_status`, `late`, `sign_in_time` FROM `sign_in` WHERE name_id =" + name_id
       cur1.execute(sqll)
       u1 = cur1.fetchall()
       conn1.close()
       return render_template('index.html', u1=u1)

'''

@app.route('/message/', methods=['post','get'])
def shenqing():
       shenqing_leixing = request.form['leixing']
       shenqing_shijian = request.form['shenqingshijian']
       shenqing_liyou = request.form['shenqingliyou']
       shenqing_name = session.get('name_name')
       shenqing_nameid = session.get('name_id')
       conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='ci', charset='utf8')
       cur = conn.cursor()
       sql = "INSERT INTO `message` VALUES ('"+str(shenqing_name)+"','"+str(shenqing_nameid)+"','"+str(shenqing_shijian)+"','"+str(shenqing_leixing)+"','"+str(shenqing_liyou)+"','未处理');"
       print(sql)
       cur.execute(sql)
       personmessage = cur.fetchall()
       conn.close()

       conn1 = pymysql.connect(host='127.0.0.1', user='root', password='', db='ci', charset='utf8')
       cur1 = conn1.cursor()
       sqll = "SELECT `date`, `sign_in_status`, `late`, `sign_in_time` FROM `sign_in` WHERE name_id =" + shenqing_nameid
       cur1.execute(sqll)
       u1 = cur1.fetchall()
       conn1.close()

       conn2 = pymysql.connect(host='127.0.0.1', user='root', password='', db='ci', charset='utf8')
       cur2 = conn2.cursor()
       sqlll = "SELECT `date`, `type`, `result` FROM `message` WHERE name_id =" + shenqing_nameid
       cur2.execute(sqlll)
       u2 = cur2.fetchall()
       conn2.close()

       u = {
              'u1': u1,
              'u2': u2
       }

       return render_template('index.html',**u)


@app.route('/sign_in',  methods=['post'])
def sign_in():

    name = session.get('name_name')
    name_id =session.get('name_id')
    date =time.strftime("%Y-%m-%d", time.localtime())
    sign_in_status='True'
    location='1'
    sign_in_time=time.strftime("%H:%M:%S", time.localtime())


    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='ci', charset='utf8')
    cur = conn.cursor()

    sql = "SELECT `sign_in_time` FROM `setting` "
    print(sql)
    cur.execute(sql)
    Standard_setting= cur.fetchall()
    deadline = Standard_setting[0][0]
    late = (sign_in_time < deadline) and 'False' or 'True'

    sql = "INSERT INTO sign_in (name, name_id, date, sign_in_status, late, location, sign_in_time) VALUES('"+str(name)+"','"+str(name_id)+"','"+str(date)+"','"+str(sign_in_status)+"','"+str(late)+"','"+str(location) + "','"+str(sign_in_time)+"');"
    print(sql)
    cur.execute(sql)
    conn.close()
    time.sleep(5)
    conn1 = pymysql.connect(host='127.0.0.1', user='root', password='', db='ci', charset='utf8')
    cur1 = conn1.cursor()
    sqll = "SELECT `date`, `sign_in_status`, `late`, `sign_in_time` FROM `sign_in` WHERE name_id =" + name_id
    cur1.execute(sqll)
    u1 = cur1.fetchall()
    conn1.close()

    conn2 = pymysql.connect(host='127.0.0.1', user='root', password='', db='ci', charset='utf8')
    cur2 = conn2.cursor()
    sqlll = "SELECT `date`, `type`, `result` FROM `message` WHERE name_id =" + name_id
    cur2.execute(sqlll)
    u2 = cur2.fetchall()
    conn2.close()

    u = {
           'u1': u1,
           'u2': u2
    }

    return render_template('index.html', **u)


@app.route('/sign_out',  methods=['post'])
def sign_out():
    name = session.get('name_name')
    name_id = session.get('name_id')
    date = time.strftime("%Y-%m-%d", time.localtime())
    sign_out_status='1'
    late = '1'
    location='1'
    sign_out_time= time.strftime("%H:%M:%S", time.localtime())

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='ci', charset='utf8')
    cur = conn.cursor()

    sql = "SELECT `sign_out_time` FROM `setting` "
    print(sql)
    cur.execute(sql)
    Standard_setting = cur.fetchall()
    time_reborn = Standard_setting[0][0]
    late = (sign_out_time > time_reborn) and 'False' or 'True'

    sql = "INSERT INTO sign_out (name, name_id, date, sign_out_status, late, location, sign_out_time) VALUES('"+str(name)+"','"+str(name_id)+"','"+str(date)+"','"+str(sign_out_status)+"','"+str(late)+"','"+str(location) + "','"+str(sign_out_time)+"');"
    print(sql)
    cur.execute(sql)
    #realps = cur.fetchall()
    conn.close()
    time.sleep(5)

    conn1 = pymysql.connect(host='127.0.0.1', user='root', password='', db='ci', charset='utf8')
    cur1 = conn1.cursor()
    sqll = "SELECT `date`, `sign_in_status`, `late`, `sign_in_time` FROM `sign_in` WHERE name_id =" + name_id
    cur1.execute(sqll)
    u1 = cur1.fetchall()
    conn1.close()

    conn2 = pymysql.connect(host='127.0.0.1', user='root', password='', db='ci', charset='utf8')
    cur2 = conn2.cursor()
    sqlll = "SELECT `date`, `reason`, `result` FROM `message` WHERE name_id =" + name_id
    cur2.execute(sqlll)
    u2 = cur2.fetchall()
    conn2.close()

    u = {
           'u1': u1,
           'u2': u2
    }

    return render_template('index.html', **u)



if __name__ == '__main__':
   app.run()
