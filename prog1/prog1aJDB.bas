5  REM Name: Jack Baretz; Class: CSCI 365; Program Number: 1; Part: a;
6  REM Email: jack.baretz@und.edu

10 REM Gets percentage and decides what letter grade it is

20 INPUT "What is the grade percentage?"; P
40 IF P < 0 THEN GOTO 100
41 IF P > 100 THEN PRINT "Number is too high" : GOTO 20
42 IF P >= 90 THEN grade$ = "A" : GOTO 50
43 IF P >= 80 THEN grade$ = "B" : GOTO 50
44 IF P >= 70 THEN grade$ = "C" : GOTO 50
45 IF P >= 60 THEN grade$ = "D" : GOTO 50
46 grade$ = "F" : GOTO 50
50 PRINT "The letter grade is: "; grade$ : GOTO 20
100 END
