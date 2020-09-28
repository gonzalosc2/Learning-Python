# author: Gonzalo Salazar
# assigment: Homework #1
# description: Checks the songs on the hist list in a specific week

def hitlist(DAY, MONTH, YEAR):
    if len(str(DAY)) < 2:
        DAY = '0' + str(DAY)

    if len(str(MONTH)) < 2:
        MONTH = '0' + str(MONTH)

    the_date = '{y}-{m}-{d}'.format(m=MONTH, d=DAY, y=YEAR)

    from webbrowser import open
    return open(url='https://www.billboard.com/charts/hot-100/' + the_date)
