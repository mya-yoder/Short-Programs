def cribbage_pts(cards, cut: int, suit_match=False):
    points = 0

    #adds a points if suit of jack matches suit of cut card
    if suit_match:
        points += 1

    
    cards.append(cut)

    #checks for doubles
    for index in range(0, 5):
        for i in range(index + 1, 5):
            if cards[index] == cards[i]:
                points += 2
    
    #assings a number value to face cards
    for i in range(0, 5):
        if cards[i] == 'J':
            cards[i] = 11
        elif cards[i] == 'Q':
            cards[i] = 12
        elif cards[i] == 'K':
            cards[i] = 13
        elif cards[i] == 'A':
            cards[i]= 1
          
    #checks for runs
    for card in cards:
        multiplier = 0
        #3 card runs
        if (card+1) in cards and (card+2) in cards:
            #4 card runs
            if (card+3) in cards:
                #5 card runs
                if (card+4) in cards:
                    points += 5
                    break
                
                else:
                    if cards.count(card)> 1 or cards.count(card+1)>1 or cards.count(card+2)>1 or cards.count(card+3)>1:
                        points += 8
                    else:
                        points += 4
                    break

            else:
                if cards.count(card) > 1:
                    multiplier += cards.count(card)
                if cards.count(card+1) > 1:
                    multiplier += cards.count(card+1)
                if cards.count(card+2) > 1:
                    multiplier += cards.count(card+2)
                if multiplier == 0:
                    multiplier = 1
                points += multiplier * 3
                break
    
    #gives all face cards a value of 10
    for i in range(0, 5):
        if cards[i] > 10:
            cards[i] = 10
    
    #if pairs add to 15
    for a in range(0, 5):
        for b in range(a+1, 5):
            if cards[a] + cards[b] == 15:
                points += 2
    
    #if triples add to 15
    for a in range(0, 5):
        for b in range(a+1, 5):
            for c in range(b+1, 5):
                if cards[a] + cards[b] + cards[c] == 15:
                    points += 2
    
    #if quadruples add to 15
    for a in range(0, 5):
        for b in range(a+1, 5):
            for c in range(b+1, 5):
                for d in range(c+1, 5):
                    if cards[a] + cards[b] + cards[c] +cards[d] == 15:
                        points += 2
    
    #if all 5 add to 15
    if cards[0] + cards[1] + cards[2] + cards[3] + cards[4] == 15:
        points += 2
    
                    
    return points
            
    
