from os import system
from random import randint, shuffle, choice
def get(x, s):
    
    try:
        low = x-1
        hi = min((len(s)//3)*x, len(s)-1)
        return s.pop(randint(low, hi))
    except ValueError:
        return s.pop(randint(0, len(s)-1))

def assign_topics(groups):
    
    t ='''"ChatGPT is the start of the apocalypse. Agree or disagree?
"Discord might as well encrypt our messages using the Caesar Cipher! Should all social platforms use end-to-end-encryption?"
"Protect your device now: the risks of botnets, spyware, trojans and other malware."
"How to be E-safe: the risks of spam, phishing and pharming scams."
"Avoiding the cloud - is locally stored data the only sensible option?"
"Copyright infringement is endemic on YouTube."
"2024 will be the year of disinformation: AI and the future of life online."
"Social media addiction: TikTok is the opiate for the masses."'''.splitlines()

    shuffle(t)
    
    while groups:
        topic = choice(t)
        print(groups.pop(), "... you will do...\n")
        print(topic)
        t.remove(topic)
        print("-"*len(topic))
        print()
        input()

    return ""
        

def make_groups():
    out = ""
    s = '''Maya
Java
Herb
Si
Ocean
Trin
Fah-sai
Get
Daniel
James
Anne
Jayden
Proud
Namsai
Tai
James
Uta
Pookan
Miu Miu
Ping
Leslie
Dylan'''.splitlines()
    g_num = 1
    while len(s) > 1:
        t,m,b = get(1,s), get(2,s), get(3,s)
        out += (f"GROUP {g_num}: {t}, {m} & {b}\n")
        g_num += 1
        
    
    out += s[0] + " you may choose which group you join!\n"

    return out

    

if __name__ == "__main__":
    while True:
        x = "a"
        while x not in "GT":
            x = input("G. groups or T. topics? ").upper()

        
        
        while True:
            if x == "G":
                out = make_groups()
            else:
                assign_topics(out.splitlines()[:-1])
            print(out)
            if input("was that a good fit?"):
                break
            system("cls")
