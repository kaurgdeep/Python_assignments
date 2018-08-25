from flask import Flask  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response.
@app.route('/dojo')
def dojo():
  return "dojo"


@app.route('/say/<flask>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def say(flask):
    print(flask)
    return "say "+flask


@app.route('/repeat/<num>/<word>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def repeat(num, word):
    return "hello /n"*int(99)
print(repeat)

   

if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module
    app.run(debug=True)    # Run the app in debug mode.
    