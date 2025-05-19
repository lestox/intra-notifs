# Install Docker on Linux

## 1. Use Docker's convenience script

```bash
curl -fsSL https://get.docker.com | sh
```

## 2. Add your user to the docker group

```bash
sudo usermod -aG docker $USER
```

## 3. Reboot your session

```bash
sudo reboot
```

After reboot, verify:

```bash
docker run hello-world
```
