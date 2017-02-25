from flask import Flask, render_template


# Create app object
app = Flask(__name__)

# Create index route
@app.route('/')
# Index render function
def index():
    return render_template('index.html')

# Mysterious thing that makes it so other computers can view the server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
