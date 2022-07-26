from app import *
from app import app


def current_user():
    if 'user' in session:
        get_user = Users.query.filter_by(name=session['user']).first()
        return get_user


@app.route('/')
def index():
    user = current_user()
    return render_template('index.html', user=user)


@app.route('/register', methods=['POST', 'GET'])
def register():
    user = current_user()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        email = request.form.get('email')
        if password != confirm_password:
            flash('Confirm password is wrong !!! ')
            return redirect(url_for('register'))
        else:
            password_hash = generate_password_hash(password)
            print(password_hash)
            new_user = Users(name=username, password=password_hash, email=email, director=0, admin=0)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login',user=user))
    return render_template('register.html',user=user)


@app.route('/login', methods=['POST', 'GET'])
def login():
    user = current_user()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        get_user = Users.query.filter_by(name=username).first()
        if get_user:
            if check_password_hash(get_user.password, password):
                session['user'] = get_user.name
                return redirect(url_for('index'))
            else:
                flash('user name or password is wrong !!!')
        else:
            flash('user name or password is wrong !!!')
            return redirect(url_for('login'))
    return render_template('login.html',user=user)


@app.route('/users')
def users():
    user = current_user()
    get_user_list = Users.query.filter(Users.director == False).order_by("id").all()
    return render_template('users.html', get_user_list=get_user_list,user=user)


@app.route('/set_info/<int:get_id>')
def set_info(get_id):
    get_user = Users.query.filter_by(id=get_id).first()
    if get_user.admin:
        get_user.admin = False
        db.session.commit()
        return redirect(url_for('users'))
    else:
        get_user.admin = True
        db.session.commit()
        return redirect(url_for('users'))



@app.route('/add_job')
def add_job():
    user = current_user()
    return render_template('job_page.html',user=user)


@app.route('/logout')
def logout():
    session['user'] = None
    return redirect(url_for('index'))