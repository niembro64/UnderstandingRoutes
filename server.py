
# Imports
from pickle import FALSE
from flask import Flask, render_template  # Import Flask to allow us to create our app


# Instatiating from Flask
app = Flask(__name__) # Create a new instance of the Flask class called "app"







@app.route('/index')
def index():
    return render_template("index.html", phrase = "hello", times=5)

@app.route('/about')
def about():
    return render_template("about.html", phrase = "sup", times = 33)

@app.route('/repeat/<word>/<num>')
def repeat(word, num):
    return render_template("return.html", phrase = word, times = int(num))

# Routing Methods
@app.route('/')             # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'ROOT : Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/wow')
def wow():
    return 'Wooooowwwww!'

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/dojo')
def dojo():
    return "Dojo!"
    
@app.route('/hi/<name>')
def hi(name):
    return "Hi, " + name




if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.


