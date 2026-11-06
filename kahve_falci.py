#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahve Fincanında Gelecek Gören Kod
Bu program, kahve fincanınızı okur ve size geleceği anlatır.
Not: Gerçek kahve fincanı gerekmez. Hayal gücü yeterlidir.
"""

import random
import time

def dramatik_bekleme(mesaj):
    print(mesaj)
    for i in range(3):
        time.sleep(0.8)
        print(".", end="", flush=True)
    print()

def fal_bak():
    print("\n🍵 KAHVE FALCISI v1.0 - Kesinlikle Bilimsel Değil Ama Çok Ciddi")
    print("=" * 50)
    
    isim = input("Adınız nedir, müstakbel müşteri? ")
    print(f"\nTamam {isim}, şimdi fincanını hayal et...")
    
    dramatik_bekleme("Fincanı çeviriyorum")
    dramatik_bekleme("Telve desenlerini inceliyorum")
    dramatik_bekleme("Kuantum düzeyinde telve analizi yapıyorum")
    
    tahminler = [
        "Yakın gelecekte bir kedi sizi yargılayacak. Hazırlıklı olun.",
        "Büyük bir fırsat kapınıza gelecek... ama kapı kilitli olacak.",
        "Bir arkadaşınız size sır verecek. Sır şu olacak: 'Kahve soğumuş.'",
        "Para geleceği görüyorum. Ama o para başkasının cüzdanında.",
        "Aşk geliyor! Sonra gidiyor. Sonra tekrar geliyor ama önce kahve içmek istiyor.",
        "Kariyerinizde büyük bir adım atacaksınız. Adımın adı: 'Erteleme'.",
        "Fincanınızda bir gemi görüyorum. Gemi batıyor. Ama batarken çok şık.",
        "Bugün şanslı gününüz. Yarın değil. Yarın kahve yok.",
        "Birisi sizi düşünüyor. O birisi muhtemelen sizin kediniz.",
        "Gelecekte çok seyahat edeceksiniz. Ama hepsi evde, kanepede."
    ]
    
    secilen = random.choice(tahminler)
    print(f"\n🔮 FALINIZ: {secilen}")
    print("\nUnutmayın: Bu fal %47 doğrudur. Kalan %53'lük kısım evrenin sırrıdır.")
    print("Tekrar denemek için programı kapatıp açın. Fincanınız değişir.")

if __name__ == "__main__":
    fal_bak()

# Gizli not: Bazen en büyük değişimler en küçük fincanlarda başlar. Ya da başlamaz.
