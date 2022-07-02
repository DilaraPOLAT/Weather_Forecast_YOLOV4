# Weather_Forecast_YOLOV4
**Özgün Değer**

Hava Durumu Tahmini Uygulaması hava durumu (yağmurlu, güneşli, bulutlu) veri seti toplanıp gerekli etiketlemeler ve düzenlemeler yapılarak eğitimi gerçekleşecektir. Havada bulut var ise hava bulutlu, havada bulut yok ise güneşli, bulutlar kara ise yağmurlu olarak model eğitilecektir. Oluşturulan veri seti YoloV4 algoritması kullanılarak fotoğraftan bulutların şekli, büyüklüğü ve rengine göre havanın durumu tespit edilecektir. Tespit edilen hava durumu Python programlama diliyle yazılacak arayüz PyQt kullanılacaktır. PyQt çapraz platform uygulama geliştirmeye yarayan ve C++ ile yazılmış olan Qt kütüphanesinin Python bağlamasıdır. Konum bilgilerine göre gerçek hava değerlerine ulaşılabilecek ve kullanıcı tahmin edilen hava durumuyla karşılaştırabilecektir. Projeye sesli asistan ekleyerek istenilen şehrin hava durumunu sesli bir şekilde de öğrenebilecektir.
**Projenin Amacı ve Hedefi**

Projenin amacı çekilen havanın görüntüsüne göre hava durumunu anlık belirleme. Kullanıcı çektiği gökyüzü fotoğrafıyla havanın yağmurlu mu, karlı mı, bulutlu mu, güneşli mi olduğunu anlayabilecek. Bulutların görüntüsüne (şekline ve büyüklüğüne, rengine vb.) göre hava durumu doğru tespit edilip edilmeyeceğini lokasyondaki gerçek değerle karşılaştırılarak öğrenebilecektir. 


#Kullanılan Teknolojiler
* Python
* OpenCV
* PyQT5
* PyAudio
* SpeechRecognition
* gTTS
* playsound
* Requests
* Beautifulsoup


***Etiketleme İşlemini Yaptığım Site***


![image](https://user-images.githubusercontent.com/59871974/177015873-b49fc5e1-e460-4a50-a807-3ea10bd575f9.png)


***Darknet Dosyamın İçinde Bulunan Weather Data Klasörü***


![image](https://user-images.githubusercontent.com/59871974/177015833-ecc7efcf-1bbb-458a-9bfc-cf3f81c27494.png)


***Eğitim Sonucunda Oluşan Chart Grafiği***


![image](https://user-images.githubusercontent.com/59871974/177015800-1a7bedfa-c2a4-4d99-bc54-a07222cf3b6e.png)


***YOLOV4 Eğitim Sonrası Elde Edilen Ağırlıklardan Test Sonuçları***


![image](https://user-images.githubusercontent.com/59871974/177015695-b21af239-8281-41e9-880f-b3ca7ff571d3.png)

![image](https://user-images.githubusercontent.com/59871974/177015721-580df4ec-e80b-4966-a4b6-abb19029b57a.png)

![image](https://user-images.githubusercontent.com/59871974/177015731-5afde862-fa52-4d37-bfa9-14575350d989.png)


***PyQt Arayüz Bağlanması ve Projenin Son Hali***


![image](https://user-images.githubusercontent.com/59871974/177015783-5a43fd65-3876-4919-b2b0-36df07a040cf.png)

![image](https://user-images.githubusercontent.com/59871974/177015787-8dcc6582-02d7-428c-95e7-14cc4a6ed46f.png)

![image](https://user-images.githubusercontent.com/59871974/177015789-432118bb-99f0-4a6f-ac41-b026e941036d.png)

![image](https://user-images.githubusercontent.com/59871974/177015794-b3816fa0-daa3-4c27-bef9-e574b874fc97.png)

