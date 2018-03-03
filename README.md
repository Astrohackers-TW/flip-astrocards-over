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
(待補)

### 規範
* 程式碼風格規範: 
  * [PEP 8](https://www.python.org/dev/peps/pep-0008/)
  * [Django Documentation - Coding style](https://docs.djangoproject.com/en/1.11/internals/contributing/writing-code/coding-style/)
* Git/GitHub規範:
  * git commit message 請用英文撰寫， 並參考[如何寫一個 Git Commit Message](https://blog.louie.lu/2017/03/21/%E5%A6%82%E4%BD%95%E5%AF%AB%E4%B8%80%E5%80%8B-git-commit-message/)一文

  * 《Flip Astrocards Over》GitHub repository的[Issues](https://github.com/Astrohackers-TW/flip-astrocards-over/issues)以中文或英文撰寫皆可
