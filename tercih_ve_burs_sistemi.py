print("\nÜNİVERSİTE TERCİH VE BURS UYGUNLUK SİSTEMİ")
print("------------------------------------------")

ogrenci_adi = "Ahmet"
puan = 435
siralama = 85000
butce = 18000
sehir_tercihi = "Ankara"
ingilizce_seviyesi = "B1"
hazirlik_istermi = True

ilgi_alanlari = ["yazılım", "yapay zeka", "veri"]

guclu_dersler = {"matematik", "fizik", "bilgisayar"}

orta_ve_ustu_ingilizce = ("B1", "B2", "C1", "C2")

yazilim = {
    "bolum": "Yazılım Mühendisliği",
    "sehir": "Ankara",
    "taban_puan": 410,
    "taban_siralama": 120000,
    "aylik_maliyet": 16000,
    "ingilizce_gereklimi": True,
    "hazirlik_varmi": True
}

veri_bilimi = {
    "bolum": "Veri Bilimi",
    "sehir": "İstanbul",
    "taban_puan": 400,
    "taban_siralama": 140000,
    "aylik_maliyet": 22000,
    "ingilizce_gerekli_mi": True,
    "hazirlik_var_mi": True
}

elektronik= {
    "bolum":"Elektrik-Elektronik Mühendisliği",
    "sehir":"Ankara",
    "taban_puan":420,
    "taban_siralama":100000,
    "aylik_maliyet":15000,
    "ingilizce_gerekli_mi":False,
    "hazirlik_var_mi":False
}

yazilim_puani = 0
veri_puani= 0
elektronik_puani = 0

if puan >= yazilim["taban_puan"]:
    yazilim_puani += 25
else:
    yazilim_puani -= 20

if siralama <= yazilim["taban_siralama"]:
    yazilim_puani += 25
else:
    yazilim_puani -= 15

if butce >= yazilim["aylik_maliyet"]:
    yazilim_puani += 15
else:
    yazilim_puani -= 10    

if sehir_tercihi == yazilim["sehir"]:
    yazilim_puani += 10

if "yazılım" in ilgi_alanlari or "yapay zeka" in ilgi_alanlari:
    yazilim_puani += 20

if "bilgisayar" in guclu_dersler and "matematik" in guclu_dersler:
    yazilim_puani +=15

if yazilim ["ingilizce_gereklimi"] == True:
    if ingilizce_seviyesi in orta_ve_ustu_ingilizce:
        yazilim_puani += 10
else: 
    yazilim_puani -= 10      

if hazirlik_istermi == yazilim["hazirlik_varmi"]:
    yazilim_puani += 5

if puan >= veri_bilimi["taban_puan"]:
    veri_puani += 25
else:
    veri_puani -=20

if siralama <= veri_bilimi["taban_siralama"]:
    veri_puani += 25
else:
    veri_puani -= 15

if butce >= veri_bilimi ["aylik_maliyet"]:
    veri_puani += 15    
else:
    veri_puani -=10

if sehir_tercihi == veri_bilimi["sehir"]:
    veri_puani += 10    

if "veri" in ilgi_alanlari or "yapay zeka" in ilgi_alanlari:
    veri_puani += 20

if "matematik" in guclu_dersler:
    veri_puani += 15

if veri_bilimi["ingilizce_gerekli_mi"] == True:

    if ingilizce_seviyesi in orta_ve_ustu_ingilizce:
        veri_puani += 10    
else:
    veri_puani -= 10

if hazirlik_istermi == veri_bilimi["hazirlik_var_mi"]:
    veri_puani += 5    

if puan >= elektronik["taban_puan"]:
    elektronik_puani += 25
else:
 elektronik_puani -= 20

if siralama <= elektronik["taban_siralama"]:
    elektronik_puani += 25
else:
    elektronik_puani -= 15

if butce >= elektronik["aylik_maliyet"]:
    elektronik_puani += 15
else:
    elektronik_puani -= 10

