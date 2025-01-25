# Hugging Face ve Selenium ile Web Test Otomasyonu

Bu proje, Selenium ve Hugging Face modelleri kullanarak bir web sayfasındaki metinleri analiz etmeyi amaçlamaktadır. Selenium ile web sayfasına gidilir, metinler alınır ve Hugging Face'in duygu analiz modeli kullanılarak bu metinlerin duygu durumu analiz edilir.

## Proje Yapısı

- `models/model.py`: Selenium ve Hugging Face modelini kullanarak web sayfasını ziyaret etme ve içerikleri analiz etme.
- `tests/test_website.py`: Web sitesine gidip test senaryolarını çalıştırma.
- `requirements.txt`: Gerekli bağımlılıklar.

## Gereksinimler

Bağımlılıkları yüklemek için:

```bash
pip install -r requirements.txt
