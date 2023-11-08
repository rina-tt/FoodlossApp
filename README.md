# 概要
2023/08/21-2023/08/25　楽天グループ主催の短期インターンシップに参加した際に作成したWebアプリのコードです。

## インターン概要
- タイトル：Summer Short Internship 2023　〜夏の陣オンライン〜
- 期間：2023/08/21-2023/08/25
- 使用技術:Python、Streamlit、Docker、SQLite、Vision API、Rakuten API
- テーマ：フードロス解決に貢献できるプロダクトを各チームで開発
- 
## アプリ概要
- 解決する課題：家庭系食品ロスのうち、直接廃棄
- 原因：買いすぎ、消費期限の把握不足、レシピがわからない
- 解決する方法：在庫を管理する、消費期限が近い食材を通知する、レシピを推薦して消費を促す
- 基本機能：在庫登録、確認、編集、削除、レシート読み込み、消費とロスの金額をグラフ表示、期限切れが近い食品を用いたレシピの提案
- URL：https://foodlossapp-qtzdd49irr2mxuigj3mkdd.streamlit.app/

### ログイン画面
<img width="1128" alt="home" src="https://github.com/rina-tt/FoodlossApp/assets/71320379/4e134e25-d25a-4ab2-b207-0057257ac0d1">

### レシピ推薦
消費期限が最も早い、すぐに消費するべき食材を使うレシピを優先して表示します。
<img width="1122" alt="recipe" src="https://github.com/rina-tt/FoodlossApp/assets/71320379/e5469c2d-5444-4a37-8ac3-4b0b7e859933">

### 在庫追加画面
<img width="1127" alt="add_stock" src="https://github.com/rina-tt/FoodlossApp/assets/71320379/41930f47-0718-48c3-ba6b-07765df060db">

<!--## 現在確認されている不具合・改善点
- [ ] レシピの「もっと見る」を押した際に表示が途切れる場合がある
- [ ] ユーザー名を入力する前に「Recipe」や「Stock」のページに遷移すると中途半端なエラーメッセージが表示される
- [ ]　
- [ ]
-->
