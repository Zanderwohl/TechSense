import SystemV
import SystemM
import System

class SystemC():
    def __init__(self, solarSystem):
        self.ss = solarSystem
        self.time = 0
    
    def exit(self, state):
        print('Exit function yet to be determined. (' + str(state) + ')')

    def showWindow(self):
        print('Starting Solar System UI')
        i = 0
        SystemV.showWindow(self)
        print('Done')

    def setTime(self, newTime):
        self.time = newTime

solar = System.testSystem

window = SystemC(solar)
window.showWindow()
