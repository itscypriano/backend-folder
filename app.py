from flask import Flask, request, jsonify

app = Flask(__name__)


def aereoOuMaritimo(cotacao, taxa, bl, awb, taxedWeight, cbm):  # escolha de cotacao
    if cotacao == "maritima":
        return taxaMaritimo(taxa, bl, cbm)  # chama função maritima
    else:
        return taxaAereo(taxa, awb, taxedWeight)  # chama função aerea


def taxaMaritimo(taxa, bl, cbm):
    if not bl:
        precoFinal = taxa / cbm  # se bl for falso
    else:
        precoFinal = taxa * 1
    return precoFinal


def taxaAereo(taxa, awb, taxedWeight):
    if not awb:
        precoFinal = taxa / taxedWeight  # se awb for falso
    else:
        precoFinal = taxa * 1
    return precoFinal


@app.route("/api/formulario", methods=["POST"])
def receber_dados():
    data = request.json  # recebendo os dados enviados pelo frontend
    origin = data.get("origin")
    destiny = data.get("destiny")
    route = data.get("route")
    transittime = data.get("transittime")
    expirationdate = data.get("expirationdate")
    cotacao = data.get("cotacao")
    taxedWeight = data.get("taxedWeight")
    awb = data.get("awb")
    cbm = data.get("cbm")
    bl = data.get("bl")
    taxa = data.get("taxa")

    precoFinal = aereoOuMaritimo(cotacao, taxa, bl, awb, taxedWeight, cbm)

    return (
        jsonify({"precoFinal": precoFinal}),
        200,
    )


if __name__ == "__main__":
    app.run(debug=True)
