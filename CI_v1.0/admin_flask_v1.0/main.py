#设置
from flask import Flask, render_template, request
import pymysql
import json

app = Flask(__name__)

@app.route('/admin')
def index():
   return render_template('main.html')

#|------------------------------------set_signin------------------------------------|
@app.route('/admin/set_signin')
def setsign():
   return render_template('set_signin.html')

@app.route('/admin/set_sign', methods=['POST','GET'])
def set_signin():
    #print(1)
    sign_in_time = request.form.get('go')
    sign_out_time = request.form.get('leave')
    longitude = request.form.get('position1')
    latitude = request.form.get('position2')
    range = request.form.get('distance')
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='ci', charset='utf8')
    cursor = conn.cursor()
    sql = 'DELETE FROM setting'
    cursor.execute(sql)
    #sql = "INSERT INTO setting VALUES(sign_in_time,sign_out_time,longitude,latitude,range)"
    sql = "INSERT INTO setting VALUES ('%s','%s','%s','%s','%s')" % (sign_in_time,sign_out_time,longitude,latitude,range)
    #print(sql)
    cursor.execute(sql)
    conn.commit()
    cursor.close
    conn.close()
    return render_template('set_signin.html')

#|------------------------------------checksignin------------------------------------|
@app.route('/admin/checksignin/')
def check_signin():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='ci', charset='utf8')
    cur = conn.cursor()
    sql1 = "SELECT name,name_id,date,sign_in_status,late,sign_in_time FROM sign_in"
    cur.execute(sql1)
    u1 = cur.fetchall()
    sql2 = "SELECT sign_out_time FROM sign_out"
    cur.execute(sql2)
    u2 = cur.fetchall()
    conn.close()
    u = ()
    for i in range(len(u1)):
        u_temp = ()
        u_temp += u1[i]
        u_temp += u2[i]
        u += (u_temp,)
    #print(u)
    return render_template('check_signin.html', u=u)

#|------------------------------------userinfo------------------------------------|

@app.route('/admin/userinfo/',methods=['POST','GET'])
def userinfo_write():
    #write
    #print(request.method)
    if request.method == 'POST':
        #print(2)
        conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='ci', charset='utf8')
        name = request.form.get('name')
        name_id = request.form.get('num')
        gender = request.form.get('gender')
        age = request.form.get('age')
        address = request.form.get('home')
        job = request.form.get('job')
        password = request.form.get('pwd')

        cur = conn.cursor()
        sql2 = "INSERT INTO information VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (name, name_id, gender, age, address, job, password)
        #print(sql2)
        cur.execute(sql2)
        sql1 = "SELECT name,name_id,gender,age,address,position,password FROM information"
        cur.execute(sql1)
        u1 = cur.fetchall()
        conn.commit()
        conn.close()
        return render_template('user_info.html',u=u1)
    #print(1)
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='ci', charset='utf8')
    # read
    cur = conn.cursor()
    sql1 = "SELECT name,name_id,gender,age,address,position,password FROM information"
    cur.execute(sql1)
    u1 = cur.fetchall()
    conn.close()
    return render_template('user_info.html', u=u1)
#|------------------------------------messagelist------------------------------------|
@app.route('/admin/messagelist',methods=['GET','POST'])
def user_info():
    if request.method=='POST':
        conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='ci', charset='utf8')
        cur = conn.cursor()
        sql3 = "SELECT name_id FROM message"
        cur.execute(sql3)
        u3 = cur.fetchall()
        for each in range(len(u3)):
            print(type(u3[each][0]))
            if request.form.get(u3[each][0]) == 'agree':
                name = u3[each][0]
                result = 'agree'
                break
            elif request.form.get(u3[each][0]) == 'refuse':
                name = u3[each][0]
                result = 'refuse'
                break
        #sql2 = "INSERT INTO 'message'('result') VALUES ('%s')" % (result)
        sql2 = "UPDATE message SET result = '"+str(result)+"' WHERE  name_id = '"+str(name)+"'"
        cur.execute(sql2)
        sql1 = "SELECT * FROM message"
        cur.execute(sql1)
        u1 = cur.fetchall()
        conn.commit()
        conn.close()
        return render_template('message_list.html', u=u1)
    else:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='ci', charset='utf8')
        # read
        cur = conn.cursor()
        sql1 = "SELECT * FROM message"
        cur.execute(sql1)
        u1 = cur.fetchall()
        conn.commit()
        conn.close()
        return render_template('message_list.html', u=u1)

if __name__ == "__main__":
    ip = '127.0.0.1'
    app.run(debug=True)
