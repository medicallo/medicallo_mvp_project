from flask_app import app
from flask_app.controllers import hospitals, users,cards,categories,diseases,admins



if __name__=="__main__":
    app.run(debug=True)  
