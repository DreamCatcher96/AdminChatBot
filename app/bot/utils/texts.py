from abc import abstractmethod, ABCMeta

# Add other languages and their corresponding codes as needed.
# You can also keep only one language by removing the line with the unwanted language.
SUPPORTED_LANGUAGES = {
    #"ru": "🇷🇺 Русский",
    "en": "🇬🇧 English",
}


class Text(metaclass=ABCMeta):
    """
    Abstract base class for handling text data in different languages.
    """

    def __init__(self, language_code: str) -> None:
        """
        Initializes the Text instance with the specified language code.

        :param language_code: The language code (e.g., "ru" or "en").
        """
        self.language_code = language_code if language_code in SUPPORTED_LANGUAGES.keys() else "en"

    @property
    @abstractmethod
    def data(self) -> dict:
        """
        Abstract property to be implemented by subclasses. Represents the language-specific text data.

        :return: Dictionary containing language-specific text data.
        """
        raise NotImplementedError

    def get(self, code: str) -> str:
        """
        Retrieves the text corresponding to the provided code in the current language.

        :param code: The code associated with the desired text.
        :return: The text in the current language.
        """
        return self.data[self.language_code][code]


class TextMessage(Text):
    """
    Subclass of Text for managing text messages in different languages.
    """

    @property
    def data(self) -> dict:
        """
        Provides language-specific text data for text messages.

        :return: Dictionary containing language-specific text data for text messages.
        """
        return {
            "en": {
                "select_language": "👋 <b>Hello</b>, {full_name}!\n\nSelect language:",
                "change_language": "<b>Select language:</b>",
                "main_menu": "<i><b>Hello {full_name} 👋 I am Online,\n\n Chat With Admin Here!\n\nNB : ഇവിടെ മൂവിയുടെ പേര് എഴുതി അയച്ചിട്ട് കാര്യം ഇല്ല, ഇത് മൂവി കിട്ടുന്ന ബോട്ട് അല്ല , അഡ്മിനുമായി സംസാരിക്കുന്ന ബോട്ട് ആണ്..!!\n\n Use ➲ @FileSearch2Bot For Movies</b></i>",
                "message_sent": "<i><b>Message Sent to Admin ✅\n\nReplay Will Be Given Once Admin Comes Online..!! 🙊\n\nഅഡ്മിൻ ഓൺലൈനിൽ വന്നാൽ റീപ്ലേ തരുന്നതാണ്..!! 💥</b></i>",
                "message_edited": (
                    "<b>The message was edited only in your chat.</b> "
                    "To send an edited message, send it as a new message."
                ),
                "source": (
                    "Source code available at "
                    
                ),
                "user_started_bot": (
                    "<b>User {name} started the bot!</b>\n\n"
                    "• /ban\n"
                    "• /silent\n"
                    "• /information\n\n"
                    "<code>𝐁𝐨𝐭 𝐋𝐢𝐧𝐤  ➠ https://telegram.me/FileSearch2Bot\n\n𝐆𝐫𝐨𝐮𝐩 𝟏 𝐋𝐢𝐧𝐤 ➠ https://t.me/+EJh5yV8msmYzYTNk\n\n𝐆𝐫𝐨𝐮𝐩 𝟐 𝐋𝐢𝐧𝐤 ➠ https://t.me/+eNoYW8ufodY1ZTA1\n\n𝐎𝐓𝐓 𝐔𝐩𝐝𝐚𝐭𝐞 ➠ https://t.me/+HtbNlbLWliw1MDhk</code>\n\n"
                    "<code>⚠️ മൂവി കിട്ടാൻ @FileSearch2Bot 👈 ഇതിൽ പോയി നിങ്ങൾക്ക് ആവശ്യമുള്ള മൂവിയുടെ പേര് മെസ്സേജ് അയക്കുക..!!\n\n 📌NOTE : നിങ്ങൾ അയക്കുന്ന മൂവിയുടെ പേരിൻ്റെ സ്പെല്ലിംങ്ങ് Googlil ഉള്ളത് പോലെ ആണോ എന്ന് കൂടെ ഉറപ്പ് വരുത്തുക..!!</code>\n\n"
                    "<code>𝗣𝗹𝗲𝗮𝘀𝗲 𝗚𝗼 𝘁𝗼 👉 @FileSearch2Bot 𝗮𝗻𝗱 𝗦𝗲𝗻𝗱 𝗬𝗼𝘂𝗿 𝗠𝗼𝘃𝗶𝗲 𝗡𝗮𝗺𝗲 𝗪𝗶𝘁𝗵 𝗖𝗼𝗿𝗿𝗲𝗰𝘁 𝗚𝗼𝗼𝗴𝗹𝗲 𝗦𝗽𝗲𝗹𝗹𝗶𝗻𝗴..!!</code>"
                ),
                "user_restarted_bot": "<b>User {name} restarted the bot!</b>",
                "user_stopped_bot": "<b>User {name} stopped the bot!</b>",
                "user_blocked": "<b>User blocked!</b> Messages from the user are not accepted.",
                "user_unblocked": "<b>User unblocked!</b> Messages from the user are being accepted again.",
                "blocked_by_user": "<b>Message not sent!</b> The bot has been blocked by the user.",
                "user_information": (
                    "<b>ID:</b>\n"
                    "- <code>{id}</code>\n"
                    "<b>Name:</b>\n"
                    "- {full_name}\n"
                    "<b>Status:</b>\n"
                    "- {state}\n"
                    "<b>Username:</b>\n"
                    "- {username}\n"
                    "<b>Blocked:</b>\n"
                    "- {is_banned}\n"
                    "<b>Registration date:</b>\n"
                    "- {created_at}"
                ),
                "message_not_sent": "<b>Message not sent!</b> An unexpected error occurred.",
                "message_sent_to_user": "<b>Message sent to user!</b>",
                "silent_mode_enabled": (
                    "<b>Silent mode activated!</b> Messages will not be delivered to the user."
                ),
                "silent_mode_disabled": (
                    "<b>Silent mode deactivated!</b> The user will receive all messages."
                ),
            },
            "ru": {
                "select_language": "👋 <b>Привет</b>, {full_name}!\n\nВыберите язык:",
                "change_language": "<b>Выберите язык:</b>",
                "main_menu": "<b>Оставьте свой вопрос</b>, и мы ответим вам в ближайшее время:",
                "message_sent": "<b>Сообщение отправлено!</b> Ожидайте ответа.",
                "message_edited": (
                    "<b>Сообщение отредактировано только в вашем чате.</b> "
                    "Чтобы отправить отредактированное сообщение, отправьте его как новое сообщение."
                ),
                "source": (
                    "Исходный код доступен на "
                    "<a href=\"https://github.com/nessshon/support-bot\">GitHub</a>"
                ),
                "user_started_bot": (
                    "<b>Пользователь {name} запустил(а) бота!</b>\n\n"
                    "Список доступных команд:\n\n"
                    "• /ban\n"
                    "Заблокировать/Разблокировать пользователя"
                    "<blockquote>Заблокируйте пользователя, если не хотите получать от него сообщения.</blockquote>\n\n"
                    "• /silent\n"
                    "Активировать/Деактивировать тихий режим"
                    "<blockquote>При включенном тихом режиме сообщения не отправляются пользователю.</blockquote>\n\n"
                    "• /information\n"
                    "Информация о пользователе"
                    "<blockquote>Получить сообщение с основной информацией о пользователе.</blockquote>"
                ),
                "user_restarted_bot": "<b>Пользователь {name} перезапустил(а) бота!</b>",
                "user_stopped_bot": "<b>Пользователь {name} остановил(а) бота!</b>",
                "user_blocked": "<b>Пользователь заблокирован!</b> Сообщения от пользователя не принимаются.",
                "user_unblocked": "<b>Пользователь разблокирован!</b> Сообщения от пользователя вновь принимаются.",
                "blocked_by_user": "<b>Сообщение не отправлено!</b> Бот был заблокирован пользователем.",
                "user_information": (
                    "<b>ID:</b>\n"
                    "- <code>{id}</code>\n"
                    "<b>Имя:</b>\n"
                    "- {full_name}\n"
                    "<b>Статус:</b>\n"
                    "- {state}\n"
                    "<b>Username:</b>\n"
                    "- {username}\n"
                    "<b>Заблокирован:</b>\n"
                    "- {is_banned}\n"
                    "<b>Дата регистрации:</b>\n"
                    "- {created_at}"
                ),
                "message_not_sent": "<b>Сообщение не отправлено!</b> Произошла неожиданная ошибка.",
                "message_sent_to_user": "<b>Сообщение отправлено пользователю!</b>",
                "silent_mode_enabled": (
                    "<b>Тихий режим активирован!</b> Сообщения не будут доставлены пользователю."
                ),
                "silent_mode_disabled": (
                    "<b>Тихий режим деактивирован!</b> Пользователь будет получать все сообщения."
                ),
            },
        }
