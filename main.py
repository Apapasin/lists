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