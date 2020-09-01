def findMonth(choice):
    properties = {} 
    month = choice['month']
    source = '/static/img/'
    if (month == 'jan'): 
        source += 'jan-garnet.jpg'
        bstone = "Garnet"
        mon = "January"
    elif (month == 'feb'):
        source += 'feb-amethyst.jpg'
        bstone = "Amethyst"
        mon = "February"
    elif (month == 'mar'):
        source += 'mar-aquamarine.jpg'
        bstone = "Aquamarine"
        mon = "March"
    elif (month == 'apr'):
        source += 'gem.png'
        bstone = "Diamond"
        mon = "April"
    elif  (month == 'may'):
        source += 'gem.png'
        bstone = "Emerald"
        mon = "May"
    elif (month == 'aug'):
        source += 'aug-peridote.jpg'
        bstone = "Peridote"
        mon = "August"
    else:
        source += 'gem.png'
    properties['month']=mon
    properties['source'] = source
    properties['birthstone']=bstone
    return properties