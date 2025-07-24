from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # замените на свой секретный ключ

# "База данных" пользователя
user_profile = {
    'name': 'Иван Иванов',
    'email': 'ivan@example.com',
    'password': 'password123'
}

@app.route('/')
def home():
    return 'Добро пожаловать! Перейдите по <a href="/profile">ссылке</a>.'

@app.route('/profile', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        if not name or not email:
            flash('Пожалуйста, заполните имя и почту.')
            return redirect(url_for('edit_profile'))
        user_profile['name'] = name
        user_profile['email'] = email
        if password:
            user_profile['password'] = password
        flash('Профиль успешно обновлён!')
        return redirect(url_for('edit_profile'))
    return render_template('profile.html', user=user_profile)

if __name__ == '__main__':
    app.run(debug=True)