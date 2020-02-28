import SystemV
import SystemM
import System


class SystemC:
    def __init__(self, solar_system):
        self.ss = solar_system
        self.time = 0
    
    def exit(self, state):
        print('Exit function yet to be determined. (' + str(state) + ')')

    def show_window(self):
        print('Starting Solar System UI')
        i = 0
        SystemV.show_window(self)
        print('Done')

    def set_time(self, new_time):
        self.time = new_time


solar = System.test_system

window = SystemC(solar)
window.show_window()
