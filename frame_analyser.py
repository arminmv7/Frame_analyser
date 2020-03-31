import frame_analysis_class
length = int(input ("Input member lentgh (m) : "))
j1con = int( input ("Define first joint connection :\n 1:pin  2:fix  3:none\nYour choice : "))
j2con = int(input ("Define second joint connection :\n 1:pin  2:fix  3:none\nYour choice : "))
loadtype = int(input ("Define type of loads :\n 1:uniform load -- 2:point load\nYour choice : "))
loadpos = int(input ("Input position of applied load (distance from first joint)(m) :"))
loadvalue = int(input ("Input load value (ton) : "))
analyser1 = frame_analysis_class.frame_analysis(length,j1con,j2con,loadtype,loadpos,loadvalue)
if j1con == 1 and j2con == 1:
    analyser1.FA_pin_pin()
    analyser1.printmessage()
elif j1con == 2 and j2con == 3:
    analyser1.FA_fix_none()
    analyser1.printmessage()
elif j1con == 3 and j2con ==2:
    analyser1.FA_none_fix()
    analyser1.printmessage()
else:
        print ("------------------------\n****WARNING**** Your model is NOT defined")
    

    
    
