from flask import Flask, render_template_string, request

app = Flask(__name__)

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if not encrypt:
                shift_amount = -shift_amount
            if char.islower():
                shifted = ord(char) + shift_amount
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
                result += chr(shifted)
            elif char.isupper():
                shifted = ord(char) + shift_amount
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
                result += chr(shifted)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        action = request.form['action']
        if action == 'encrypt':
            result = caesar_cipher(text, shift, encrypt=True)
        elif action == 'decrypt':
            result = caesar_cipher(text, shift, encrypt=False)

    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Caesar Cipher</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
            body {
                font-family: 'Roboto', Arial, sans-serif;
                background-color: #121212; /* Dark background */
                color: #E0E0E0; /* Light text */
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: #1f1f1f; /* Darker container background */
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
                width: 500px;
                text-align: center;
            }
            h1 {
                margin-bottom: 30px;
                color: #BB86FC; /* Light purple */
            }
            form {
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            label {
                margin: 10px 0;
                color: #E0E0E0; /* Light text */
                font-weight: bold;
            }
            input, select, button {
                padding: 10px;
                margin: 5px 0;
                border: 1px solid #333333; /* Dark gray border */
                border-radius: 5px;
                background-color: #333333; /* Dark input background */
                color: #E0E0E0; /* Light text */
                font-family: 'Roboto', Arial, sans-serif;
                font-size: 14px;
                transition: border-color 0.3s;
                width: calc(100% - 24px); /* Adjusted width for better alignment */
            }
            input:focus, select:focus, button:focus {
                outline: none;
                border-color: #BB86FC; /* Light purple border on focus */
            }
            select {
                width: 100%;
            }
            button {
                background-color: #BB86FC; /* Light purple */
                color: #121212; /* Dark text */
                cursor: pointer;
                font-weight: bold;
                transition: background-color 0.3s;
            }
            button:hover {
                background-color: #9b67e8; /* Darker purple on hover */
            }
            .result {
                margin-top: 20px;
                padding: 10px;
                background-color: #333333; /* Dark result background */
                border-radius: 5px;
                box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
            }
            .result p {
                color: #E0E0E0; /* Light text */
                font-size: 18px;
                margin: 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Caesar Cipher Application</h1>
            <form action="/" method="POST">
                <label for="text">Message:</label>
                <input type="text" id="text" name="text" required>
                
                <label for="shift">Shift Value:</label>
                <input type="number" id="shift" name="shift" required>
                
                <label for="action">Action:</label>
                <select id="action" name="action">
                    <option value="encrypt">Encrypt</option>
                    <option value="decrypt">Decrypt</option>
                </select>
                
                <button type="submit">Submit</button>
            </form>
            
            {% if result %}
                <div class="result">
                    <h2>Result:</h2>
                    <p>{{ result }}</p>
                </div>
            {% endif %}
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content, result=result)

if __name__ == '__main__':
    app.run(debug=True)
