from flask import Flask, render_template, request
from PIL import Image
import secrets

app = Flask(__name__)

# generate random secret key
app.config['SECRET_KEY'] = secrets.token_hex(16)

@app.route('/')
def hello():
    # home page
    
    return render_template(
        "index.html", 
        # pass variables into the HTML template
        btn_range = range(3), 
        prompt_images = ["/static/images/placeholder_image.png" for i in range(3)]
    )

@app.route('/prompt', methods=['POST', 'GET'])
def prompt():
    # generate images from user prompt
    print("user prompt received:", request.form['prompt_input'])
    
    return render_template(
        "index.html", 
        # pass variables into the HTML template
        btn_range = range(3), 
        prompt_images = ["/static/images/placeholder_image.png" for i in range(3)]
    )

@app.route('/supersample', methods=['POST', 'GET'])
def supersample():
    # enlarge and save prompt image in high quality
    print("save button", request.form['save_btn'], "was clicked!")

    return render_template(
        "index.html", 
        # pass variables into the HTML template
        btn_range = range(3), 
        prompt_images = ["/static/images/placeholder_image.png" for i in range(3)]
    )

if __name__ == '__main__':
    # run application
    app.run(
        host = '0.0.0.0', 
        port = 8000, 
        debug = True
    )   

