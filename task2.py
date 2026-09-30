requests=["ПК-1", "ПК-2", "ПК-3"]
requests.append("ПК-4")
requests.insert(0,"Срочно")
pk2=requests.index("ПК-2")
requests[pk2]="ПК-2 исправлен"
requests.remove("ПК-3")
print("Извлечённое значение:",requests.pop())
print(requests)