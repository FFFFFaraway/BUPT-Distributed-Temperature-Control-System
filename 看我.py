'''
强烈建议把服务器端记录时间的项目从
time.ctime()
改成与mysql中datetime类型兼容的格式，不然日期选择不好搞
以及数据库中与时间/日期有关的类型datetime
time.strftime("%Y-%m-%d", time.localtime()) 
time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

'''
#在server.py中
#正常
@app.route('/form/roomList')
def get_room_list():
    ret=MASTER.get_room_list()
    return jsonify(ret)
#正常
@app.route('/form/rep',methods=['POST'])
def get_form():
    req=request.get_json()
    sd,ed,sr,er=req['sd'],req['ed'],req['sr'],req['er']
    ret=MASTER.get_form(sd,ed,sr,er)
    return jsonify(ret)

#在master_and_slave.py的Master类中
    #正常
    def get_OpRecord_id(self, Record:str):
        sql = 'select id from CheckRecord where Record = {}'.format(Record)
        self.cursor.execute(sql)
        id =self.cursor.fetchone()[0]
        self.db.commit()
        return id

    #不正常
    #staring date,ending date,starting room,ending room
    def get_form(self,sd,ed,sr,er):
        sql="select * from oprecord where time between \"{}\" and \"{}\"".format(sd,ed)
        self.cursor.execute(sql)
        ret=[]
        while 1:
            t=self.cursor.fetchone()
            if t is None:
                break
            rid=self.get_OpRecord_id(t[0])
            if rid<sr or rid> er:
                continue
            ret.append({
                "room":rid,
                "time":t[1],
                "type":t[2],
                "old":t[3],
                "new":t[4],
                "wind":t[5],
                "cost":t[6]
            })
        self.db.commit()
        return ret