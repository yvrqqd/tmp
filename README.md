Реализовано 3 функции: <br> 
 <br> 
Опредление города в сообщении. <br> 
Определение города в сообщениях из файла. <br> 
Генерация поздравления по имени. <br> 
 <br> 
Использован yandex gpt <br> 
 <br> 
У сервиса есть ограничения, обход которых требует значительного усложнения программы. Ограничение заключается в количестве запросов, на которые можно получить ответ за час. Квота - 100, поэтому при тестировании следует оставить загрузку файла на конец. <br> 
 <br> 
Варианты улучшения: <br> 
	1. Использовать агентов для проверки. Это позолит избежать ответов, данных не по шаблону. В таком случае также, вероятно, можно использовать кратно более копактные модели. <br> 
	2. Создать базу сокращений и использовать RAG. <br> 
 <br> 
Пример разобранных сообщений есть в файле answers.txt (разобраны не все | из-за квоты) <br> 
 <br> 
Опробовать сервис можно по ссылке: https://2tk6fbjuxnappgdxvxd2cmh.streamlit.app/ <br> 
