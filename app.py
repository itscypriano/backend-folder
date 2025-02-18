from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/api/formulario', methods=['POST'])
def receber_dados():
    data = request.json  # Recebe os dados JSON enviados pelo frontend
    nome = data.get('nome')
    email = data.get('email')

    # Aqui você pode processar esses dados, como armazenar em um banco de dados ou fazer outras ações.
    print(f"Nome: {nome}, Email: {email}")

    return jsonify({'message': 'Formulário recebido com sucesso!'}), 200


if _name_ == '_main_':
    app.run(debug=True)