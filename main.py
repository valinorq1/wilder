# -*- coding: utf-8 -*-
import re
import sys
import threading
import string
import random
import json
from datetime import datetime, date


from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from requests_futures.sessions import FuturesSession
import requests
from bs4 import BeautifulSoup
import pandas as pd
from wmi import WMI


from utils import *
from ui import Ui_Dialog


class WildParser(QtWidgets.QMainWindow):
    def __init__(self):
        super(WildParser, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_UI()
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.products_data = []

    def init_UI(self):
        self.ui.start_parse.clicked.connect(self.start_work)
        self.ui.stop_parse.clicked.connect(lambda: self.start_work(stop=True))
        self.ui.minimize_window.clicked.connect(self.minimize)
        self.ui.close_programm.clicked.connect(self.close_programm)
        self.ui.save_parsed_data.clicked.connect(self.save_data)
        self.ui.activate.clicked.connect(self.check_serial)
        self.ui.save_parsed_data.hide()
        self.ui.stop_parse.hide()
        self.ui.work_text_status.setText("<font color='white' style='font-weight:bold;'>Ожидаем работы</font>")
        self.setFixedSize(1014, 790)
        self.ui.start_parse.hide()
        self.ui.label.hide()

    def get_hwid(self):
        a = WMI().Win32_ComputerSystemProduct()[0].UUID
        return a

    def check_serial(self):
        key = self.ui.personal_key.text()
        hwid = self.get_hwid()
        req = requests.get(f"http://valinor-dev.ru/wilder/?hwid={hwid}&key={key}")
        response = json.loads(req.text)
        if response['auth']:
            self.ui.logs_data.append("Авторизация прошла успешно")
            self.ui.start_parse.show()
        else:
            try:
                self.ui.start_parse.hide()
            except:
                pass
            self.ui.logs_data.append("Авторизация не пройдена")

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    def minimize(self):
        self.showMinimized()

    def close_programm(self):
        self.close()

    def get_selected_option_from_check_box(self):
        selected_options_list = {
            'parse_full_name': self.ui.full_name.isChecked(),
            'parse_brand': self.ui.brand.isChecked(),
            'parse_current_price': self.ui.current_price.isChecked(),
            'parse_default_price': self.ui.default_price.isChecked(),
            'parse_articul': self.ui.articul.isChecked(),
            'parse_rating': self.ui.rating.isChecked(),
            'parse_description': self.ui.description.isChecked(),
            'parse_img_link': self.ui.img_link.isChecked(),
            'parse_order_count': self.ui.order_count.isChecked(),
            'parse_reviews_count': self.ui.reviews_count.isChecked(),
            'parse_quantity_count': self.ui.product_quantity.isChecked(),
            'parse_characteristics': self.ui.characteristics.isChecked(),
            'parse_sizes': self.ui.sizes.isChecked(),
            'parse_colors': self.ui.colors.isChecked(),
            'parse_link': True

        }
        return selected_options_list

    def clear_string(self, string):  # В основном только для того, что удать знак "рубль" из строки "цена"
        return re.sub(r'\D', '', string)

    def process_filters(self, url_to_normalize):
        filter_list = ['discount', 'fkind', 'fseason', 'fconsists', 'fcolor', 'fsize', 'fbrand', 'priceU', 'xsubject',
                       'xparams', 'xshard', 'xfilters','xsearch', ]
        if any(ext in url_to_normalize for ext in filter_list):
            page_filter = True
        else:
            page_filter = False
        return page_filter

    def get_random_string(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
            self, "Сохранить как", "", "All Files (*);;Text Files (*.txt);;CSV files (*.csv)", options=options)
        if fileName:
            return fileName
        else:
            return 'report'

    def write_pd(self, data, file_name):
        first_dict_field = data[0]
        fields_name = []
        for i in first_dict_field.keys():
            fields_name.append(i)
        df = pd.DataFrame(data, columns=fields_name)
        if file_name != '':
            if '.csv' in file_name:
                df.to_csv(file_name, index=False)
                self.append_data_to_logs(f"<font color='green'>Файл {file_name}  успешно сохранён</font>", 'success')
                return True
            else:
                df.to_csv(file_name + '.csv', index=False)
                self.append_data_to_logs(
                    f"<font color='green'>Файл {file_name}.csv  успешно сохранён</font>", 'success')
                return True

        else:
            rand_name = self.get_random_string(5)
            print(rand_name)
            df.to_csv(f'{date.today()}{rand_name}.csv', index=False)
            self.append_data_to_logs(
                f"<font color='green' style='font-size:24px;'>Файл {rand_name}.cvs  успешно сохранён</font>", 'success')
            return True

    def append_data_to_logs(self, text, status_color ='notif'):
        if status_color == 'warning':
            self.ui.logs_data.append(
                f"<span style=\" font-size:10pt; font-weight:600; color:#ff0000;\" >{text} "
                f"<br />________________________</span>")
        elif status_color == 'success':
            self.ui.logs_data.append(
                f"<span style=\" font-size:10pt; font-weight:600; color:#169c16;\" >{text}"
                f"<br />________________________</span>")
        elif status_color == 'notif':
            self.ui.logs_data.append(
                f"<span style=\" font-size:10pt; font-weight:600; color:#169db8\" >{text}"
                f"<br />________________________</span>")
        else:
            self.ui.logs_data.append(
                f"<span style=\" font-size:10pt; font-weight:600; color:#e3b614;\" >{text}"
                f"<br />________________________</span>")

    def calculate_page_count(self, html):
        soup = BeautifulSoup(html.text, 'lxml')
        total_item_in_selected_filters = soup.find_all('div', {'id': 'body-layout'})

        for child in total_item_in_selected_filters:
            total_products = int(
                child.find(class_='goods-count').get_text().strip().encode('ascii', 'ignore').decode(
                    encoding="utf-8"))
        total_page = total_products // 100
        if total_page <= 0:
            return 1
        else:
            if (total_products % 100) > 0:
                total_page += 1
                return total_page

    def get_product_count(self, html):
        soup = BeautifulSoup(html.text, 'lxml')
        total_item_in_selected_filters = soup.find_all('div', {'id': 'body-layout'})
        for child in total_item_in_selected_filters:
            total_products = int(
                child.find(class_='goods-count').get_text().strip().encode('ascii', 'ignore').decode(
                    encoding="utf-8"))
        return total_products

    def get_total_page(self, url, filters):
        s = requests.Session()
        if filters:
            page_type = "&page="
        else:
            page_type = "?page="

        if '&xsearch=true' in url:
            get_page = s.get(url + f'{page_type}1&xsearch=true')
            page_count = self.calculate_page_count(get_page)
        else:
            get_page = s.get(url + f'{page_type}1')
            page_count = self.calculate_page_count(get_page)

        self.ui.total_prod_count.setText(str(self.get_product_count(get_page)))

        if page_count <= 1:
            page_count = 1
            self.ui.total_page_find.setText(str(page_count))
            return page_count
        elif page_count > 1:
            self.ui.total_page_find.setText(str(page_count))
            return page_count

    def parse_all_product_link(self, url, page_count, filters):
        self.ui.work_text_status.setText(
            "<font color='yellow' style='font-weight:bold;'>Получаем ссылки на товары</font>")
        base_url = 'https://www.wildberries.ru'
        products_link = []

        s = requests.Session()
        if filters:
            page_type = "&page="
        else:
            page_type = "?page="
        if page_count > 1:
            for i in range(1, page_count + 1):
                html = s.get(url + f'{page_type}{i}')
                soup = BeautifulSoup(html.text, 'lxml')
                all_product_link = soup.find_all('div', {'class': 'dtList-inner'})
                for k in all_product_link:
                    products_link.append(base_url + k.span.span.a.get('href'))
            return products_link
        else:
            html = requests.get(url)
            soup = BeautifulSoup(html.text, 'lxml')
            all_product_link = soup.find_all('div', {'class': 'dtList-inner'})
            for i in all_product_link:
                products_link.append(base_url + i.span.span.a.get('href'))
            return products_link

    def parse_selected_product_data(self, product_html, url, options):
        self.ui.work_text_status.setText(
            "<font color='green' style='font-weight:bold;'>Получаем информацию о товарах</font>")
        soup = BeautifulSoup(product_html, 'lxml')
        product_detailt_page = soup.find_all('div', {'id': 'container'})
        data = {}

        for child in product_detailt_page:
            if 'ssrModel' in product_html:
                start = 'ssrModel: '
                end = 'seoHelper'
                data_string = product_html[product_html.index(start):product_html.index(end) + len(end)]
                data_string = data_string[:-38]
                data_string = data_string.replace('\n', ' ')
                data_string = data_string[10:]
                json_data = json.loads(data_string)

            if options['parse_full_name']:
                try:
                    data['Полное название'] = extract_good_name(json_data)
                except AttributeError:
                    data['Полное название'] = ''

            if options['parse_brand']:
                try:
                    brand = child.find(class_='brand').get_text().strip().encode('ascii', 'ignore').decode(
                        encoding="utf-8")
                    data['Бренд'] = brand
                except AttributeError:
                    data['brand'] = ''

            if options['parse_current_price']:
                try:
                    current_price = child.find(class_='final-cost').get_text().strip().encode('ascii', 'ignore').decode(
                        encoding="utf-8")
                    data['Текущая цена'] = current_price + 'р.'
                except AttributeError:
                    data['Текущая цена'] = ''

            if options['parse_default_price']:
                try:
                    default_price = child.find(class_='c-text-base').get_text().strip().encode('ascii',
                                                                                               'ignore').decode(
                        encoding="utf-8")
                    data['Цена без скидкой'] = default_price + 'р.'
                except AttributeError:
                    data['default_price'] = ''

            if options['parse_articul']:
                try:
                    articul = child.find(class_='article').get_text().strip()
                    articul = articul[articul.find(":") + 1:]
                    articul = articul.lstrip()
                    data['Артикул'] = articul
                except AttributeError:
                    data['Артикул'] = ''

            if options['parse_rating']:
                try:
                    rating = child.find(class_='stars-line-lg').get_text().strip().encode('ascii', 'ignore').decode(
                        encoding="utf-8")
                    data['Рейтинг'] = rating

                except AttributeError:
                    data['Рейтинг'] = ''

            if options['parse_link']:
                data['Ссылка'] = url

            if options['parse_description']:
                if 'Описание' in product_html:
                    desc = extract_description(json_data)
                    data['Описание'] = desc
                else:
                    data['Описание'] = ''

            if options['parse_img_link']:
                images = child.find(class_='preview-photo')
                if images.has_attr('src'):
                    img_url = images['src']
                    img_url = img_url[img_url.find("//") + 2:]
                    data['Ссылка на картинку'] = str('http://' + img_url)

            if options['parse_reviews_count']:
                rew_count = child.find(id="a-Comments").get_text()
                rew_count = self.clear_string(rew_count)
                data['Кол-во отзывов'] = rew_count

            if options['parse_characteristics']:
                data['Характеристики'] = extract_characteristics(json_data)

            if options['parse_order_count']:
                data['Количество заказов'] = extract_order_counts(json_data)

            if options['parse_quantity_count']:
                data['Всего в наличии'] = extract_quantity(json_data)

            if options['parse_sizes']:
                data['Размеры'] = extract_sizes(json_data)

            if options['parse_colors']:
                data['Цвета'] = extract_colors(json_data)

            total_product = self.ui.total_product_parsed.text()
            total_product = int(total_product)
            total_product += 1

            self.ui.total_product_parsed.setText(str(total_product))
            self.products_data.append(data)
            self.ui.logs_data.append(
                f'\n {datetime.now().time().replace(microsecond=0)}: Получили информацию о товаре:  {url}')

    def fetch_product_data(self, urls, options, stop):
        with FuturesSession() as session:
            futures = [session.get(url) for url in urls]
            for future in futures:
                if stop():
                    break
                self.parse_selected_product_data(future.result().text, future.result().url, options)

    def stop(self):
        return True

    def main(self, stop):
        url = self.ui.url_to_parse.text()
        filters = self.process_filters(url)
        total_page = self.get_total_page(url, filters)
        all_product_link = self.parse_all_product_link(url, total_page, filters)
        options = self.get_selected_option_from_check_box()
        self.fetch_product_data(all_product_link, options, stop)
        self.ui.work_text_status.setText("<font style='font-weight:bold;color:#1eff00;'>Завершили работу...</font>")
        self.ui.start_parse.show()
        self.ui.stop_parse.hide()
        self.ui.label.show()
        self.ui.save_parsed_data.show()

    def save_data(self):
        if len(self.products_data) > 0:
            file_name = self.saveFileDialog()
            if file_name:
                save_status = self.write_pd(self.products_data, file_name)
            else:
                pass
            if save_status:
                self.ui.save_parsed_data.hide()
                self.field_data_reset()

    def start_work(self, stop=False):
        global stop_parsing
        if stop:
            stop_parsing = True
            self.ui.start_parse.setEnabled(True)
            self.ui.start_parse.show()
            self.ui.work_text_status.setText("<font color='red' style='font-weight:bold;'>Остановили работу</font>")
        else:
            self.ui.total_product_parsed.setText('0')

            stop_parsing = False
            if self.ui.url_to_parse.text() == '':
                self.ui.logs_data.append('Похоже нужно указать ссылку')
            else:
                self.ui.start_parse.hide()
                self.ui.stop_parse.show()
                parser_thread = threading.Thread(target=self.main, name='parse_thread', args=(lambda: stop_parsing,))
                parser_thread.daemon = True
                parser_thread.start()

    def field_data_reset(self):
        self.ui.url_to_parse.setText('')
        self.ui.total_page_find.setText('0')
        self.ui.total_product_parsed.setText('0')
        self.ui.total_prod_count.setText('')
        self.ui.label.hide()
        self.ui.logs_data.clear()
        self.products_data = []
        self.append_data_to_logs('Файл успешно сохранён', 'success')
        self.ui.work_text_status.setText("<font color='white' style='font-weight:bold;'>Ожидаем работы</font>")



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = WildParser()
    application.show()
    sys.exit(app.exec_())
