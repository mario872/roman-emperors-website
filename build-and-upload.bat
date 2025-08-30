docker compose up --build
docker tag roman-emperors-project-web:latest solderingiron86/roman-emperors-project:latest
docker tag roman-emperors-project-web:latest solderingiron86/roman-emperors-project:0.2
docker push solderingiron86/roman-emperors-project:latest
docker push solderingiron86/roman-emperors-project:0.2
REM Remember to change the version tags! HERE and Dockerfile