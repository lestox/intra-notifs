# intra-notifs – Developer Guide

This document provides setup and contribution instructions for developers working on `intra-notifs`.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/lestox/intra-notifs
cd intra-notifs
```

---

### 2. Create your environment

It is recommended to use a virtualenv:

```bash
python -m venv venv
source venv/bin/activate
```

Install required dependencies:

```bash
pip install -r requirements-dev.txt
```

---

### 3. Configure environment

Create a `.env` file from the provided template:

```bash
cp .env.example .env
```

Fill in the values for:
- `LOGIN`
- `PASSWORD`
- `GOOGLE_CHAT_WEBHOOK_INFORMATIONS`

---

### 4. Run locally

```bash
make run
```

---

## 🧪 Running tests & checks

Run all tests:

```bash
make test
```

Check code style:

```bash
make lint
```

Auto-fix lint issues:

```bash
make fix
```

Format the code:

```bash
make format
```

---

## 🐳 Using Docker (dev)

Build the image:

```bash
docker build -t intra-notifs:dev .
```

Run it:

```bash
docker run --rm -it --env-file .env intra-notifs:dev
```

---

## 🗂 Project Structure

```
.
├── app/                  # Main source code
│   ├── config/           # Logging and env loading
│   ├── constants/        # URLs and secrets
│   ├── services/         # Core logic (auth, data, chat)
├── tests/                # Unit tests
├── scripts/              # Docker and helper scripts
├── run.py                # Entry point for local execution
├── refresh_cookie.py     # Cookie renewal logic
├── requirements.txt
├── requirements-dev.txt
└── .env.example
```

---

## 🛠 Tooling

- Python 3.11+
- `black` for formatting
- `ruff` for linting and auto-fixes
- `pytest` for testing
- `Docker` for packaging
- `Makefile` for automation

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feat/feature-name`)
3. Commit your changes (`git commit -m 'feat: add something'`)
4. Push to the branch (`git push origin feat/feature-name`)
5. Open a pull request

---

## 📬 Contact

For issues, open a GitHub ticket or contact the maintainer directly.
