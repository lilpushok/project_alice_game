days = [["Ваш старинный приятель пригласил вас на охоту. Изволите принять приглашение?", ['Да', 'Нет'], [[0, 0, 0], [0, 0, 0]]]
     
     , ['У вашего сына день рождения, но у вас деловая встреча. Вы не успеите и туда и туда. Изволите отменить встречу?', ['Да', 'Нет'], [[0, -2, -10000], [0, 1, 50000]]]
     
     , ['Президент Когрании пригласил подписать вас документ, в результате которого вы обмениваетесь научными достижениями. Изволите принять приглашение?', ['Да', 'Нет'], [[0, 0, 5000], [0, -2, -20000]]] 
     
     , ['Ваш шпион узнал интересные сведения о правительстве. Изволите его выслушать?', ['Да', 'Нет'], [[2, -4, -10000], [-2, 2, 0]]]
     
     , ['Вам донесли что в городе Ропка готовится теракт. Изволите усилить патрули?', ['Да', 'Нет'], [[0, 0, -10000], [-3, -1, 0]]] # 5
     
     , ['На территории Белябинска нашли большие залежи медной руды. Изволите построить шахту?', ['Да', 'Нет'], [[-4, 1, 100000], [1, 0, 0]]]
 
     , ['Один из ученных говорит, что он создал формулу “Вечной молодости”. Изволите спонсировать его?', ['Да', 'Нет'], [[-2, 0, -30000], [0, 0, 0]]]
 
     , ['В соседней стране революция. Изволите помочь соседним властям?', ['Да', 'Нет'], [[-3, 2, -50000], [0, -2, 0]]]
 
     , ['В соседней стране революция. Изволите усилить вашу охрану?', ['Да', 'Нет'], [[-3, -1, -5000], [0, 0, 0]]] 
 
     , ['Рабочие шахты покинули ее, так она может в любой момент обвалиться. Изволите сказать шахтерам работать в обычном режиме, или усилите её?', ['Да', 'Нет'], [[-5, -1, 75000], [1, 1, -20000]]] # 10
 
     , ['Вашу семью взяли в заложников. Террористы требуют вас покинуть пост. Изволите покинуть пост президента?', ['Да', 'Нет'], [[-10000, -10000, -1000000000000], [0, 0, 0]]]
 
     , ['Вашу семью взяли в заложников. Террористы требуют выкуп и вертолет. Изволите выполнить их требование?', ['Да', 'Нет'], [[-3, -2, -200000], [-3, -2, 0]]]
 
     , ['В одном из ваших городов потоп. МЧС не справляются, выслать отряд помощи?', ['Да', 'Нет'], [[2, 1, -30000], [-3, -1, 0]]]
 
     , ['На вашу страну напали. Вашим войскам удалось отбить атаку. Перейти в контратаку?', ['Да', 'Нет'], [[2, 1, -100000], [-3, -1, 0]]]
 
     , ['Ваш сотрудник пытался вас отравить. Посадить его в тюрьму?', ['Да', 'Нет'], [[3, -4, 0], [-2, -2, 0]]] # 15
 
     , ['На территории нашей страны сгорел памятник архитектуры. Прикажите реставрировать?', ['Да', 'Нет'], [[3, -1, -40000], [-2, 0, 0]]]
 
     , ['Музей архитектуры требует востановления. Реставрировать?', ['Да', 'Нет'], [[3, 1, -50000], [-2, 0, 0]]]
 
     , ['Министерство образования хочет ввести бесплатное питание в школах. Подписать указ? ', ['Да', 'Нет'], [[3, 2, -50000], [-2, -1, 0]]]
 
     , ['Министерство образования хочет отменить систему оценивая, с сохранением ОГЭ и ЕГЭ. Подписать указ?', ['Да', 'Нет'], [[4, 2, 0], [0, -2, 0]]]
 
     , ['Министерство образования хочет ввести новый обязательный предмет "Философия". Подписать указ? ', ['Да', 'Нет'], [[-1, 2, 0], [0, -2, 0]]] # 20
 
     , ['Министерство обороны запрашивает у вас 300000 дублей на новейшую систему ракетных установовок. Заплатить им 300000 дублей', ['Да', 'Нет'], [[0, 2, -300000], [0, -4, 35000]]] 
 
     , ['А.П.Закров(посол Каброловой страны) предлагает подписать мирное соглашение. При условии военного альянса. Подписать соглашение?', ['Да', 'Нет'], [[0, -1, -30000], [-1, 0, -15000]]]
 
     , ['На нашем воздушном коридоре замечен не запланированный беспилотный истребитель. Прикажите стрелять на поражение?', ['Да', 'Нет'], [[-2, 1, 15000], [-1, -2, 0]]]
 
     , ['Фермеры нашли на своей территории древние остатки больших животных. Археологи хотеть провести раскопки. Дать разрешение на раскопки', ['Да', 'Нет'], [[-3, 1, -20000], [1, -1, 15000]]]
 
     , ['В Прогоновой стране убили нашего посла, целью которого было подписание мирного соглашения. Объявить войну или послать еще одного посла', ['Объявить войну', 'Послать посла'], [[2, 2, -50000], [1, -1, -5000]]] # 25
 
     , ['Один человек утверждает, что он доказал квадрат гипотенузы равен сумме квадратов катетов в прямоугольном треугольнике. Наградить его Нобилевской премией', ['Да', 'Нет'], [[-2, -2, -10000], [1, 1, 10000]]]
 
     , ['Ваш содрудник взял взятку, уволить его без возможности дальшей работы, вназидание другим?', ['Да', 'Нет'], [[1, -3, 40000], [-2, 1, 15000]]] 
 
     , ['Вы владеете контрольным пакетом акций одного завода на котором работает свыше 1500 людей. Бизнесмен хочет купить у вас этот пакет, чтобы построить на месте завода гипермаркет. Продать пакет акций?', ['Да', 'Нет'], [[-3, 1, 70000], [1, -2, 0]]]
 
     , ['Наши граждане жалуются на отсутствие детских площадок. Построить детские площадки?', ['Да', 'Нет'], [[3, 0, -25000], [-2, 0, 0]]]
  
     , ['Сын прокурора может сесть в тюрьму. За его освобождение вам хотят дать взятку в размере 50000 дублей. Возьмете ли вы деньги?', ['Да', 'Нет'], [[-1, 2, 50000], [1, -2, 0]]]]

print(days)
