# ECS

### sample project git clone
```
git clone https://github.com/go4real/Django-Poll-App.git
cd Django-Poll-App
git switch ecs-base
```

### ECS app init
```
copilot init
```
### dev3 env deploy
```
copilot env init
copilot env deploy --name dev3
```
### poll-db3 deploy
```
copilot deploy
```
### poll-backend3 deploy
```
copilot init
copilot deploy
```
### poll-frontend3 deploy
```
copilot init
copilot deploy
```

### prod3 env deploy
```
copilot env init --name prod3 --profile default --container-insights
copilot env deploy --name prod3
copilot svc deploy --app poll-app3 --env prod3 --name poll-db3
copilot svc deploy --app poll-app3 --env prod3 --name poll-backend3
copilot svc deploy --app poll-app3 --env prod3 --name poll-frontend3
```
### ab test
```
sudo apt install apache2-utils
ab -n 3000 -c 10 http://poll-publi-1r25anylgs1ty-1602012990.ap-northeast-2.elb.amazonaws.com/polls/list/ 
```