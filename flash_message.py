from flask import Flask, render_template, flash

app = Flask(__name__)
app.secret_key = 'SecretKey'


@app.route('/simple-flash')
def simple_flash():
    flash('Flash message added!')
    return render_template("flash/simple-flash.html")


@app.route('/flash-with-category')
def flash_with_category():
    flash('Flash message added with category!', 'error')
    return render_template("flash/flash-with-category.html")


@app.route('/filtering-flash-message')
def filtering_flash_message():
    flash('Flash message added with category filter error!', 'error')
    flash('Flash message added with category filter success!', 'success')
    return render_template("flash/filtering-flash-message.html")


if __name__ == '__main__':
    app.run()
