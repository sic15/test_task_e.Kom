from flask import Flask, request, jsonify
from tinydb import TinyDB
from datetime import datetime
import re

app = Flask(__name__)
db = TinyDB('templates.json')


@app.route('/get_form', methods=['POST'])
def get_form():
    """Обработчик POST запроса."""
    form_data = request.get_json()
    template = find_template(form_data)
    if template:
        return jsonify({"template_name": template["name"]})
    else:
        typed_fields = type_fields(form_data)
        del typed_fields['name']
        return jsonify(typed_fields)


def find_template(form_data):
    """Функция поиска подходящего шаблона."""
    templates = db.all()
    for template in templates:
        template_fields = set(template.keys()) - {'name'}
        form_fields = set(form_data.keys()) - {'name'}
        if template_fields.issubset(form_fields):
            typed_fields = type_fields(form_data)
            if all(template[t] == typed_fields[t] for t in template_fields):
                return template
            return None


def type_fields(form_data):
    """Определяем типы полей на основе правил валидации."""
    field_types = {}
    for field, value in form_data.items():
        if is_valid_date(value):
            field_types[field] = "date"
        elif is_valid_phone(value):
            field_types[field] = "phone"
        elif is_valid_email(value):
            field_types[field] = "email"
        else:
            field_types[field] = "text"
    return field_types


def is_valid_date(date_str):
    """Проверка валидности даты."""
    formats = ["%d.%m.%Y", "%Y-%m-%d"]
    for date_format in formats:
        try:
            datetime.strptime(date_str, date_format)
            return True
        except ValueError:
            pass
    return False


def is_valid_phone(phone_str):
    """Проверку валидности номера телефона."""
    phone_pattern = re.compile(r'^\+7 \d{3} \d{3} \d{2} \d{2}$')
    return bool(phone_pattern.match(phone_str))


def is_valid_email(email_str):
    """Проверка валидности email."""
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(email_pattern.match(email_str))


if __name__ == '__main__':
    app.run(debug=True)
