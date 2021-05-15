const TelegramBot = require('node-telegram-bot-api');
const token = '1895811339:AAHnvHT5EANaMf53eW0ZoP-d8vQR8Adu0g0';
const bot = new TelegramBot(token, {polling: true});

bot.on('message', (msg) => {
    let Hi = "hi";
    if (msg.text.toString().toLowerCase().indexOf(Hi) === 0) {
        bot.sendMessage(msg.chat.id,"Hello dear user");
    }
});