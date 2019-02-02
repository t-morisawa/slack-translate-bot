# 概要
Slackで特定のチャンネルで呟くと英訳して返事をしてくれるbot

# 使用技術
* Cloud Functions
* Cloud Translation API
* Slack (outgoing-webhooks)
* Python (Flask)

# デプロイ方法
* SlackとGCPのコンソールをぽちぽちする
* IaC的なデプロイはtodo

## ソース更新
* `main.py` `requirements.txt` をCloud Functionsのwebコンソールのフォームに貼り付けて更新。
