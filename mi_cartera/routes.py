from mi_cartera import app

@app.route("/")
def index():
    return "Flask rulando"