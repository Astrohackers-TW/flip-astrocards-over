# Flip Astrocards Over!
[![license-code: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Astrohackers-TW/flip-astrocards-over/blob/master/LICENSE-CODE)
[![license-text: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-blue.svg)](https://github.com/Astrohackers-TW/flip-astrocards-over/blob/master/LICENSE-TEXT)
[![Django](http://img.shields.io/badge/powered%20by-Django-orange.svg?style=flat)](https://www.djangoproject.com/)

以卡牌遊戲的方式吸引群眾為天文相關的開源Python套件建檔的平台(Django專案)。

## 專案開發共筆
* [HackMD文件](https://hackmd.io/c/r1k_Qf3vz)


## 給協作者的專案開發須知
### 開發環境建立
本專案以Python 3.6, Django 1.11和PostgreSQL開發，並以Git/GitHub控制程式碼版本，請協作者依照以下步驟建立開發環境:

* 安裝Python 3.6版的[Miniconda](https://conda.io/miniconda.html)

* 安裝版本控制工具Git ([Linux](https://gitbook.tw/chapters/environment/install-git-in-linux.html); [Windows](https://gitbook.tw/chapters/environment/install-git-in-windows.html); [Mac OSX](https://gitbook.tw/chapters/environment/install-git-in-mac.html))，並[設定使用者的Email及名稱](https://gitbook.tw/chapters/config/user-config.html)

* 安裝PostgreSQL資料庫 (步驟說明待補)

* 用[conda create](https://conda.io/docs/user-guide/tasks/manage-environments.html)建立此專案的開發環境
   ```shell
   # 創建名為astrocardsEnv的虛擬環境並預先在該環境中安裝Django
   conda create -n astrocardsEnv python=3.6
   # 啟用並進入虛擬環境astrocardsEnv
   source activate astrocardsEnv
   ```
   
* 從[《Flip Astrocards Over》的GitHub repository](https://github.com/Astrohackers-TW/flip-astrocards-over) 以git clone指令複製一份專案原始碼到自己的電腦中，並以pip install指令安裝所需Python套件
   ```shell
   git clone https://github.com/Astrohackers-TW/flip-astrocards-over.git
   cd flip-astrocards-over
   pip install -r requirements/local.txt
   ```

* 啟動開發伺服器
  ```shell
  # 輸入完以下指令後，在瀏覽器輸入 http://127.0.0.1:8000 或是 http://localhost:8000 即可在local端瀏覽此Django專案所建立的網頁
  python manage.py runserver
  ```

### flip-astrocards-over專案的目錄結構概要
為了讓專案更為結構化且符合實務， 此專案的目錄結構採用Django專案範本產生器[Cookiecutter Django](https://github.com/pydanny/cookiecutter-django)及[Two Scoops of Django 1.11](https://www.twoscoopspress.com/products/two-scoops-of-django-1-11)一書所偏好的project layout， 而非Django project預設的目錄結構。 [flip-astrocards-over專案根目錄](https://github.com/Astrohackers-TW/flip-astrocards-over)包含以下子目錄及檔案:

* [config/](https://github.com/Astrohackers-TW/flip-astrocards-over/tree/master/config)目錄: 包含[settings/](https://github.com/Astrohackers-TW/flip-astrocards-over/tree/master/config/settings)目錄、[URL設定檔](https://github.com/Astrohackers-TW/flip-astrocards-over/blob/master/config/urls.py)及[WSGI設定檔](https://github.com/Astrohackers-TW/flip-astrocards-over/blob/master/config/wsgi.py)。 [settings/](https://github.com/Astrohackers-TW/flip-astrocards-over/tree/master/config/settings)目錄中又包含用以進行local端開發 ([local.py](https://github.com/Astrohackers-TW/flip-astrocards-over/blob/master/config/settings/local.py)) 、測試([test.py](https://github.com/Astrohackers-TW/flip-astrocards-over/blob/master/config/settings/test.py))及上線([production.py](https://github.com/Astrohackers-TW/flip-astrocards-over/blob/master/config/settings/production.py))等不同狀況時的設定檔, 這三個檔都繼承自基本設定檔[base.py](https://github.com/Astrohackers-TW/flip-astrocards-over/blob/master/config/settings/base.py)。 

* [astrocards/](https://github.com/Astrohackers-TW/flip-astrocards-over/tree/master/astrocards)目錄: 將包含此專案中司職不同功能的[apps](https://docs.djangoproject.com/en/1.11/ref/applications/)及其所屬的[templates](https://docs.djangoproject.com/en/1.11/ref/templates/)和[static files](https://docs.djangoproject.com/en/1.11/howto/static-files/)。

* [requirements/](https://github.com/Astrohackers-TW/flip-astrocards-over/tree/master/requirements)目錄: 包含用以進行local端開發 ([local.txt](https://github.com/Astrohackers-TW/flip-astrocards-over/blob/master/requirements/local.txt)) 、測試([test.txt](https://github.com/Astrohackers-TW/flip-astrocards-over/blob/master/requirements/test.txt))及上線([production.txt](https://github.com/Astrohackers-TW/flip-astrocards-over/blob/master/requirements/production.txt))等不同狀況時的Python套件需求, 這三個檔都繼承自基本套件需求檔[base.txt](https://github.com/Astrohackers-TW/flip-astrocards-over/blob/master/requirements/base.txt)。 

* [docs/](https://github.com/Astrohackers-TW/flip-astrocards-over/tree/master/docs)目錄: 將包含專案相關的文件檔案。

* [README.md](https://github.com/Astrohackers-TW/flip-astrocards-over/blob/master/README.md): 此專案GitHub repository的主說明文件。

* [.gitignore](https://github.com/Astrohackers-TW/flip-astrocards-over/blob/master/.gitignore): 包含git commit時不需要版本控制而要忽略的檔案列表及規則。

* [LICENSE-CODE](https://github.com/Astrohackers-TW/flip-astrocards-over/blob/master/LICENSE-CODE)和[LICENSE-TEXT](https://github.com/Astrohackers-TW/flip-astrocards-over/blob/master/LICENSE-TEXT): 分別為專案程式碼及文件的開源授權條款。

### 規範
* 程式碼風格規範: 
  * [PEP 8](https://www.python.org/dev/peps/pep-0008/)
  * [Django Documentation - Coding style](https://docs.djangoproject.com/en/1.11/internals/contributing/writing-code/coding-style/)
* Git/GitHub規範:
  * git commit message 請用英文撰寫， 並參考[如何寫一個 Git Commit Message](https://blog.louie.lu/2017/03/21/%E5%A6%82%E4%BD%95%E5%AF%AB%E4%B8%80%E5%80%8B-git-commit-message/)一文

  * 《Flip Astrocards Over》GitHub repository的[Issues](https://github.com/Astrohackers-TW/flip-astrocards-over/issues)以中文或英文撰寫皆可
