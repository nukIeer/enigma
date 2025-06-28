
# Enigma Makinesi Simülatörü ve Brute-Force Kırıcı (Python)

Bu proje, II. Dünya Savaşı sırasında Alman ordusu tarafından kullanılan **Enigma şifreleme makinesinin** temel işleyişini modelleyen ve aynı zamanda basitleştirilmiş bir brute-force kırma algoritması içeren bir Python uygulamasıdır.

## 🔧 Özellikler

- 3 rotorlu klasik Enigma modeline uygun şifreleme ve çözme
- Rotor sıralaması ve başlangıç pozisyonlarının özelleştirilebilir olması
- Reflector B kullanımı
- Basit rotor stepping (yalnızca dış rotor döner)
- Plugboard ve ring ayarı olmadan sadeleştirilmiş yapı
- Crib (önceden bilinen açık metin parçası) tabanlı brute-force çözüm algoritması
- Tüm kod tek bir `main.py` dosyasındadır

## 🧠 Teknik Arka Plan

Enigma makinesi, harfleri karmaşık bir rotorlama ve yansıma (reflector) sistemi üzerinden geçirerek şifreleme yapar. Her mesaj, farklı rotor pozisyonlarıyla başlatıldığından şifreleme sonuçları değişkenlik gösterir. Bu uygulama, rotor dönüşü, reflektör kullanımı ve ters yansıma gibi temel işlevleri içerir.

Crib-based kırma algoritması, kullanıcı tarafından bilinen kısa bir açık metin (ör. `"WETTER"`) parçasını kullanarak, şifreli mesaj üzerinde rotor dizilimleri ve pozisyonlarının tüm olası kombinasyonlarını dener. Doğru kombinasyon bulunduğunda açık mesaj geri elde edilir.

## 🚀 Kullanım

### 1. Bağımlılıklar

Herhangi bir harici bağımlılık bulunmamaktadır. Python 3.x yeterlidir.

### 2. Çalıştırma

```bash
python main.py

Program:

Örnek bir açık mesajı Enigma algoritmasıyla şifreleyecek,

Daha sonra, bu mesajı brute-force yöntemle çözecektir.

```
📂 Dosya Yapısı

main.py         # Tüm kodun bulunduğu tek Python dosyası
README.md       # Bu açıklama dosyası

⚠️ Sınırlamalar

Plugboard (steckerbrett) desteği yoktur.

Rotor halkası (Ringstellung) ayarları uygulanmamıştır.

Gerçek Enigma'da bulunan rotor geçişleri (double-stepping) bu sürümde basitleştirilmiştir.

Brute-force çözüm süresi tam rotor/pozisyon kombinasyonlarına göre uzayabilir.


📜 Lisans

Bu proje, eğitim ve akademik kullanım amacıyla MIT lisansı altında sunulmuştur.

✍️ Yazar

Bu simülasyon, tarihi şifreleme sistemlerinin temel prensiplerini öğretmek amacıyla hazırlanmıştır. Katkı sağlamak veya genişletmek isterseniz, pull request göndermekten çekinmeyin.
