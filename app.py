from flask import Flask, render_template, request,jsonify
from apPM import TamanhoM2
from apMP import PrecoM2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def Home():
    if request.method == "POST":
        entrada_rs = request.form.get("valor")
        entrada_m2 = request.form.get("metros")
        
        resultadoRS = TamanhoM2(entrada_rs) if entrada_rs and float(entrada_rs) >= 50000 else None
        resultadoM2 = PrecoM2(entrada_m2) if entrada_m2 and float(entrada_m2) >= 45 else None
        
        return jsonify(resultadoRS=resultadoRS, resultadoM2=resultadoM2)
    
    return render_template('index.html')

app.run(debug=True)
