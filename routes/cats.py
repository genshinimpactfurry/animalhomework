from flask import Blueprint, render_template

cats_bp = Blueprint('cats', __name__, template_folder='../templates')

cats_data = {
    'title': 'Все о кошках',
    'breeds': [
        {'name': 'Мейн-кун', 'description': 'Крупная порода с милыми кисточками на ушах.'},
        {'name': 'Сиамская', 'description': 'Элегантные кошки с голубыми глазами.'},
        {'name': 'Британская короткошерстная', 'description': 'Плюшевые котики, очень красивые.'}
    ],
    'care_tips': [
        'Регулярно расчесывать шерсть.',
        'Обеспечить когтеточкой.',
        'Игры и общение необходимы.'
    ]
}

@cats_bp.route('/cats')
def cats():
    return render_template('cats.html', data=cats_data)
