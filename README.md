# Python+Selenium 網址轉換經緯度批次處理程式
* 此程式使用 Python 和 Selenium，針對網路上提供的地址轉換經緯度服務進行模擬人為操作，達到批次處理的效果。

# 如何使用
1. Git此專案至您的本機端。
2. 在您的電腦上安裝 Python 和 Selenium 。
3. 在 batch_convert.py 可以修改、設定網址轉換經緯度服務的網址、輸入欄位的 XPath 等相關設定。
4. 將您要批次處理的地址清單存放在 input.txt中，每行一個地址。
5. 在終端機中切換至此專案所在的目錄，執行 python batch_convert.py。
6. 程式會自動模擬人為操作，將每個地址輸入網頁中並取得經緯度結果，最後存放在 output.txt 中。
# 注意事項
* 程式預設使用 Chrome 瀏覽器，您需要先安裝 Chrome 瀏覽器並下載對應版本的 ChromeDriver。
* 請勿過度使用此程式，以免造成網站伺服器負擔過大或 IP 被封鎖等問題。
* 本程式僅供學習和研究使用，請勿用於商業用途或不當用途。
# 授權
* 本程式採用 MIT 授權，詳細內容請參閱 LICENSE 檔案。

# 成果展示
*![image](https://user-images.githubusercontent.com/33368807/231086862-3e471e18-871d-420e-bf48-785ed98a12bc.png)

