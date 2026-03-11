from flask import Flask, render_template
from analise import analisar

app = Flask(__name__)

@app.route("/")

def dashboard():

    total, media, maior, categoria = analisar()

    return render_template(
        "dashboard.html",
        total=total,
        media=media,
        maior=maior,
        
    )

if __name__ == "__main__":
    app.run(debug=True)