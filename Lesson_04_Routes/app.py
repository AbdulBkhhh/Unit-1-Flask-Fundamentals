from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
           <h1>Dynamic Routes Demo</h1>
<h2>Try: These URLS</h2>
<ul>
    <li><a href="/user/john">User Profile: john</a></li>
    <li><a href="/user/alice">User Profile: alice</a></li>
</ul> 
"""

@app.route('/user/<username>')
def user_profile(username):
    return f'''
     <h1>User Profile</h1>
 <p>Username: <strong>{username}</strong></p>
 <p>Profile Type: {type(username).__name__}</p>
 <p>Welcome to {username}'s profile page!</p>
 <nav>
    <a href="/"> Back to Homepage</a>
    <a href="/user/alice">Alice</a>
    <a href="/user/bob">Bob</a>
 </nav>    
'''
@app.route("/calc/<int:num1>/<operation>/<int:num2>")
def calculator(num1, operation, num2):
    operations = {
        '+' : num1 + num2,
        '-' : num1 - num2,
        '*' : num1 * num2,
        '/' : num1 / num2 if num2 != 0 else 'Error: Division by zero!'
    }
    if operation in operations:
        result = operations[operation]
        return f"{num1} {operation} {num2} = {result}"
    else:
        return f"Unknown operation!{operation}"
@app.route("/temp/<current>/<int:num1>")
def temperature(num1, current):
    changes = {
        'C' : (num1 * 9/5) + 32,
        'F' : (num1 - 32) * 5/9
    }
    if current in changes:
        result = changes[current]
        return f"{num1} {current} = {result} ˚{'F' if current == 'C' else 'C'}"
    else:
        return f"Unknown operation!{current}"
    

if __name__ == "__main__":
    app.run(debug=True)