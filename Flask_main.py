import datetime
import hashlib
from flask import *
from MongoDBHelper import MongoDBHelper
from bson.objectid import ObjectId

web_app = Flask("Vets App")

@web_app.route("/")
def index():
    #return "Hello World :)"
    return render_template("index.html")

@web_app.route("/register")
def register():
    return render_template('register.html')

@web_app.route("/home")
def home():
    return render_template("home.html",email=session['vet_email'], name=session['vet_name'])

@web_app.route("/login-vet", methods=['POST'])
def login_vet():
    vet_data = {
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest(),
    }
    print(vet_data)
    db = MongoDBHelper(collection="vets")
    documents = list(db.fetch(query  = vet_data))
    print(documents, type(documents))
    if len(documents) == 1:


        session['vet_id'] = str(documents[0]['_id'])
        session['vet_email'] = documents[0]['email']
        session['vet_name'] = documents[0]['name']
        print(vars(session))
        return render_template('home.html', email=session['vet_email'], name=session['vet_name'])
    else:
        return render_template('error.html')

@web_app.route("/logout")
def logout():
    session['vet_id'] = ""
    session['vet_email'] = ""
    return redirect("/")



@web_app.route("/register-vet",methods =["POST"])
def register_vet():

    vet_data = {
        'name': request.form['name'],
        'email' : request.form['email'],
        'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest(),
        'createdOn': datetime.datetime.today()
    }
    print(vet_data)
    db = MongoDBHelper(collection='vets')
    db.insert(vet_data)

    return render_template('home.html', email=session['vet_email'])

@web_app.route("/add-customer" , methods = ["POST"])
def add_customer():

    customer_data = {
        'name': request.form['name'],
        'phone': request.form['phone'],
        'email': request.form['email'],
        'age': int(request.form['age']),
        'gender': request.form['gender'],
        'address': request.form['address'],
        'vet_id': session['vet_id'],
        'vet_email': session['vet_email'],
        'createdOn': datetime.datetime.today()
    }
    print(customer_data)
    db = MongoDBHelper(collection='Customer')
    db.insert(customer_data)

    return render_template('success.html', message="{} added successfully".format(customer_data['name']))

@web_app.route("/fetch-customers")
def fetch_customers_of_vet():
    db = MongoDBHelper(collection='Customer')
    query = {'vet_email':session['vet_email']}
    #query = {'_id': session['vet_id']}
    documents = (db.fetch(query))
    print(documents,type(documents))
    return render_template('customers.html', email=session['vet_email'], name=session['vet_name'], documents=documents)

@web_app.route("/fetch-pets")
def fetch_pets_of_vet():
    db = MongoDBHelper(collection='pet')
    query = {'vet_email':session['vet_email']}
    #query = {'_id': session['vet_id']}
    documents = (db.fetch(query))
    print(documents,type(documents))
    return render_template('pets.html', email=session['vet_email'], name=session['vet_name'], documents=documents)

@web_app.route("/delete-customer/<id>")
def delete_customer(id):
    db = MongoDBHelper(collection='Customer')
    query = {'_id':ObjectId(id)}
    customer = db.fetch(query= query)[0]
    db.delete(query)
    return render_template('success.html', message= "Customer with Id {} and Name {} Deleted Successfully".format(id,customer['name']))

@web_app.route("/update-customer/<id>")
def update_customer(id):
    db = MongoDBHelper(collection='Customer')
    query = {'_id': ObjectId(id)}
    customer = db.fetch(query=query)[0]

    return render_template('update customer.html',
                           message="Customer with Id {} and Name {} Updated Successfully".format(id, customer['name']), email=session['vet_email'], name=session['vet_name'],customer = customer)

@web_app.route("/update-pet/<id>")
def update_pet(id):
    db = MongoDBHelper(collection='pet')
    query = {'_id': ObjectId(id)}
    pet = db.fetch(query=query)[0]
    #return "Pet Updated"
    return render_template('update pet.html',
                           message="Pet with Id {} and Name {} Updated Successfully".format(id, pet['name']), email=session['vet_email'], name=session['vet_name'],pet = pet)

