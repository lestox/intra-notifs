# intra-alerting

git
docker

```
git clone https://github.com/etna-student/intra-alerting

cd intra-alerting
```



```
LOGIN=
PASSWORD=

GOOGLE_CHAT_WEBHOOK_INFORMATIONS=
GOOGLE_CHAT_WEBHOOK_CONVERSATIONS=
GOOGLE_CHAT_WEBHOOK_UNREAD_CONVERSATIONS=
GOOGLE_CHAT_WEBHOOK_NEW_RELEASE=
```

```
sh scripts/install
```

```
sh scripts/uninstall
```


Faire une pull de la branche main du projet suivant :
https://github.com/etna-student/intra-alerting

Faire un build du container :
docker build -t internal-alerting:python .

Lancer le container :
docker run --restart=always -d --name intra-alerting intra-alerting:python
