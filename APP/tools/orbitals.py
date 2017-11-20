from find_a_string_in_file import Find_a_String
import sys

class Transitions(object):

    def __init__(self, excitedState, wavelength, osc_force, transitions, contrib, homo):
        try:
            self.excitedState = excitedState
            self.wavelength = float(wavelength)
            self.osc_force = float(osc_force)
            self.homo = homo
            self.transitions = []
            for transitions_raw in transitions:
                self.transitions.append([int(transitions_raw.split()[0]), int(transitions_raw.split()[1])])
            self.contrib = [float(x) for x in contrib]
            self.contrbutionPercent()
            self.translateTransition()
        except:
            print("Error in Transition(object)")
            sys.exit()

    def contrbutionPercent(self):
        self.contrib_percent = [x*x*2*100 for x in self.contrib]

    def translateTransition(self):
        self.transleted_transitions = []
        for i in range(0, len(self.transitions)):
            arrow_fletching = self.translateOrbital(self.transitions[i][0])
            arrow_head = self.translateOrbital(self.transitions[i][1])
            self.transleted_transitions.append([arrow_fletching, arrow_head])

    def translateOrbital(self, orbital):
        lumo = self.homo +1
        if orbital < self.homo:
            translatedOrbital = "HOMO"+str(orbital-self.homo)
        elif orbital > lumo:
            translatedOrbital = "LUMO+" + str(orbital - lumo)
        elif orbital == lumo:
            translatedOrbital = "LUMO"
        else:
            translatedOrbital = "HOMO"
        return translatedOrbital

    def getTransitions(self):
        return [self.excitedState, self.wavelength, self.transleted_transitions, self.contrib_percent]

class FrontierOrbitals(object):

    def __init__(self, file):
        self.file = file
        self.totalElectrons()
        self.homo = self.orb_occp_nb
        self.lumo = self.orb_occp_nb +1

    def totalElectrons(self):
        electrons_desc = Find_a_String(self.file, "alpha electrons").return_the_line()[0]
        self.number_of_electrons = int(electrons_desc.split()[0]) + int(electrons_desc.split()[3])
        self.orb_occp_nb = int(electrons_desc.split()[0])


class TransitionContribution(object):

    def __init__(self, file):
        self.file = file
        self.orbitals = FrontierOrbitals(self.file)
        self.lines_of_states = Find_a_String(self.file," Excited State  ").return_numbers_of_line()
        self.nb_of_states = len(self.lines_of_states)
        self.states = []
        self.font_orbitals = []
        self.makeTransitions()

    def makeTransitions(self):
        myFile = open(self.file, 'r').readlines()
        for state in range(0, self.nb_of_states):
            number_of_line = self.lines_of_states[state]
            y = myFile[self.lines_of_states[state]-1].split()
            line = myFile[number_of_line]
            transitions_in_file = []
            cont_transtions = []
            while ("->" in line):
                x = [x for x in line.split("->")]
                transitions_in_file.append(x[0]+x[1].split()[0])
                cont_transtions.append(x[1].split()[1])
                number_of_line+=1
                line = myFile[number_of_line]
            self.states.append(Transitions(state+1, y[6], y[8].split("=")[1], transitions_in_file, cont_transtions, self.orbitals.homo))

    def getTransitions(self):
        x = []
        for state in self.states:
            x.append(state.getTransitions())

if __name__ == "__main__":
    #file_ = "/Users/thiagolopes/Downloads/TD_Epinefrina_Tuned_LC-wPBE_49000.log"
    #x = TransitionContribution(file_)
    #w = FrontierOrbitals(file_)

    file__ = "/Users/thiagolopes/Downloads/TD_Epinefrina_LC-wPBE_49000_OPT.log"
    x = TransitionContribution(file__).getTransitions()
    w = FrontierOrbitals(file__)
