# Install Docker on Windows

## 1. Install Docker Desktop

- Download from [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)
- Requires WSL2 backend (install WSL and a Linux distribution)

## 2. Enable WSL2 integration in Docker settings

## 3. Verify installation

```powershell
docker --version
docker run hello-world
```

## 4. Add user permissions (optional)

If needed, open PowerShell as admin:

```powershell
wsl --set-default-version 2
```