if sehir_tercihi == elektronik["sehir"]:
    elektronik_puani += 10

if "elektronik" in ilgi_alanlari or "donanım" in ilgi_alanlari:
    elektronik_puani += 20

if "fizik" in guclu_dersler and "matematik" in guclu_dersler:
    elektronik_puani += 20

if elektronik["ingilizce_gerekli_mi"] == True:
    if ingilizce_seviyesi in orta_ve_ustu_ingilizce:
     elektronik_puani += 10
    else:
        elektronik_puani -= 10
else:
    elektronik_puani += 5

if hazirlik_istermi == elektronik["hazirlik_var_mi"]:
    elektronik_puani += 5
else:
    elektronik_puani -= 3

print()    
print("Öğrenci Adı:",ogrenci_adi)
print("Puan:",puan)
print("Sıralama:",siralama)
print("Bütçe:",butce,"TL")
print("Şehir Tercihi:",sehir_tercihi)
print("İlgi Alanları:",ilgi_alanlari)
print("Güçlü Dersler:",guclu_dersler)
print("----------------------------")

print("Yazılım Mühendisliği Uygunluk Puanı:",yazilim_puani)
print("Veri Bilimi Uygunluk Puanı:",veri_puani)
print("Elektrik-Elektronik Uygunluk Puanı:",elektronik_puani)

print("----------------------------------------------------")

if yazilim_puani > veri_puani and yazilim_puani > elektronik_puani:
    onerilen_bolum = yazilim["bolum"]
    onerilen_sehir = yazilim["sehir"]
    en_yuksek_puan = yazilim_puani

elif veri_puani > yazilim_puani and veri_puani > elektronik_puani:
    onerilen_bolum = veri_bilimi["bolum"]
    onerilen_sehir = veri_bilimi["sehir"]
    en_yuksek_puan = veri_puani

elif elektronik_puani > yazilim_puani and elektronik_puani > veri_puani:
    onerilen_bolum = elektronik["bolum"]
    onerilen_sehir = elektronik["sehir"]
    en_yuksek_puan = elektronik_puani

else:
    onerilen_bolum = "Birden Fazla Bölüm Aynı Derecede Uygun"
    onerilen_sehir = "Kararsız"
    en_yuksek_puan = yazilim_puani

print("Önerilen Bölüm:",onerilen_bolum)
print("Önerilen Şehir:",onerilen_sehir)
print("Uygunluk Puanı:",en_yuksek_puan)

print("------------------------------")

if en_yuksek_puan >= 90:
    print("Yorum: Bu bölüm senin için çok uygun görünüyor.")
elif en_yuksek_puan >= 70:
    print("Yorum: Bu bölüm senin için uygun görünüyor.")
elif en_yuksek_puan >= 50:
    print("Yorum: Bu bölüm düşünülebilir ama bazı eksiklerin var.")
else:
    print("Yorum: Bu bölüm şu an için pek uygun görünmüyor.")

print("----------------------------------------------------")            
print("Burs değerlendirmesi")

if puan >= 430 and siralama <= 90000:
    print("Burs İhtimali: Yüksek burs alma ihtimalin var.")
elif puan >= 410 and siralama <= 120000:
    print("Burs İhtimali: Orta seviyede burs alma ihtimalin var.")    
else:
    print("Burs İhtimali: Burs ihtimalin çok düşük olabilir.")

print("-----------------------------------------------------")
print("Kariyer Önerisi")

if onerilen_bolum == "Yazılım Mühendisliği":
    print("Python, algoritma, web geliştirme ve proje üretmeye odaklanmalısın.")

elif onerilen_bolum == "Veri Bilimi":
    print("Python, matematik, istatistik ve veri analizi çalışmalısın.")

elif onerilen_bolum == "Elektrik-Elektronik Mühendisliği":
    print("Fizik, elektronik devreler, gömülü sistemler ve C programlama çalışmalısın.")

else:
    print("Bölümleri tekrar karşılaştırıp ilgi alanlarına göre karar vermelisin.")