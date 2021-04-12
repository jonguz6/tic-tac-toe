def create_board():
    board = {
        'tL': ' ', 'tM': ' ', 'tR': ' ',
        'mL': ' ', 'mM': ' ', 'mR': ' ',
        'bL': ' ', 'bM': ' ', 'bR': ' ',
    }
    return [
        f"{board['tL']}|{board['tM']}|{board['tR']}",
        '-+-+-',
        f"{board['mL']}|{board['mM']}|{board['mR']}",
        '-+-+-',
        f"{board['bL']}|{board['bM']}|{board['bR']}"
    ]


if __name__ == '__main__':
    pass
