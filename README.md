# Дипломный проект по тестированию API [reqres.in](https://reqres.in/)
<p align="left">
  <img width="50%" src="images/logo/reqres.png"/>
</p>


## Реализованные проверки по тест-кейсам  
✓ Запрос списка источников(ресурсов)  
✓ Авторизация пользователя с валидными данными 
✓ Получаение пользователя по переданному id  
✓ Обновление данных пользователя по его id 
✓ Удаление пользователя  
✓ Ошибка авторизации с пустым обязательным полем password
✓ Регистрация пользователя с валидными данными

## Используемый стек
<p align="center">
<code><img width="6%" title="Python" src="images/logo/python.png"></code>
<code><img width="6%" title="PyCharm" src="images/logo/pycharm.png"></code>
<code><img width="6%" title="PyTest" src="images/logo/pytest.png"></code>
<code><img width="6%" title="Requests" src="images/logo/requests.png"></code>
<code><img width="6%" title="Swagger" src="images/logo/swagger.png"></code>
<code><img width="6%" title="GitHub" src="images/logo/github.png"></code>
<code><img width="6%" title="Jenkins" src="images/logo/jenkins.png"></code>
<code><img width="6%" title="Allure" src="images/logo/allure_report.png"></code>
<code><img width="6%" title="Allure" src="images/logo/allure_testops.png"></code>
<code><img width="6%" title="Allure" src="images/logo/jira.png"></code>

</p>

## <img width="3%" title="Jenkins" src="images/logo/jenkins.png">Сборка в Jenkins
[JOB](https://jenkins.autotests.cloud/job/AleksandrN_reqres_api/)
<p align="left">
  <img width="90%" src="images/screenshots/jenkins_project_api.jpg"/>
</p>

## <img width="3%" title="Allure report" src="images/logo/allure_report.png">Allure report
[Ссылка на отчет](https://jenkins.autotests.cloud/job/Students/job/Requests_API/allure/)
##### После прохождения тестов, результаты можно посмотреть в Allure отчете, где так же содержится ссылка на Jenkins.
<p align="left">
  <img width="90%" src="images/screenshots/allure_report_suites_api.jpg"/>
</p>

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.

<p align="left">
  <img width="90%" src="images/screenshots/allure_report_api_graph.jpg"/>
</p>

<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="images/logo/allure_testops.png"> Интеграция с Allure TestOps
### [Dashboard](https://allure.autotests.cloud/project/3599/dashboards)
##### Так же вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики.
![This is an image](images/screenshots/allure_testops_api_graph.jpg)

#### Во вкладке со сьютами, мы можем:
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграцию с Jira
- Добавлять ручные тесты и т.д

![This is an image](images/screenshots/allure_testops_api_results.jpg)

<!-- Jira -->

### <img width="5%" title="Jira" src="images/logo/jira.png"> Интеграция с Jira
##### Настроив через Allure TestOps интеграцию с Jira, в тикет можно передать результат прохождение тестов и список тест-кейсов из Allure

![This is an image](images/screenshots/Jira_integrationns_api.jpg)