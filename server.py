from flask_app import app
from flask_app.controllers import hospitals,users,cards,doctors,categories,diseases



if __name__=='__main__':
    app.run(debug=True)  
