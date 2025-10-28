def sweeper(hiding, full, col, row):
    hiding[col][row],full[col][row]=full[col][row],hiding[col][row]
    return hiding,full

