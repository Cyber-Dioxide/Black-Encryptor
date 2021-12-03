import os, pyfiglet
os.system("clear")
while True:
    import os, pyfiglet
    from colorama import Fore
    import random

    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'
    all_col = [red, green, orange, cyan, lightred, lightgreen, yellow, lightcyan]
    ran = random.choice(all_col)

    


    def banner():
        en = pyfiglet.figlet_format("Black\nEncryptor\n")
        print(ran, en)
        print("\n\n")
        print(Fore.CYAN, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
        print(Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
        print(Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)


    banner()

    print(ran + "[1] Encrypt Text\n[2] Decrypt Text\n[3]Exit ")

    choice = input(ran + "Enter your choice: ")


    def encrypt():
        text = input(ran + "Enter the text to Encrypt: ")

        text = text.replace("A", "Ç")
        text = text.replace("a", "ü")
        text = text.replace("B", "é")
        text = text.replace("b", "â")
        text = text.replace("C", "ä")
        text = text.replace("c", "ç")
        text = text.replace("D", "à")
        text = text.replace("d", "å")
        text = text.replace("E", "ý")
        text = text.replace("e", "ø")
        text = text.replace("F", "•")
        text = text.replace("f", "þ")
        text = text.replace("G", "Ú")
        text = text.replace("g", "Ý")
        text = text.replace("H", "Þ")
        text = text.replace("h", "Ã")
        text = text.replace("I", "Û")
        text = text.replace("i", "š")
        text = text.replace("J", "˜")
        text = text.replace("j", "Š")
        text = text.replace("K", "Ÿ")
        text = text.replace("k", "Ø")
        text = text.replace("L", "ë")
        text = text.replace("l", "™")
        text = text.replace("M", "Ü")
        text = text.replace("m", "ê")
        text = text.replace("N", "ï")
        text = text.replace("n", "Ù")
        text = text.replace("O", "è")
        text = text.replace("o", "¾")
        text = text.replace("P", "È")
        text = text.replace("p", "æ")
        text = text.replace("Q", "ã")
        text = text.replace("q", "►")
        text = text.replace("R", "ƒ")
        text = text.replace("r", "‰")
        text = text.replace("S", "╨")
        text = text.replace("s", "Ë")
        text = text.replace("T", "Æ")
        text = text.replace("t", "î")
        text = text.replace("U", "ð")
        text = text.replace("u", "À")
        text = text.replace("V", "ô")
        text = text.replace("v", "£")
        text = text.replace("W", "¥")
        text = text.replace("w", "õ")
        text = text.replace("X", "Á")
        text = text.replace("x", "ì")
        text = text.replace("Y", "Â")
        text = text.replace("y", "Ê")
        text = text.replace("Z", "¢")
        text = text.replace("z", "ö")
        text = text.replace("0", "û")
        text = text.replace("1", "ÿ")
        text = text.replace("2", "ò")
        text = text.replace("3", "├")
        text = text.replace("4", "┌")
        text = text.replace("5", "⌂")
        text = text.replace("6", "║")
        text = text.replace("7", "≤")
        text = text.replace("8", "ù")
        text = text.replace("9", "á")
        text = text.replace(" ", "»")
        print(ran + "\n\n\tGetting things ready- - - - - - \t\n\n")

        print(text)


    def decrypt():
        text = input(ran + "Enter the text to Decrypt: ")

        text = text.replace("Ç", "A")
        text = text.replace("ü", "a")
        text = text.replace("é", "B")
        text = text.replace("â", "b")
        text = text.replace("ä", "C")
        text = text.replace("ç", "c")
        text = text.replace("à", "D")
        text = text.replace("å", "d")
        text = text.replace("ý", "E")
        text = text.replace("ø", "e")
        text = text.replace("•", "F")
        text = text.replace("þ", "f")
        text = text.replace("Ú", "G")
        text = text.replace("Ý", "g")
        text = text.replace("Þ", "H")
        text = text.replace("h", "Ã")
        text = text.replace("Û", "I")
        text = text.replace("š", "i")
        text = text.replace("˜", "J")
        text = text.replace("Š", "j")
        text = text.replace("Ÿ", "K")
        text = text.replace("Ø", "k")
        text = text.replace("ë", "L")
        text = text.replace("™", "l")
        text = text.replace("Ü", "M")
        text = text.replace("ê", "m")
        text = text.replace("ï", "N")
        text = text.replace("Ù", "n")
        text = text.replace("è", "O")
        text = text.replace("¾", "o")
        text = text.replace("È", "P")
        text = text.replace("æ", "p")
        text = text.replace("ã", "Q")
        text = text.replace("►", "q")
        text = text.replace("ƒ", "R")
        text = text.replace("‰", "r")
        text = text.replace("╨", "S")
        text = text.replace("Ë", "s")
        text = text.replace("Æ", "T")
        text = text.replace("î", "t")
        text = text.replace("ð", "U")
        text = text.replace("À", "u")
        text = text.replace("ô", "V")
        text = text.replace("£", "v")
        text = text.replace("¥", "W")
        text = text.replace("õ", "w")
        text = text.replace("Á", "X")
        text = text.replace("ì", "x")
        text = text.replace("Â", "Y")
        text = text.replace("Ê", "y")
        text = text.replace("¢", "Z")
        text = text.replace("ö", "z")
        text = text.replace("û", "0")
        text = text.replace("ÿ", "1")
        text = text.replace("ò", "2")
        text = text.replace("├", "3")
        text = text.replace("┌", "4")
        text = text.replace("⌂", "5")
        text = text.replace("║", "6")
        text = text.replace("≤", "7")
        text = text.replace("ù", "8")
        text = text.replace("á", "9")
        text = text.replace("»", " ")

        print(ran + "\n\n\tGetting things ready- - - - - - \t\n\n")

        print(text)


    def exit():
        os.system("exit")


    if choice == "1":
        encrypt()
    elif choice == "2":
        decrypt()
    elif choice == "3":
        print(ran + "\n\tDont Forget to do following tasks :-)\t\n")
        print(Fore.CYAN, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
        print(Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
        print(Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)
        exit()

    else:
        print(ran + "\nInvalid option")
        exit()
        
    input(ran+"press enter to continue")











