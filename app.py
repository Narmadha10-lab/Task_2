from flask import Flask
from flask_restful import Resource, Api
from flask import Flask, request

app = Flask(__name__)
api = Api(app)
nameDatabase = {
    1:{'name':'Smriti Mary.D'},
    2:{'name':'Dhaarani.A'},
    3:{'name':'Diya.B'},
    4:{'name':'Priyadharshini.K'},
    5:{'name':'Rajpriya.R'}
}
class Items(Resource):
    def get(self):
        return nameDatabase
    
    def post(self):
        data = request.json
        itemId = len(nameDatabase.keys()) + 1
        nameDatabase[itemId] = {'name':data['name']}
        return nameDatabase
    
class Item(Resource):
    def get(self, pk):
        return nameDatabase
    
    def put(self,pk):
        data = request.json
        nameDatabase[pk]['name'] = data['name']
        return nameDatabase
    
    def delete(self,pk):
        del nameDatabase[pk]
        return nameDatabase
    
api.add_resource(Items, '/')
api.add_resource(Item, '/<int:pk>')

if __name__ == '_main_':
    app.run(debug=True)