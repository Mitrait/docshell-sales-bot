#!/usr/bin/env bash
# start.sh

set -e

echo "Запуск бота..."
python -m venv venv 2>/dev/null || true
source venv/bin/activate 2>/dev/null || . venv/Scripts/activate

pip install --upgrade pip
pip install -r requirements.txt

echo "Установка завершена. Стартуем бот..."
python main.py