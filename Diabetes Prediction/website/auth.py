from flask import Blueprint, render_template, session, request, jsonify

auth = Blueprint('auth', __name__)

# Example authentication logic in your login route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Validate user credentials (replace this with your actual validation logic)
        admin_email = "sonalimirajkar174@gmail.com"
        admin_password = "Dhanashri@20"

        email = request.form.get('email')
        password = request.form.get('password')

        if admin_email == email and admin_password == password:
            # If credentials are valid, set user_authenticated to True
            session['user_authenticated'] = True
            response_data = {"success": True}
        else:
            # If credentials are invalid, set user_authenticated to False
            session['user_authenticated'] = False
            response_data = {"success": False}

        return jsonify(response_data)

    # Handle GET request (if needed)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    # Implement your logout logic here
    return "<h1>Logout Page</h1>"