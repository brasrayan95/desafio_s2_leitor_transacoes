from transactions.models import Transaction


def salvar(line):
    new_transaction = {
        "tipo": line[0:1],
        "data": line[1:5] + "-" + line[5:7] + "-" + line[7:9],
        "valor": float(float(line[9:19]) / 100),
        "cpf": line[19:30],
        "cartao": line[30:42],
        "hora": line[42:44] + ":" + line[44:46] + ":" + line[46:48],
        "dono": line[48:62],
        "nomedaloja": line[62:81],
    }

    def fix_value(obj):
        if obj["tipo"] == "2" or obj["tipo"] == "3" or obj["tipo"] == "9":
            obj["valor"] = obj["valor"] * (-1)
        return obj

    transaction = Transaction.objects.create(**fix_value(new_transaction))
    return transaction
