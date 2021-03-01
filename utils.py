# -*- coding: utf-8 -*-

def extract_quantity(data):
    for k in data["suppliersInfo"].keys():
        uniq_id = k
        all_product_quantity = []
        for i in data['productCard']['nomenclatures'][uniq_id]['sizes']:
            for k, v in i.items():
                if k == 'quantity':
                    all_product_quantity.append(v)

    return sum(all_product_quantity)


def extract_order_counts(data):
    for k in data["suppliersInfo"].keys():
        uniq_id = k
    return  data['productCard']['nomenclatures'][uniq_id]['ordersCount']

def extract_sizes(data):
    for k in data["suppliersInfo"].keys():
        uniq_id = k

    sizes_list = []
    for i in data['productCard']['nomenclatures'][uniq_id]['sizes']:
        for k, v in i.items():
            if k == 'sizeName':
                if v == '0' or len(v) <= 0:
                    pass
                else:
                    sizes_list.append(v)
    return sizes_list

def extract_colors(data):
    for k in data["suppliersInfo"].keys():
        uniq_id = k
    # цвета
    colors = ''
    try:
        color = data['productCard']['nomenclatures'][uniq_id]['colorName']
        if color != '':
            colors = color
    except KeyError:
        colors = 'Цвет не указан'

    return colors

def extract_description(data):
    description = data['productCard']['description']
    if description == '':
        desc = ''
    else:
        desc = data['productCard']['description']

    return desc.replace('\n', '').replace('\n\n',' ')

def extract_sale(data):
    sale = data['productCard']['priceForProduct']
    return sale

def extract_good_name(data):
    clear_name = data['productCard']['goodsName']
    return clear_name.replace('\n', '').replace('\n\n', '')


def extract_characteristics(data):
    charact = data['productCard']['addedOptions']
    keys_to_remove = ['categoryId', 'priority']
    for i in charact:
        for d in keys_to_remove:
            i.pop(d)
    charact_list_type = []
    charact_list_opis = []
    for i in charact:
        for k, v in i.items():
            if k == 'property':
                charact_list_type.append(v)
            if k == 'subProperty':
                charact_list_opis.append(v)

    full_character = []
    for t, v in zip(charact_list_type, charact_list_opis):
        full_character.append(f"{t}: {v}")

    set_list_as_string = ';'.join(full_character)
    return set_list_as_string