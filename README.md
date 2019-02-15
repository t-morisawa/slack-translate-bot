# 概要
Slackで特定のチャンネルで呟くと英訳して返事をしてくれるbot

# 使用技術
* Cloud Functions
* Cloud Translation API
* Slack (outgoing-webhooks)
* Python (Flask)

# デプロイ方法

* デプロイコードは未実装です。
* SlackとGCPのWebコンソールを手動で触ってもらう形です。

## 初回デプロイ
 * GCPおよびSlackに登録する。
 * [Cloud Translation API](https://console.cloud.google.com/apis/api/translate.googleapis.com/)を有効にする。
 * [Cloud Functions](https://console.cloud.google.com/functions)を新規登録する。
 * `main.py` `requirements.txt` をCloud Functionsのwebコンソールのフォームに貼り付ける。
 * トリガーURLをメモしておく。
 * Slackの[Outgoing Webhooks](https://slack.com/apps/A0F7VRG6Q)を新規登録する。
 * Outgoing WebhooksのURL(s)にCloud FunctionsのトリガーURLを貼り付ける。それ以外のチャンネルやキーワードの設定はご自由に。

## ソース更新
 * `main.py` `requirements.txt` をCloud Functionsのwebコンソールのフォームに貼り付けて更新。
