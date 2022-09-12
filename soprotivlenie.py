import random

players = ["Николай","Алексей","Михаил","Екатерина","Пётр","Степан","Митя","Влад","Женя","Артём"]

roles =[]

#узнаем сколько будет шпионов
def spy_count (gamers):
    spy_at_start = {5:2, 6:2, 7:3, 8:3, 9:3, 10:4}
    return(spy_at_start[gamers])

#узнаем сколько будет сопротивленцев
def resistance_count (gamers):
    resistance_at_start = {5:3, 6:4, 7:4, 8:5, 9:6, 10:6}
    return(resistance_at_start[gamers])

#перемешиваем роли
def role_shuffle():
    for i in range(spy_count (gamers)): roles.append('spy')
    for i in range(resistance_count (gamers)): roles.append('resistance')
    print (roles)
    random.shuffle(roles)
    print (roles)

#назначаем роли игрокам
def players_set_roles():
    for i in range(gamers):
        players[i]=[players[i],roles[i]]
        print (players[i])

gamers = input ("введите кол-во игроков (5-10): ")
if gamers.isdigit():
    gamers = int (gamers)
    if  4<gamers<11:
        print ("Сопротивление - " + str(resistance_count (gamers)))
        print ("Шпионов - " + str(spy_count (gamers)))
        role_shuffle()
        players_set_roles()
    else: print ("недопустимое кол-во игроков")
else: print ("недопустимое кол-во игроков")

#pl=["Коля","Артём"]
#print (pl[0])
#pl[0]=[pl[0],"шпион"]
#print (pl)

#pl [1]=["35"]
#print (pl[0][1])
