from selenium import webdriver
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  

chrome_options = webdriver.ChromeOptions()    

options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

class TestFormElements:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(options = chrome_options)
        cls.driver.get("http://localhost:5000")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_nama_label(self):
        nama_label = self.driver.find_element(By.XPATH, "//label[@for='nama']")
        assert nama_label.text == "Nama:", "Pengecekan Nama gagal"

    def test_nim_label(self):
        nim_label = self.driver.find_element(By.XPATH, "//label[@for='nim']")
        assert nim_label.text == "NIM:", "Pengecekan NIM gagal"

    def test_mata_kuliah_label(self):
        mata_kuliah_label = self.driver.find_element(By.XPATH, "//label[@for='mata_kuliah']")
        assert mata_kuliah_label.text == "Mata Kuliah:", "Pengecekan Mata Kuliah gagal"

    def test_jurusan_label(self):
        jurusan_label = self.driver.find_element(By.XPATH, "//label[@for='jurusan']")
        assert jurusan_label.text == "Jurusan:", "Pengecekan Jurusan gagal"

if __name__ == "__main__":
    pytest.main()