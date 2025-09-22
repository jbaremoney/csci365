1 REM Name: Jack Baretz; Course: CSCI365; Program number: 1; Part:b
2 REM Email: jack.baretz@und.edu
5 REM Loops through 1-100 printing out Fizz, Buzz or number
10 num = 1 : val$ = ""

50 IF num MOD 3 = 0 THEN val$ = val$ + "Fizz"
51 IF num MOD 5 = 0 THEN val$ = val$ + "Buzz" : GOTO 55
52 IF val$ = "" THEN val$ = STR$(num)

55 PRINT val$ : GOTO 60
60 IF num = 100 THEN END
61 num = num + 1 : val$ = "" : GOTO 50 
