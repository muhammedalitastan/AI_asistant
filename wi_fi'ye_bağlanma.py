import subprocess

def connect_to_wifi(ssid, password):
    # Bağlanmak istediğiniz Wi-Fi ağına bağlanmak için netsh komutunu kullanıyoruz
    try:
        print(f"{ssid} ağına bağlanıyor...")
        
        # Wi-Fi bağlantısını başlatmak için komut
        command = f'netsh wlan set hostednetwork mode=allow ssid="{ssid}" key="{password}"'
        
        # Komutu çalıştırıyoruz
        subprocess.run(command, shell=True, check=True)
        
        # Bağlantıyı başlatmak için Wi-Fi bağlantısını başlatma komutu
        start_command = 'netsh wlan start hostednetwork'
        subprocess.run(start_command, shell=True, check=True)
        
        print(f"{ssid} ağına başarıyla bağlanıldı.")
    except subprocess.CalledProcessError as e:
        print(f"Bir hata oluştu: {e}")

# Kullanıcıdan Wi-Fi bilgilerini alıyoruz
ssid = input("Wi-Fi ağı adını (SSID) girin: ")
password = input("Wi-Fi ağının parolasını girin: ")

connect_to_wifi(ssid, password)
