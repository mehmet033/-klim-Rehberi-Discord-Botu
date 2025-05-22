# 🌍 İklim Rehberi Botu

## Proje Hakkında
**İklim Rehberi Botu**, Discord sunucularında kullanıcıları iklim değişikliği hakkında bilinçlendirmek ve günlük çevreci alışkanlıklar kazandırmak amacıyla tasarlanmış bir bottur.

Bot, kullanıcılara her gün rastgele bir çevreci görev gönderir. Kullanıcılar bu görevleri tamamladığında puan kazanır, tamamlamadıklarında ise puan kaybeder. Puanlar haftalık ve aylık olarak sıralanır. Ayrıca kullanıcılar temel iklim bilgilerine ve istatistiklere bot üzerinden erişebilir.

## 🚀 Özellikler

- 🌱 **Günlük çevre dostu görevler** (örneğin: “Bugün musluğu açık bırakmadan diş fırçala”)
- 🔁 **Görev tamamlandığında puan kazanma**
- 😞 **Görev yapılmadığında puan kaybı**
- 🏆 **Liderlik sıralamaları**

## 🧪 Komutlar

| Komut | Açıklama |
|-------|----------|
| `!gorev kolay` | Kolay zorlukta görev verir |
| `!gorev orta` | Orta zorlukta görev verir |
| `!gorev zor` | Zor görev verir |
| `!yaptim` | Son alınan görevin tamamlandığını bildirir ve puan kazandırır |
| `!yapmadim` | Görev tamamlanmadıysa puan kaybettirir |
| `!puan` | Kullanıcının mevcut puanını gösterir |
| `!liderlik` | İlk 10 kullanıcıyı sıralı şekilde listeler |
| `!yardim` | Tüm kullanılabilir komutları listeler |

## 👨‍💻 Kullanılan Teknolojiler

- Python
- Discord.py kütüphanesi
- JSON (puan verisi için)
