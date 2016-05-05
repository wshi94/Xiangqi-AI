import requests

count = 0

for gameI in range(1, 600):
    for i in range(1, 100):
        req = 'http://wxf.ca/xq/xqdb/jgamelist_gen.php?id=' + str(gameI) + '&lan=c&mode=e&step=&order=&page=' + str(i) + '&pack=1&bid=&nolink=&rid='
        response = requests.get(req).text

        game = response.split('<PRE>')
        game = game[1]
        #print(len(game))
        if len(game) == 1:
	        break

        fname = 'tournament-' + str(count) + '.txt'
        count += 1
        f = open(fname, 'w')
        f.write(game)
        f.close
        