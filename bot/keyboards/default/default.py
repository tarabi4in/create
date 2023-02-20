from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from loader import _
from models import User


def get_default_markup(user):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    markup.add(_('Интеллект'), _('Воображение'), _('Аккаунт'), _('О Нас'), _('Damn'))
    
    if user.is_admin:
        markup.add(_('Export users 📁'))
        markup.add(_('Count users 👥'))
        markup.add(_('Count active users 👥'))

    if len(markup.keyboard) < 1:
        return ReplyKeyboardRemove()

    return markup

