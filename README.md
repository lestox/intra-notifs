# intra-notifs

Automated notifications from the ETNA Intranet system, delivered via Google Chat.

---

## 🛠 Requirements

- `git`
- `docker` (with daemon running)

---

## Installation

### 1. Clone the repository

```sh
git clone https://github.com/lestox/intra-notifs
cd intra-notifs
```

### 2. Configure environment variables

Create a `.env` file in the project root with the following content:

```env
LOGIN=your_etna_login
PASSWORD=your_etna_password

GOOGLE_CHAT_WEBHOOK_INFORMATIONS=...
GOOGLE_CHAT_WEBHOOK_CONVERSATIONS=...
GOOGLE_CHAT_WEBHOOK_UNREAD_CONVERSATIONS=...
GOOGLE_CHAT_WEBHOOK_NEW_RELEASE=...
```

---

## Run the container

Use the provided scripts from the `scripts/` directory:

### Install and start

```sh
sh scripts/install
```

### Update and restart

```sh
sh scripts/update
```

### Stop the container

```sh
sh scripts/stop
```

### Restart the container

```sh
sh scripts/restart
```

### Uninstall completely

```sh
sh scripts/uninstall
```

### View logs

```sh
sh scripts/logs
```

### Check container status

```sh
sh scripts/status
```

---

## Manual run (optional)

If needed, you can manually rebuild and run:

```sh
docker build -t intra-notifs:python .
docker run --restart=always -d --name intra-notifs intra-notifs:python
```

---

## Related repository

You can also check the main branch of this related project:  
👉 https://github.com/lestox/intra-notifs
