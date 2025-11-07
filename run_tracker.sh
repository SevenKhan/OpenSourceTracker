#!/bin/bash

# Repo dizinine geç
cd ~/OpenSourceTracker_clean || exit

# Virtual environment aktif et
source venv/bin/activate

# Gerekli Python paketlerini yükle
pip install --upgrade pip
pip install PyGithub requests

# Tracker.py çalıştır
python tracker.py

# README güncelle (varsa)
python update_readme.py

# Git işlemleri
git add .
git commit -m "Auto update tracker output and README" 2>/dev/null

# Önce remote değişiklikleri al ve rebase yap
git pull --rebase origin main

# Push
git push

echo "Tracker ve README güncellemesi tamamlandı!"
