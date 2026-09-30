# Задание 4
def read_scores(count):
    scores=[]
    while len(scores)<count:
        try:
            user_input=input(f"Введите оценку-{len(scores)+1} из {count}:")
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