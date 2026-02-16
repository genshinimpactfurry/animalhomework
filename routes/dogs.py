from flask import Blueprint, render_template

dogs_bp = Blueprint('dogs', __name__, template_folder='../templates')

dogs_data = {
    'title': 'Все о собаках',
    'breeds': [
        {'name': 'Лабрадор', 'description': 'Активная, дружелюбная порода.'},
        {'name': 'Овчарка', 'description': 'Умная, легко обучаемая собака.'},
        {'name': 'Йорк', 'description': 'Маленькая, но смелая порода.'}
    ],
    'training_tips': [
        'Начинать с простых команд.',
        'Использовать лакомство для поощрения.',
        'Быть терпеливым.'
    ]
}

@dogs_bp.route('/dogs')
def dogs():
    return render_template('dogs.html', data=dogs_data)
