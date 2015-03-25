from mechanics import effectiveness

def battletext (game,packet):
    battlestr = ''
    if packet[2] == 'FF':
        if packet[1] == 0:
            battlestr += 'You have fled!'
        elif packet[1] == 1:
            battlestr += str(game.p2name) + ' has fled!'
    elif packet[2] == 'Swap':
        if packet[1] == 0:
            battlestr += 'You swapped in ' + packet[3] + '!'
        elif packet[1] == 1:
            battlestr += str(game.p2name) + ' swapped in ' + packet[3] + '!'
    elif packet[2] == 'Move':
        if packet[1] == 0:
            battlestr += game.pokemans[game.activePoke].name + ' used '
        elif packet[1] == 1:
            battlestr += game.oppPoke.name + ' used '
        battlestr += packet[3].moveName
        if packet[3].buff == True:
            if packet[3].buffstat == 0:
                battlestr += ', atk has risen!'
            elif packet[3].buffstat == 1:
                battlestr += ', def has risen!'
            elif packet[3].buffstat == 2:
                battlestr += ', satk has risen!'
            elif packet[3].buffstat == 3:
                battlestr += ', sdef has risen!'
            elif packet[3].buffstat == 4:
                battlestr += ', spd has risen!'
            elif packet[3].buffstat == 5:
                battlestr += ', he healed!'
        else:
            if packet[1] == 0:
                if effectiveness(packet[3],game.oppPoke) == 0.5:
                    battlestr += ', it was not very effective...'
                elif effectiveness(packet[3],game.oppPoke) == 2:
                    battlestr += ', it was super effective!'
                else:
                    battlestr += '!'
            if packet[1] == 1:
                if effectiveness(packet[3],game.pokemans[game.activePoke]) == 0.5:
                    battlestr += ', it was not very effective...'
                elif effectiveness(packet[3],game.pokemans[game.activePoke]) == 2:
                    battlestr += ', it was super effective!'
                else:
                    battlestr += '!'
    else:
        raise TypeError('???')
    return battlestr.upper()