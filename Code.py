CODE:
runs_scored=int(input("Enter the runs scored:"))
balls_faced=int(input("Enter the balls faced"))
fours=int(input("Enter the fours:"))
sixes=int(input("Enter the sixes:"))
wickets_taken=int(input("Enter the wickets taken:"))
runs_conceded=int(input("Enter the runs conceded:"))
overs_bowled=int(input("Enter the overs bowled:"))
catches_taken=int(input("Enter the catches taken:"))
batting_strike_rate=runs_scored/balls_faced
bowling_economy_rate=runs_conceded/overs_bowled
if runs_scored >=50 and batting_strike_rate>=120:
    batter="Excellent"
    print("Excellent batter")
elif runs_scored>=30 and batting_strike_rate>=100:
    batter="Good"
    print("Good batter")
elif runs_scored>=20:
    batter="Average"
    print("Average batter")
else:
    batter="Poor"
    print("Poor batter")
if wickets_taken>=3 and bowling_economy_rate<=6:
    bowler="Excellent"
    print("Excellent bowler")
elif wickets_taken>=2and bowling_economy_rate<=8:
    bowler="Good"
    print("Good bowler")
elif wickets_taken>=1:
    bowler="Average"
    print("Average bowler")
else:
    bowler="Poor"
    print("Poor bowler")
if catches_taken>=2:
    print("Outstanding fielder")
elif catches_taken==1:
    print("Active fielder")
else:
    print("Needs improvement")
if batter=="Excellent" and bowler=="Excellent":
    print("Star all rounder")
elif batter=="Good" and bowler=="Good":
    print("Strong all rounder")
elif batter=="Good" or bowler=="Good":
    print("supporting all rounder")
else:
    print("Needs improvement")
Needs improvement
