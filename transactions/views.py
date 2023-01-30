from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from transactions.models import Transaction

from .forms import FileForm
from . import serializers
from transactions.utils import get_shops_names
import ipdb


def read_file(file):
    for line in file["file"]:
        serializers.salvar(line.decode("utf-8").rstrip())


def get_file(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            read_file(request.FILES)
            return HttpResponseRedirect("/transactions/transactions/")
    else:
        form = FileForm()

    return render(request, "file.html", {"form": form})


def fix_type(data):
    tipos_de_transacao = {
        1: "Débito",
        2: "Boleto",
        3: "Financiamento",
        4: "Crédito",
        5: "Rec. Empréstimo",
        6: "Vendas",
        7: "Recebimento TED",
        8: "Recebimento DOC",
        9: "Aluguel",
    }
    for trans in data:
        trans.tipo = tipos_de_transacao[trans.tipo]
    return data


def show_trans(request):
    data = Transaction.objects.all()
    shops = get_shops_names(data)
    data = fix_type(data)

    return render(
        request,
        "transactionsList.html",
        {"data": data, "shops": shops},
    )
