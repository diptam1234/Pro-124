from flask import Flask

app = Flask(__name__)
@app.route("/")
def helloWorld():
    return "Hello World! By Diptam"

if (__name__ == '__main__'):
    app.run()


# The GET Method - GET is used to request data from a specified resource.
# The POST Method -POST is used to send data to the server to create/update a resource.
# The PUT Method - PUT is used to send data to a server to create / update a resource.
# The DELETE Method - DELETE is used to delete a resource..