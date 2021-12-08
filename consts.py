
URL = "http://support-sp.apple.com/sp/index?page=cpuspec&cc="

YEARS = {
    '3': (2003, False), '4': (2004, False), '5': (2005, False), '6': (2006, False), '7': (2007, False),
    '8': (2008, False), '9': (2009, False), '0': (2010, False), '1': (2011, False), '2': (2013, False),

    'C': (2010, False), 'D': (2010, True), 'F': (2011, False), 'G': (2011, True),
    'H': (2012, False), 'J': (2012, True), 'K': (2013, False), 'L': (2013, True),
    'M': (2014, False), 'N': (2014, True), 'P': (2015, False), 'Q': (2015, True),
    'R': (2016, False), 'S': (2016, True), 'T': (2017, False), 'V': (2017, True),
    'W': (2018, False), 'X': (2018, True), 'Y': (2019, False), 'Z': (2019, True)
}

WEEKS = {
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'C': 10, "D": 11, "F": 12, "G": 13, "H": 14,
    "J": 15, "K": 16, "L": 17, "M": 18, "N": 19, "P": 20, "Q": 21, "R": 22, "T": 23, "V": 24, "W": 25, "X": 26,
    "Y": 27  # This is only for 53 week, which is rare. 27 week will be '1' on second part of year
}

LOCATIONS = {
    'RM': 'Refurbished/remanufactured',
    'FC': 'Fountain Colorado, USA',
    'XA': 'USA (Elk Grove/Sacramento, California)',
    'XB': 'USA',
    'QP': 'USA',
    'G8': 'USA',
    'RN': 'Mexico',
    'CK': 'Cork, Ireland',
    'VM': 'Foxconn, Pardubice, Czech Republic',
    'SG': 'Singapore',
    'MB': 'Malaysia',
    'PT': 'Korea',
    'CY': 'Korea',
    'EE': 'Taiwan',
    'UV': 'Taiwan',
    'QT': 'Taiwan (Quanta Computer)',
    'FK': 'Foxconn-Zhengzhou, China',
    'F1': 'Foxconn-Zhengzhou, China',
    'F2': 'Foxconn-Zhengzhou, China',
    'W8': 'Shanghai China',
    'DL': 'Foxconn, China',
    'DM': 'Foxconn, China',
    'DN': 'Foxconn, Chengdu, China',
    'YM': 'Hon Hai/Foxconn, China',
    '7J': 'Hon Hai/Foxconn, China',
    '1C': 'China',
    '4H': 'China',
    'MQ': 'China',
    'WQ': 'China',
    'F7': 'China',
    'C0': 'Tech Com-Quanta Computer Subsidiary, China',
    'C3': 'Foxconn, Shenzhen, China',
    'C7': 'Foxconn, Changhai, China',
    'F5K': 'USA (Flextronics)',
    'CK2': 'Cork, Ireland',
    'C02': 'Tech Com-Quanta Computer Subsidiary, China',
    'C07': 'Tech Com-Quanta Computer Subsidiary, China',
    'YM0': 'China (Hon Hai/Foxconn)',
    'C17': 'China',
    'C1M': 'China',
    'C2V': 'China',
    'C2Q': 'China',
}
