#!/bin/bash

# Kullanıcıdan commit mesajını al
read -p "Commit mesajını gir: " commit_msg

# SSH remote URL kontrol (zaten ayarlıysa sorun yok)
git remote set-url origin git@github.com:SevenKhan/OpenSourceTracker.git

# Tüm değişiklikleri ekle
git add .

# Commit yap
git commit -m "$commit_msg"

# Push et
git push -u origin main

echo "Push tamamlandı! 🚀"
