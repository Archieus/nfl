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

## Create a function to see if user wants to use team analysis
def analyze_choice():
    # The original choice value can be anthing that isn't Y or N
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input("Would you like to Analyze Another Game? Y or N: ").upper()

        if choice not in ['Y','N']:

            print("Sorry, I didn't understand.  Please input Y or N: ").upper()

    if choice == "Y":
        #Continue to analyze
        return True
    else:
        #End analysis
        return False

## DEFINE VARIABLES
pointsforWA = []
pointsaggWA = []
pointsforLA = []
pointsaggLA = []

pointsforWB = []
pointsaggWB = []
pointsforLB = []
pointsaggLB = []

pointsforAllA = []
pointsaggAllA = []

pointsforAllB = []
pointsaggAllB = []

teamA = []
teamnameA = []

teamB = []
teamnameB = []

##CREATE POWER RANK FUNCTION
def analyze_teams():
    print('\n', teamdict, '\n')

    teamA = input('Enter Team A Initials: ').upper()
    teamB = input('Enter Team B Initials: ').upper()

    print('\n')

## Assigns the values defined globally to this function since it doesn't iterate over them on additional analysis.
    global pointsforAllA; global pointsforAllB; global pointsaggAllA; global pointsaggAllB

    for teamkey, tmvalue in teamdict.items():
        if teamA == teamkey:
            teamnameA = tmvalue

        if teamB == teamkey:
            teamnameB = tmvalue

    for line in box:
        boxscore = line.split(',')
        if teamnameA == boxscore[4]:
            windateA = boxscore[2]
            winteamA = boxscore[4]
            wwkscoreA = boxscore[8]
            woppscoreA = boxscore[9]
            pointsforWA.append(int(boxscore[8]))
            pointsaggWA.append(int(boxscore[9]))
            print(windateA, winteamA, wwkscoreA, woppscoreA, "W")

        elif teamnameA == boxscore[6]:
            losedateA = boxscore[2]
            loseteamA = boxscore[6]
            lwkscoreA = boxscore[9]
            loppscoreA = boxscore[8]
            pointsforLA.append(int(boxscore[9]))
            pointsaggLA.append(int(boxscore[8]))

            print(losedateA, loseteamA, lwkscoreA, loppscoreA, "L")

        if teamnameB == boxscore[4]:
            windateB = boxscore[2]
            winteamB = boxscore[4]
            wwkscoreB = boxscore[8]
            woppscoreB = boxscore[9]
            pointsforWB.append(int(boxscore[8]))
            pointsaggWB.append(int(boxscore[9]))
            print( windateB, winteamB, wwkscoreB, woppscoreB, "W")

        elif teamnameB == boxscore[6]:
            losedateB = boxscore[2]
            loseteamB = boxscore[6]
            lwkscoreB = boxscore[9]
            loppscoreB = boxscore[8]
            pointsforLB.append(int(boxscore[9]))
            pointsaggLB.append(int(boxscore[8]))
            print(losedateB, loseteamB, lwkscoreB, loppscoreB, "L")

        pointsforAllA = pointsforWA + pointsforLA
        pointsaggAllA = pointsaggWA + pointsaggLA
        pointsforAllB = pointsforWB + pointsforLB
        pointsaggAllB = pointsaggWB + pointsaggLB

    print('\n')
    print(teamnameA, "Weekly Points For:", pointsforAllA)
    print(teamnameA, "Weekly Points Against:", pointsaggAllA,'\n')

    print(teamnameA,"Median Points For (Off. Rating): ", statistics.median(pointsforAllA))
    print(teamnameA,"Median Points Against (Def. Rating): ", statistics.median(pointsaggAllA))
    print(teamnameA, "Power_Rank: ", ((statistics.median(pointsforAllA) + statistics.median(pointsaggAllB))-20))
    print('\n')
    print(teamnameB, "Weekly Points For:", pointsforAllB)
    print(teamnameB, "Weekly Points Against:", pointsaggAllB,'\n')

    print(teamnameB,"Median Points For (Off. Rating): ", statistics.median(pointsforAllB))
    print(teamnameB,"Median Points Against (Def. Rating): ", statistics.median(pointsaggAllB))
    print(teamnameB, "Power_Rank: ", ((statistics.median(pointsforAllB) + statistics.median(pointsaggAllA))-20), '\n')

team_analysis = True

## RUN THE SCRIPT FROM FUNCTIONS
while team_analysis: #Same as while team_analysis is True:
    analyze_teams()
    team_analysis = analyze_choice()
