class frame_analysis:

# in this class we have objects to do structural analysis
# length = length of member (m)
# j1con = first joint connection type (fix/pin/none)
# j2con = second joint connection type (fix/pin/none)
# loadtype = type of loads (uniform/point)
# loadpos = load apply position (distance from J1) (m)
# loadvalue = value of load (tom.m)
# j1m = the moment of J1 joint (ton.m)
# j1v = the value of shear of J1 joint (ton)
# j2m = the moment of J2 joint (ton.m)
# j2v = the value of shear of J2 joint (ton)
# m_desgin = the value of moment that will be used to design member (ton.m)
# v_desgin = the value of shear force that will be used to design member (ton)

    def __init__(self,length,j1con,j2con,loadtype,loadpos,loadvalue):
        
        self.length = length
        self.j1con = j1con
        self.j2con = j2con
        self.loadtype = loadtype
        self.loadvalue = loadvalue
        self.j1m = 0
        self.j1v = 0
        self.j2m = 0
        self.j2v = 0
        self.m_design = 0
        self.v_design = 0

    def FA_pin_pin(self):

        # frame analyser in pin-pin member
        # j1con = 1 ------ j2con = 1
        # 1:pin    2:fix    3:none

        self.m_design = (self.loadvalue)*(self.length)**2/8
        self.v_design = (self.loadvalue)*(self.length)/2
        self.j1m = 0
        self.j2m = 0
        self.j1v = self.v_design
        self.j2v = self.v_design
        
    def FA_fix_none(self):

        # frame analyser in pin-pin member
        # j1con = 2 ------ j2con = 3
        # 1:pin    2:fix    3:none

        self.m_design = (self.loadvalue)*(self.length)**2/4
        self.v_design = (self.loadvalue)*(self.length)
        self.j1m = (self.loadvalue)*(self.length)**2/4
        self.j2m = 0
        self.j1v = (self.loudvalue)*(self.length)
        self.j2v = 0

    def FA_none_fix(self):

        # frame analyser in pin-pin member
        # j1con = 3 ------ j2con = 2
        # 1:pin    2:fix    3:none

        self.m_design = (self.loadvalue)*(self.length)**2/4
        self.v_design = (self.loadvalue)*(self.length)
        self.j1m = 0
        self.j2m = (self.loadvalue)*(self.length)**2/4
        self.j1v = 0
        self.j2v = (self.loudvalue)*(self.length)

    def printmessage(self):
        
        print ("***************************************")
        print ("The information of first joint :\n")
        print ("Moment = " + str(self.j1m) + " ton.m\n")
        print ("Shear force = " + str(self.j1v) +" ton\n")
        print ("The information of second joint :\n")
        print ("Moment = " + str(self.j2m) + " ton.m\n")
        print ("Shear force = " + str(self.j2v) + " ton\n")
        print ("------------------------\n")
        print ("Design Moment = " + str(self.m_design) + " ton.m\n")
        print ("Design Shear force = " + str(self.v_design) + " ton\n")
               
        


