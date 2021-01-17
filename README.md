# component-recipes

Microservices build to contain food recipes

**Project**

- GitHub - profil: https://github.com/parisnakitakejser
- GitHub - Source code: https://github.com/parisnakitakejser/component-recipes
- Docker Hub: https://hub.docker.com/r/parisnk/component-recipes

**🌟 Community 🌟**

- Subscribe my channel: https://www.youtube.com/c/ParisNakitaKejser?sub_confirmation=1
- Private website: https://www.pnk.sh
- Discord: https://discord.gg/6tcWjxV
- Donate: https://www.patreon.com/parisnakitakejser

**System environments to set**

| Environment vars  | Fallback          |
| ----------------- | ----------------- |
| MONGO_DATABASE    | component-recipes |
| MONGO_HOST        | None              |
| MONGO_PORT        | None              |
| MONGO_USERNAME    | None              |
| MONGO_PASSWORD    | None              |
| MONGO_AUTH_SOURCE | None              |
| MONGO_MECHANISM   | None              |

**Build new images**

If you found eny bugs and want to build your own images, you can do it very quickly by using this command

    docker build -t component-recipes:{version} . --no-cache -f .docker/Dockerfile

**Run unittest local in container**

If you want to run test after you have change code or just want to check all tests out, its can be done by build a unittest images and run the unittest images after in a single docker container.

    docker build -t unittest . -f .docker/Unittest/Dockerfile
    docker run --rm unittest

**docker-compose.yaml sample**

    version: "3.7"

    services:
        component-recipes:
            image: parisnk/component-recipes
            ports:
                - "5000:5000"

            environment:
                - MONGO_DATABASE=component-authentication
                - MONGO_HOST={hostname}
                - MONGO_PORT={port}
                - MONGO_USERNAME={username}
                - MONGO_PASSWORD={password}
                - MONGO_AUTH_SOURCE=admin
                - MONGO_MECHANISM=SCRAM-SHA-1
