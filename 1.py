import pymongo
from flask import Flask,request
import json
from bson.objectid import ObjectId

app=Flask(__name__)
try:
    mongo=pymongo.MongoClient(host='localhost',port=27017,serverSelectionTimeoutMS=1000)  
    db=mongo.company                                                                        # python cursor to mongo database 'company'
    mongo.server_info()
 
except:
    print("ERROR")

#######################-------------CREATE-----------------############################

@app.route('/create')
def create():

    try:
        user={'name':request.form['name'],'Age':request.form['Age']}
        db.users.insert_one(user)
        print(user)
        return json.dumps({'status' : 'Success'})
    
    except:
        return json.dumps({'status' : "Failed"})




#######################-------------RETRIEVE-----------------############################

@app.route('/retrieve')
def retrieve():
    try:
        
        data=db.users.find()
        data=list(data)
        for i in data:
            i['_id']=str(i['_id'])
        print(data)
        return json.dumps(data,indent=4)
    
    except:
        return json.dumps({'status' : "False"})
    


#######################-------------UPDATE-----------------############################

@app.route('/update/<id>',methods=["PATCH"])
def update(id):
    try:
        db.users.update_one(
            {'_id':ObjectId(id)},
            {'$set': {'name':request.form['name'],'Age':request.form['Age']}}
            
        )
        return json.dumps({'status': "Success"})

    except:
        return json.dumps({'status': "USER ID ABSENT;CREATE NEW USER"})
    

#######################-------------DELETE-----------------############################

@app.route('/delete/<id>',methods=["DELETE"])
def delete(id):
    try:
        db.users.delete_one(
            {'_id':ObjectId(id)}
        )

        return json.dumps({'status':'Successfully deleted'})
    except:

        return json.dumps({'status' : 'USER DATA ABSENT OR ALREADY DELETED'})
        

        
if __name__=='__main__':
    app.run(port=8000,debug=True)


 