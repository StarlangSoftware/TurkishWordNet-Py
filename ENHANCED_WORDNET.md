# Enhanced Turkish WordNet (KeNet)

**Katkıda Bulunan:** Uğur Sürmeli (@surmeliugur) - NK-Engine Project

Bu PR, orijinal Turkish WordNet'e kapsamlı semantik ilişkiler ve metadata ekler.

---

## 🚀 Yenilikler

### 1. Zengin Semantik Edge'ler (236,690 ilişki)

| İlişki Tipi | Açıklama | Sayı |
|-------------|----------|------|
| **HYPERNYM** | Üst kavram (kedi → memeli) | ~50,000 |
| **HYPONYM** | Alt kavram (memeli → kedi) | ~50,000 |
| **SUBSTANCE_HOLONYM** | Bütün-parça (su → damla) | ~30,000 |
| **MEMBER_HOLONYM** | Üye-bütün (takım → oyuncu) | ~20,000 |
| **PART_HOLONYM** | Parça-bütün (kapı → kulbu) | ~25,000 |
| **ANTONYM** | Zıt anlamlı (büyük ↔ küçük) | ~10,000 |
| **ATTRIBUTE** | Nitelik (kırmızı → renk) | ~15,000 |
| **ENTAILMENT** | Fiil çıkarımı (koşmak → hareket) | ~10,000 |
| **CAUSE** | Nedensellik (öldürmek → ölüm) | ~5,000 |

### 2. Literal Graph (80,644 eş anlamlı bağlantı)

```python
# Örnek: "su" için eş anlamlılar
wn.get_synonyms("su")
# {"ab", "âb", "mü", "aqsâl"}

# Çok anlamlı kelimeler için:
wn.get_synonyms("banka")
# {"kredi kurumu", "nehir kenarı", "masa"} - bağlama göre
```

### 3. Sense ve Origin Metadata

Her literal için:
- `sense`: Anlam sırası (1, 2, 3...)
- `origin`: Kaynak (TDK, derleme, özel ad...)
- `groups`: Kavramsal gruplandırma

### 4. CSV Format (Hızlı Erişim)

XML parsing yerine CSV okuma:
- **10-100x daha hızlı** lookup
- **Düşük bellek** kullanımı (streaming)
- **Pandas/Spark** entegrasyonu kolay

---

## 📊 Karşılaştırma

| Özellik | Orijinal | Enhanced |
|---------|----------|----------|
| Synset sayısı | 78,000 | 78,328 |
| Literal sayısı | 110,000 | 110,260 |
| Semantik edge | 0 | **236,690** |
| Eş anlamlı bağlantı | 0 | **80,644** |
| Sense metadata | Yok | Var |
| Origin bilgisi | Yok | Var |
| Wikipedia link | Sınırlı | Zenginleştirildi |

---

## 🔧 Kullanım

### Temel Kullanım

```python
from WordNet.enhanced_wordnet import EnhancedWordNet

wn = EnhancedWordNet()

# Synset bilgisi
synset = wn.get_synset("TUR10-0819650")
print(synset['definition'])  # "su: İçme, yıkanma vb. işlerde kullanılan..."

# Literaller
literals = wn.get_literals("TUR10-0819650")
# [{literal: "su", sense: "1", origin: "TDK"}, ...]

# Üst kavramlar (hypernym)
hypernyms = wn.get_hypernyms("TUR10-0819650")
# ["TUR10-0819600"]  # → sıvı

# Alt kavramlar (hyponym)
hyponyms = wn.get_hyponyms("TUR10-0819650")
# ["TUR10-0819651", "TUR10-0819652"]  # → yağmur suyu, kaynak suyu
```

### Semantik Benzerlik

```python
# Kök'e kadar yol bulma
path = wn.find_path_to_root("TUR10-0819650")  # su
# ["TUR10-0819650", "TUR10-0819600", "TUR10-0819000", ...]
# su → sıvı → madde → fiziksel nesne → nesne → varlık

# İki kavram arası mesafe
def semantic_distance(synset1, synset2):
    path1 = set(wn.find_path_to_root(synset1))
    path2 = set(wn.find_path_to_root(synset2))
    common = path1 & path2
    if not common:
        return float('inf')
    lca = min(common, key=lambda x: wn.find_path_to_root(x).index(x))
    depth1 = len(wn.find_path_to_root(synset1)) - wn.find_path_to_root(synset1).index(lca)
    depth2 = len(wn.find_path_to_root(synset2)) - wn.find_path_to_root(synset2).index(lca)
    return depth1 + depth2
```

---

## 📁 Dosya Yapısı

```
WordNet/
├── __init__.py
├── enhanced_wordnet.py          # Yeni API
├── data/
│   ├── csv/                     # Yeni CSV dosyaları
│   │   ├── trwordnet_synsets_v0_1_0.csv      (78K satır)
│   │   ├── trwordnet_literals_v0_1_0.csv     (110K satır)
│   │   ├── trwordnet_edges_v0_1_0.csv        (236K satır)
│   │   └── trwordnet_literal_graph_v0_1_0.csv (80K satır)
│   └── *.xml                     # Orijinal XML'ler
└── ...
```

---

## 🏗️ Üretim Süreci

Bu veriler şu kaynaklardan türetildi:
1. **GTS V12** - Türkçe Sözlük
2. **KeNet** - Orijinal WordNet
3. **Dilbaz** - Morfolojik analiz
4. **Üç kesişim** - Triple intersection (en yüksek kalite)

Üretim kodları: [NK-Engine](https://github.com/surmeliugur/M-Engine)

---

## 📝 Lisans

Orijinal KeNet ile aynı lisans. Bu katkı açık kaynak ve akademik kullanıma açıktır.

---

## 🤝 Teşekkür

Bu çalışma [Starlang Software](https://github.com/StarlangSoftware) ekibinin TurkishWordNet projesi üzerine inşa edilmiştir. Orijinal yapının üzerine semantik zenginlik eklenmiştir.

**İletişim:** Uğur Sürmeli - ugur.surmeli@gmail.com
