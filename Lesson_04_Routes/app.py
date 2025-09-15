from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <h1>Dynamic Routes Demo</h1>
<h2>Try: These URLs</h2>
<ul>
    <li><a href="/user/john"></a>User Profile: John</li>
    <li><a href="/user/alice"></a>User Profile: Alice</li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
</ul>
'''

@app.route('/user/username>', methods=['GET'])
def user_profile(username):
    return f'''
<h1>User Profiles</h1>
<p>Username: <strong>{username}</strong></p>
<p>Profile Type: {type(username).__name__}</p>
<p>Welcome to {username}'S profile page!</p>
<nav>
    <a href="/">Back to Homepage</a>
    <a href="/user/alice">Alice</a>
    <a href="/user/bob">Bob</a>
</nav>
'''
@app.route("/calc/<int:num1>/<operation>/<int:num2>")
def calculator(num1, operation, num2):
    operations = {
        '=': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else 'Error (Division by Zero!)'
    }
    if operation in operations:
        result = operations[operation]
        return f"{num1} {operation} {num2} = {result}"
    else:
        return f"Unknown operation: {operation}"
if __name__ == '__main__':
    app.run(debug=True)