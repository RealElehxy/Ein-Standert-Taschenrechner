import time

while True:
    zahl1 = int(input("Bitte gib die erste Zahl ein! : "))
    print(f"Du hast {zahl1} eingegeben!\n")
    
    operator = input("Bitte gib das Rechenzeichen ein (+, -, *, /) : ")
    print(f"Du hast '{operator}' eingegeben!\n")
    
    zahl2 = int(input("Bitte gib die zweite Zahl ein! : "))
    print(f"Du hast {zahl2} eingegeben!\n")
    
    print("Bitte warte, ich rechne...")
    time.sleep(1.5)
    
    ergebnis = 0
    if operator == "+":
        ergebnis = zahl1 + zahl2
    elif operator == "-":
        ergebnis = zahl1 - zahl2
    elif operator == "*":
        ergebnis = zahl1 * zahl2
    elif operator == "/":
        ergebnis = zahl1 / zahl2
    else:
        print("Unbekanntes Rechenzeichen! Ich konnte nicht rechnen.")
        print("-" * 30)
        continue
        
    print("")
    print(f"Das Ergebnis ist: {ergebnis}")
    print("-" * 30)
    print("")
