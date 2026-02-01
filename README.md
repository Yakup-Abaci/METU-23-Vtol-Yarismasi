# METU-23-Vtol-Yarismasi
METU-23 yarışması için geliştirmiş olduğum çalışmam. Proje yarım kalmış olup tamamlanmamıştır. Yarışma içerisinde bir hedef alanının tespit edilmesi ve yük bırakılması görevi için yazıldı. HEdef nesnenin bulunması için OpenCV kullanıldır. Otonom uçuş için DroneKit ve MAVLink kullandım. Ardupilot kartı ile çalıştım. Kamera olarak SIYI R1M FPV kamera kullanıldı. 
Alanın tespitinden sonra VTOL aracının konuma doğru hareket etmesi sağlandı. İstenilen hedefin üzerine gelindiğinde ise alanın ortasına tam gelecek şekilde hizalama yapıldı. Daha sonrasında belirli bir metre iniş yaptıktan sonra hizalama işlemi tekrar gerçekleştirildi. Bu sayede her bir metrede alanın üstünde kalması sürekli hale getirilmiş olundu. Alanın bırakılması ile görev tamamlandı.

# Yarışma Alanı
<img width="500" height="500" alt="Image" src="https://github.com/user-attachments/assets/4629810a-8512-4bbc-b06d-825dbd98e347" />

# Hedef Alan
<img width="500" height="500" alt="Image" src="https://github.com/user-attachments/assets/336ceda3-7bdc-4963-a8e6-bbf4314a945b" />

# Otonom Uçuş
Otonom uçuş; Raspberry Pi 4 DIY bilgisayar kullanılarak ArduPilot yazılımı ile çalışan Pixhawk uçuş kontrolörü ile USB bağlantısı kurulmasıyla gerçekleştirildi. Uçuş kontrolörü ile Pixhawk arasındaki veri alışverişi, Python programlama dilini kullanan Pymavlink kütüphanesi ile kolaylaştırıldı. Araç parametre değerleri, ArduPilot tabanlı Mission Planner simülasyon uygulaması kullanılarak yapılandırıldı. Uçuş planı ve otonom uçuş, Dronekit kütüphanesi kullanılarak ve ArduPilot açık kaynak kod tabanından yararlanarak Python'da kodlandı. Kod içindeki Time kütüphanesi kullanılarak etkili zamanlama sağlandı. Yazılan uçuş komut dosyaları, en iyi sonuçları elde etmek için hem Mission Planner hem de Gazebo simülasyon ortamlarında test edildi. Sonuç olarak, olası kazalar proaktif olarak önlendi.

# Görüntü İşleme
Görüntü işleme için Raspberry Pi 4 kullanıldı ve Python programlama dili ile OpenCV ve NumPy kütüphaneleri kullanıldı. Şişelerin yerleştirilmesini kolaylaştırmak için OpenCV kütüphanesi kullanılarak renge göre hedef nokta belirlendi ve maskelendi, böylece yerleştirme alanı kameranın görüş alanına girdiğinde algılama iyileştirildi. Maskeleme tekniği, doğruluğu önemli ölçüde artırdı. NumPy kütüphanesi, çerçeveyi hesaplamak ve rengin kamera perspektifinde bulunduğu piksel koordinatlarını belirlemek için kullanıldı. Kameranın görüş alanı içindeki alanın konumunu hesaplayarak, VTOL için kırmızı bölgenin optimum merkezlenmesi sağlandı. Alanın boyutuna orantılı olarak, drone görüntü işlemeye dayalı olarak kendi kendine merkezlemeyi gerçekleştirdi.

