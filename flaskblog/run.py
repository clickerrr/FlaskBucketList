# this imports the app from the init file and then allows for the app to be ran with all the routes and stuff done
from flaskblog import app
from os import getenv
# run
if __name__ == "__main__":
    app.run(debug=getenv("debug-mode") == "True")