from transactions.models import Transaction


def get_shops_names(data):
    shop_list = []
    for object in data:
        shop_list.append(object.nomedaloja)
    shop_set = set(shop_list)
    return shop_set


def filter_by_shop(data):
    shop_list = []
    transactions_list_shop = []
    for object in data:
        shop_list.append(object.nomedaloja)
    shop_set = set(shop_list)
    for shop in shop_set:
        list = transaction_by_shop(shop)
        transactions_list_shop.append(list)
    return transactions_list_shop


def transaction_by_shop(shop):
    list = Transaction.objects.filter(nomedaloja=shop)
    return list
