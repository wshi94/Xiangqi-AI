import requests

for i in range(1, 10):
    req = 'http://wxf.ca/xq/xqdb/jgamelist_gen.php?id=13&lan=c&mode=e&step=&order=&page=' + str(i) + '&pack=1&bid=&nolink=&rid='
    response = requests.get(req).text

    game = response.split('<PRE>')
    game = game[1]

    fname = 'asian-xiangqi-championship-' + str(i) + '.txt'

    f = open(fname, 'w')
    f.write(game)
    f.close