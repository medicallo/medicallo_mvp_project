from flask_app import app
from flask_app.controllers import hospitals,doctors,users,cards,categories,diseases,admins,landing_page



if __name__=="__main__":
    app.run(debug=True)  
