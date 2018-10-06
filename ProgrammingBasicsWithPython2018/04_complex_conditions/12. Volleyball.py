leap = input().lower()
holidays = int(input())
bPWeekends = int(input())
playing_weekends = 3*(48-bPWeekends)/4 +bPWeekends
total_games = playing_weekends + holidays*2/3
if leap == "leap":
    total_games = total_games*1.15
print(int(total_games))