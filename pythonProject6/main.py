turns1 = 0
turns2 = 0
fatigue_passed1 = 50
remaining_life1 = 20000
constant_damage1 = 20
regenerate_health1 = 0
k1 = fatigue_passed1
u1 = remaining_life1
c1 = constant_damage1
fatigue_passed2 = 0
remaining_life2 = 11900
constant_damage2 = 0
regenerate_health2 = 0
k2 = fatigue_passed2
u2 = remaining_life2
c2 = constant_damage2
turns_order = 0
dannipl = 0
danniopp = 0
total_turns = 0
current_turn = 0
my_turns = 0
opponent_turns = 0
first_opponent = True
opponent_loses = False
me_loses = False

'''def turni1():
    turns1 = ((-(2*c1 + 1)) + ((2*c1+1)**2 + 4*(k1**2 + k1 + 2*u1 + 2*c1*k1))**0.5)/2 - k1
    print(turns1)
    if int(turns1) < turns1:
        return int(turns1) + 1
    return int(turns1)

def turni2():
    turns2 = ((-(2*c2 + 1)) + ((2*c2+1)**2 + 4*(k2**2 + k2 + 2*u2 + 2*c2*k2))**0.5)/2 - k2
    if int(turns2) < turns2:
        return int(turns2) + 1
    return int(turns2)

print(turni1())
print(turni2())
print(turni1() - turni2())'''

if first_opponent:
    current_turn = 0
else:
    current_turn = 1


def switching_turn():
    global current_turn
    if current_turn == 0:
        current_turn = 1
    else:
        current_turn = 0

def definisci_turno1():
    global remaining_life1
    global total_turns
    global my_turns
    global current_turn
    global regenerate_health1
    global opponent_turns
    global remaining_life2
    global opponent_loses
    global me_loses
    while True:
        if current_turn == 0:
            total_turns += 1
            opponent_turns += 1
            danniopp = fatigue_passed2 + opponent_turns
            remaining_life2 -= danniopp
            if not remaining_life2 > 0:
                opponent_loses = True
                print("Ho vinto io, per via di fatigue damage subiti dall'avversario, nel turno numero: " + str(total_turns) + ", lui aveva " + str(remaining_life2 + danniopp) + " punti vita prima che perdesse " + str(danniopp) + ", io avevo " + str(remaining_life1) + " punti vita")
                break
            danniopp = -regenerate_health2
            remaining_life2 -= danniopp
            dannipl = constant_damage1
            remaining_life1 -= dannipl
            print(remaining_life1, remaining_life2, total_turns)
            if remaining_life1 > 0:
                switching_turn()
            else:
                me_loses = True
                print("Ho perso io, per via di attacco da parte dell'avversario, nel turno numero: " + str(total_turns) + ", avevo " + str(remaining_life1 + dannipl) + " punti vita prima che mi attaccasse con " + str(constant_damage1) + ", il mio avversario aveva " + str(remaining_life2) + " punti vita")
                break
        else:
            total_turns += 1
            my_turns += 1
            dannipl = fatigue_passed1 + my_turns
            remaining_life1 -= dannipl
            print(remaining_life1, remaining_life2, total_turns)
            if not remaining_life1 > 0:
                me_loses = True
                print("Ho perso io, per via di fatigue damage, nel turno numero: " + str(total_turns) + ", avevo " + str(remaining_life1 + dannipl) + " punti vita prima che subissi " + str(dannipl) + ", il mio avversario aveva " + str(remaining_life2) + " punti vita")
                break
            dannipl = -regenerate_health1
            remaining_life1 -= dannipl
            danniopp = constant_damage2
            remaining_life2 -= danniopp
            print(remaining_life1, remaining_life2, total_turns)
            if remaining_life2 > 0:
                switching_turn()
            else:
                opponent_loses = True
                print("Ho vinto io, per via di attacco da parte mia, nel turno numero: " + str(total_turns) + ", lui aveva " + str(remaining_life2 + danniopp) + " punti vita prima che lo attaccassi con " + str(constant_damage2) + ", io avevo " + str(remaining_life1) + " punti vita")
                break



definisci_turno1()
if opponent_loses:
    print("The opponent lost")
else:
    print("I lost")
print(total_turns)
print(my_turns)
print(current_turn)