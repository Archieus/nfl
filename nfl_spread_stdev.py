import statistics
box = open("boxscores.csv")

#Skip Headers
next(box, None)

teamdict = {'BUF':'Buffalo Bills','MIA':'Miami Dolphins', 'NYJ':'New York Jets','NWE':'New England Patriots','CLE':'Cleveland Browns',
'BAL':'Baltimore Ravens','CIN':'Cincinnati Bengals','PIT':'Pittsburgh Steelers','TEN':'Tennessee Titans','IND':'Indianapolis Colts',
'HOU':'Houston Texans','JAX':'Jacksonville Jaguars','LAC':'Los Angeles Chargers','DEN':'Denver Broncos','LVR':'Las Vegas Raiders',
'KAN':'Kansas City Chiefs','DAL':'Dallas Cowboys','WAS':'Washington Football Team','PHI':'Philadelphia Eagles','NYG':'New York Giants',
'GNB':'Green Bay Packers','CHI':'Chicago Bears','MIN':'Minnesota Vikings','DET':'Detroit Lions','TAM':'Tampa Bay Buccaneers',
'CAR':'Carolina Panthers','NOR':'New Orleans Saints','ATL':'Atlanta Falcons','ARI':'Arizona Cardinals','LAR': 'Los Angeles Rams',
'SFO':'San Francisco 49ers','SEA':'Seattle Seahawks'}


winspread = []
losespread= []
allspread = []
winteam = []
loseteam = []

with open('spread.csv', 'w') as f:
    for line in box:
        boxscore = line.split(',')
        for teamkey, tmvalue in teamdict.items():
            if tmvalue == boxscore[4]:
                winspread = int(boxscore[8])-int(boxscore[9])
                winteam = boxscore[0] + "," + teamkey + ',' + str(winspread) + "," + "W"
                f.write(winteam)
                f.write('\n')
            elif tmvalue == boxscore[6]:
                losespread = int(boxscore[8]) - int(boxscore[9])
                loseteam = boxscore[0] + "," + teamkey + ',' + str(losespread) + "," + "L"
                f.write(loseteam)
                f.write('\n')
