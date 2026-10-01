# Задание 4
def read_scores(count):
    scores=[]
    while len(scores)<count:
        try:
            user_input=input(f"Введите оценку {len(scores)+1} из {count}:")
            score=int(user_input)
            if 0<=score<=100:
                scores.append(score)
            else:
                print("Оценка должна быть от 0 до 100")
        except ValueError:
            print("Оценка должна быть целым числом")
    return scores
print("Полученный список:",read_scores(5))

# Задание 5
def show_statistics(scores):
    if not scores:
        print("Нет результатов")
        return
    count=len(scores)
    total_sum=sum(scores)
    average=round(total_sum/count,2)
    minimum=min(scores)
    maximum=max(scores)
    passed=0
    failed=0
    for score in scores:
        if score>=70:
            passed+=1
        else:
            failed+=1
        print(f"Среднее: {average}; минимум: {minimum}; максимум: {maximum}; прошли/не прошли: {passed}/{failed}")
show_statistics([80,65,90,45,70])
show_statistics([69,70,71,0,100])
show_statistics([0,0,0,0,0])
show_statistics([])

# Задание 6
def retest_scores(scores):
    retest=[]
    for score in scores:
        if score<70:
            retest.append(score)
    retest.sort()
    return retest
print(retest_scores([80,40,70,55,40]))
print(retest_scores([70,100]))

# Задание 7
def replace_score(scores,number,value):
    if number<1 or number>len(scores):
        return False
    if value<0 or value>100:
        return False
    scores[number-1]=value
    return True
scores_list=read_scores(5)
if scores_list:
    try:
        num=int(input("Введите номер оценки для исправления:"))
        val=int(input("Введите новую оценку"))
        if replace_score(scores_list,num,val):
            print("Оценка исправлена")
        else:
            print("Ошибка неверный ввод")
    except ValueError:
        print("Ошибка введите целые числа")
    show_statistics(scores_list)
    print("Список на повторную проверку:",retest_scores(scores_list))