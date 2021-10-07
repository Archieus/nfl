import statistics
box = open("boxscores.csv")
nfc = open("nfc.csv")
afc = open("afc.csv")

## Skip Headers in csv
next(afc, None)
next(nfc, None)
next(box, None)

# CREATE DICTIONARY FOR TEAM ABBREVIATIONS
teamdict = {'BUF':'Buffalo Bills','MIA':'Miami Dolphins', 'NYJ':'New York Jets','NWE':'New England Patriots','CLE':'Cleveland Browns',
'BAL':'Baltimore Ravens','CIN':'Cincinnati Bengals','PIT':'Pittsburgh Steelers','TEN':'Tennessee Titans','IND':'Indianapolis Colts',
'HOU':'Houston Texans','JAX':'Jacksonville Jaguars','LAC':'Los Angeles Chargers','DEN':'Denver Broncos','LVR':'Las Vegas Raiders',
'KAN':'Kansas City Chiefs','DAL':'Dallas Cowboys','WAS':'Washington Football Team','PHI':'Philadelphia Eagles','NYG':'New York Giants',
'GNB':'Green Bay Packers','CHI':'Chicago Bears','MIN':'Minnesota Vikings','DET':'Detroit Lions','TAM':'Tampa Bay Buccaneers',
'CAR':'Carolina Panthers','NOR':'New Orleans Saints','ATL':'Atlanta Falcons','ARI':'Arizona Cardinals','LAR': 'Los Angeles Rams',
'SFO':'San Francisco 49ers','SEA':'Seattle Seahawks'}


## Mike Lee's Power Ranking
for line in nfc:
    nfclist = line.split(',')
    nfcteam = nfclist[0]

    nfc_rank = round(100-((int(nfclist[5])*10)/int(nfclist[4])),2)
    print(nfcteam," ",nfc_rank)

for line in afc:
    afclist = line.split(',')
    afcteam = afclist[0]
    afc_rank = round(100-((int(afclist[5])*10)/int(afclist[4])),2)

    print(afcteam, " ", afc_rank)

### J R Miller Power Ranking

print(teamdict)
teamA = input('Enter Team A Initials: ')
teamB = input('Enter Team B Initials: ')

print('\n')

pointsforWA = []
pointsaggWA = []
pointsforLA = []
pointsaggLA = []

pointsforAllA = []
pointsaggAllA = []

for teamkey, tmvalue in teamdict.items():
    if teamA == teamkey:
        teamname = tmvalue
        for line in box:
            boxscore = line.split(',')
            if teamname == boxscore[4]:
                windateA = boxscore[2]
                winteamA = boxscore[4]
                wwkscoreA = boxscore[8]
                woppscoreA = boxscore[9]
                pointsforWA.append(int(boxscore[8]))
                pointsaggWA.append(int(boxscore[9]))
                print(windateA, winteamA, wwkscoreA, woppscoreA, "W")

            elif teamname == boxscore[6]:
                losedateA = boxscore[2]
                loseteamA = boxscore[6]
                lwkscoreA = boxscore[9]
                loppscoreA = boxscore[8]
                pointsforLA.append(int(boxscore[9]))
                pointsaggLA.append(int(boxscore[8]))
                print(losedateA, loseteamA, lwkscoreA, loppscoreA, "L")

            pointsforAllA = pointsforWA + pointsforLA
            pointsaggAllA = pointsaggWA + pointsaggLA

print('\n')
print(teamname, "Weekly Points For:", pointsforAllA,'\n')
print(teamname, "Weekly Points Against:", pointsaggAllA,'\n')

print("Median Points For (Off. Rating): ", statistics.median(pointsforAllA))
print("Median Points Against (Def. Rating): ", statistics.median(pointsaggAllA))