@web_app.route("/update-customer-in-db" , methods = ["POST"])
def update_customer_in_db():

    customer_data_to_update = {
        'name': request.form['name'],
        'phone': request.form['phone'],
        'email': request.form['email'],
        'age': int(request.form['age']),
        'gender': request.form['gender'],
        'address': request.form['address'],

    }
    print(customer_data_to_update)
    db = MongoDBHelper(collection='Customer')
    query = {'email':request.form['email']}
    db.update(customer_data_to_update,query)

    return render_template('success.html', message="{} Updated successfully".format(customer_data_to_update['name']))

@web_app.route("/update-pet-in-db" , methods = ["POST"])
def update_pet_in_db():


    pet_data_to_update = {
        'name': request.form['name'],
        'breed': request.form['breed'],
        'age': int(request.form['age']),
        'gender': request.form['gender'],

    }
    print(pet_data_to_update)
    db = MongoDBHelper(collection='pet')
    query = {'name':request.form['name']}
    db.update(pet_data_to_update,query)

    return render_template('success.html', message="{} Updated successfully".format(pet_data_to_update['name']))

@web_app.route("/search-customer")
def search():
    return render_template('search.html', email=session['vet_email'], name=session['vet_name'])

@web_app.route("/search-customer-post",methods = ["POST"])
def search_customer():
    db =MongoDBHelper(collection='Customer')
    query = {'email':request.form['email'], 'vet_id': session['vet_id']}
    customers = db.fetch(query)
    if len(customers)==1:
        customers = customers[0]
        #return "Found the Customer with name: {}".format(customers['name'])
        return render_template("customer_profile.html",customer = customers ,email=session['vet_email'], name=session['vet_name'])
    else:
        return render_template("error.html",message = "Customer Not Found")

@web_app.route("/searchbar-customer-post", methods=["POST"])
def searchbar_customer():
    db = MongoDBHelper(collection='Customer')
    query = {'email': request.form['email'], 'vet_id': session['vet_id']}
    customers = db.fetch(query)
    if len(customers) == 1:
        customers = customers[0]
        # return "Found the Customer with name: {}".format(customers['name'])
        return render_template("customer_profile.html", customer=customers,email=session['vet_email'], name=session['vet_name'])
    else:
        return render_template("error.html", message="Customer Not Found",email=session['vet_email'], name=session['vet_name'])
    #
@web_app.route("/add-pet/<id>")
def add_pet(id):
    db =MongoDBHelper(collection='Customer')
    query = {'_id':ObjectId(id)}
    customers = db.fetch(query)

    if len(customers)==1:
        customer = customers[0]

        #return "Found the Customer with name: {}".format(customers['name'])
        return render_template("add pet.html",customer = customer
                                            ,vet_id =session["vet_id"]
                                            ,email = session["vet_email"],
                                            name = session["vet_name"],
                                            )

    else:
        return render_template("error.html",message = "Customer Not Found")

@web_app.route("/save-vet" , methods = ['POST'])
def save_pet():
    pet_data = {
        'name': request.form['name'],
        'breed': request.form['breed'],
        'age': int(request.form['age']),
        'gender': request.form['gender'],
        'customer_id': request.form['customer_id'],
        'customer_email': request.form['customer_email'],
        'vet_id': session['vet_id'],
        'vet_email': session['vet_email'],
        'createdOn': datetime.datetime.today()
    }
    print(pet_data)
    db = MongoDBHelper(collection='pet')
    db.insert(pet_data)
    if len(pet_data['name']) == 0 or len(pet_data['breed']) == 0:
        return render_template('error.html', message="Name and Breed cannot be Empty")



    return render_template('success.html', message="{} added for customer {} successfully.."
                           .format(pet_data['name'], pet_data['customer_email']))

def main():

    web_app.secret_key = 'vetsapp-key-1'
    web_app.run()

if __name__ =="__main__":
    main()
#Search Customer
#Update Customer ->Radio Button If else
    #use id  instead of email in update
