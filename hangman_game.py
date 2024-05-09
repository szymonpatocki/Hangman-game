import sys
import random

number_of_tries = 6
start_game = 1 
choice = 100
letter = "litera"
used_letters = []
user_word = []
special_character = ["@","!","#","$","%","^","&","*","(",")","-","_","=","+","`","~","[","]","{","}",":","'",'"',"\ ","<",">",",",".","?","/","*"]   
EU_countries = ["albania","andora", "austria", "belgia","białoruś","bośnia i hercegowina","bułgaria","chorwacja","czarnogóra","czech","dania","estonia","finlandia","francja","grecja","hiszpania","holondia","irlandia","kazachstan","liechtenstein","litwa","luksemburg","łotwa","macedonia północna","malta","mołdawia","monako","niemcy","norwegia","polska","portugalia","rosja","rumunia","san marino","serbia","słowacja","słowenia","szwajcaria","szwecja","trucja","ukraina","watykan","węgry","wielka brytania","włochy"]
EU_capitals = ["tirana","andora","wiedeń","bruksela","mińsk","sarajewo","sofia","zagrzeb","podgorica","praga","kopenhaga","tallinn","helsinki","paryż","ateny","madryt","amsterdam","dublin","reykjavik","nur sułtan","vaduz","wilno","luksemburg","ryga","skopje","valletta","kiszyniów","monako","berlin","oslo","warszawa","lizbona","moskwa","bukareszt","san marino","belgrad","bratysława","lublana","sztokholm","ankara","kijów","watykan","budapeszt","londyn","rzym"]
US_countries = ["antigua i barbuda","argentyna","bahamy","barbados","belize","boliwia","brazylia","chile","dominika","dominikana","ekwador","grenada","gujana","gwatemala","haiti","honduras","jamajka","kanada","kolumbia","kostaryka","kuba","meksyk","nikaragua","panama","paragwaj","peru","saint kitts i nevis","saint lucia","saint vincent i grenadyny","salwador","stany zjednoczone","surinam","trynidad i tobago","urugwaj","wenezuela"]
US_capitals = ["saint johns","buenos aries","nassau","bridgetown","belmopan","surce","brasillia","santiago","roseau","santo domingo","quito","saint georges","georgetown","gwatemala","port au prince","tegucigalpa","kingston","ottawa","bogota","san jose","hawana","meksyk","managua","panama","asuncion","lima","basseterre","casteries","kingstwon","san salvador","waszyngton","paramaribo","port of spain","montevideo","caracas"]
animals = ["pszczoła","niedźwiedź","kaczka","bóbr","dziobak","nietoperz","wilk","żyrafa","lew","wąż","hipopotam","krokodyl","żółw","rekin","wieloryb","kot","pies","foka","nosorożec","alpaka","aligator","żóbr","biedronka","bocian","czapla","bizon","bażant","baran","owca","delfin","dzik","sarna","łoś","dodo","mrówkojad","goryl","małpa","panda","orangutan","mysz","mors","morświn","motyl","wombat","wielbłąd","świnia","wiewiórka","wrona","wróbel","sroka","orzeł","jastrząb","szerszeń","pantera","tygrys","papuga","pelikan","pawian","pingiwn","puma","nosacz sundajski","norka","kret","gęś","rak","renifer","ropucha","rozgwiazda"]
names = ["kamil","sebastian","stefan","agnieszka","mikołaj","jan","kuba","jakub","rafał","konrad","patryk","szymon","natalia","marcin","damian","wioletta","daria","zuzanna","mateusz","adam","albert","adrian","adrianna","ania","dariusz","łukasz","sławomir","norbert","stanisław","jerzy","józej","ireneusz","wojtek","władysław","Agata","weronika","kasia","zofia","elenka","barbara","bartosz","wiktor","Igor","jadwiga","mieszko","oskar","michał","karol","filip"]
league_of_legends = ["aatrox","agri","akali","akshan","alistar","amumu","aniva","annie","aphelios","ashe","aurelion sol","azir","bard","belveth","blitzcrank","brand","braum","caitlyn","ca,mille","cassiopeia","cho gath","corki","darius","diana","dr mundo","draven","ekko","elise","evelynn","ezreal","fiddlesticks","fiora","fizz","galio","gangplank","garen","gnar","gragas","graves","gwen","hecarim","heimerdinger","illaoi","irelia","ivern","janna","jarvan","jax","jayce","jhin","jinx","kai sa","kalista","karma","karthus","kassadin","katarina","kayle","kayn","kennen","kha zix","kindred","kled","kog maw","leblanc","lee sin","leona","lillia","lissandra","lucian","lulu","lux","malaphite","malzahar","maokai","master yi","miss fortune","mordekaiser","morgana","nami","nasus","nautilus","neeko","nidalee","nilah","nocturne","nunu i willump","olaf","orianna","ornn","pantheon","poppy","pyke","qiyana","quinn","rakan","rammus","rek sai","rell","renata glas","renekton","rengar","riven","rumble","ryze","samira","sejuani","senna","seraphine","sett","shaco","shen","shyvana","singed","sion","sivir","skarner","sona","soraka","swian","sylas","syndra","tahm kench","taliyah","talon","taric","teemon","thresh","tristana","trundle","tryndamere","twisted fate","twitch","udyr","urgot","varus","vayne","veigar","vel koz","vex","vi","viego","viktor","vladimir","volibear","warwick","wukong","xayah","xerath","xin zhao","yasuo","yone","yorick","yuumi","zac","zde","zeri","ziggs","zilean","zoe","zyra"]
electronics = ["rezystor","kondesator","cewka","dioda zenera","dioda lawinowa","fotodioda","wzmacniacz operacyjny","tranzystor bipolarny","woltomierz","amperomierz","wtórnik emiterowy","waraktor","oscyloskop","tranzystor polowy","przetwornica","stabilziator liniowy","dioda led","klucz tranzystorowy","potencjometr","omomierz","zwora","dioda pin"]

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes
def show_state_of_game():
    print()
    print("Pozostało prób:", number_of_tries)
    print(user_word)
    print("Użyte litery:", used_letters)
    print("")
def hangman():
    if number_of_tries == 6:
        print("""    
        _________         
        |/      |    
        |       
        |       
        |      
        |
      __|__                  """) 

    if number_of_tries == 5:
        print("""    
        _________         
        |/      |    
        |       O
        |       
        |      
        |
      __|__                        """) 

    if number_of_tries == 4:
        print("""    
        _________         
        |/      |    
        |       O
        |       | 
        |      
        |
      __|__                        """) 

    if number_of_tries == 3:
        print("""    
        _________         
        |/      |    
        |       O
        |      /| 
        |      
        |
      __|__                          """) 

    if number_of_tries == 2:
        print("""    
        _________         
        |/      |    
        |       O
        |      /|\ 
        |       
        |
      __|__                        """) 

    if number_of_tries == 1:
        print("""    
        _________         
        |/      |    
        |       O
        |      /|\ 
        |      /  
        |
      __|__                       """) 

    if number_of_tries == 0:
        print("""    
        _________         
        |/      |    
        |       O
        |      /|\ 
        |      / \ 
        |
      __|__                      """) 
def new_or_end(game = 0):
    while game !=1:
        try:
            game = int(input("""
1. Zagraj jeszczę raz
2. Zakończ grę
"""))
        except ValueError: 
             game = 0

        if game == 1:
            used_letters.clear()  
            user_word.clear()
            
        elif game == 2:
            sys.exit(0)

print("Gra rozpoczęta!")
print("")

#Blok opisujący logikę gry
while True:
    Flag_special_character = 0
    
    if start_game  == 1:
        start_game  = 0

        print("Wylosuj słowo ze zbioru: ")
        print("1. EU_countries")
        print("2. EU_capitals")
        print("3. US_countries")
        print("4. US_capital")
        print("5. Animals")
        print("6. Names")
        print("7. League_of_Legends")
        print("8. Electronics")

        while choice > 8:
            try:
                choice = int(input("Wybierz zbiór: "))
            except ValueError:
                choice = 100

        if choice == 1:
            random_word = random.randrange(0,len(EU_countries))
            word = EU_countries[random_word]

        if choice == 2:
            random_word = random.randrange(0,len(EU_capitals))
            word = EU_capitals[random_word]

        if choice == 3:
            random_word = random.randrange(0,len(US_countries))
            word = US_countries[random_word]
            
        if choice == 4:
            random_word = random.randrange(0,len(US_capitals))
            word = US_capitals[random_word]
            
        if choice == 5:
            random_word = random.randrange(0,len(animals))
            word = animals[random_word]

        if choice == 6:
            random_word = random.randrange(0,len(names))
            word = names[random_word]

        if choice == 7:
            random_word = random.randrange(0,len(league_of_legends))
            word = league_of_legends[random_word]

        if choice == 8:
            random_word = random.randint(0,len(electronics))
            word = electronics[random_word]

        for _ in word:
            user_word.append("_")
        print(user_word)

        print("")

    letter = input("Podaj literę: ")

    number_of_letter = used_letters.count(letter)

    #Sprawdzanie czy użytkownik wprowadził znak specjalny, jeśli tak Flaga wystawia 1 
    for _ in range(len(special_character)):
        if letter == special_character[_]:
            print("Podano znak specjalny, musisz podać literę!")
            Flag_special_character = 1        

    #Sprawdzanie czy użytkownik podał  cyfrę lub więcej niż jedną literę lub tę samą literę
    if Flag_special_character == 0:
        try:
            if int(letter):
                letter = letter + letter
                print("Podano cyfrę, musisz podać literę!")
                
        except ValueError:    
            if len(letter) !=1:
                print("Podano wiecej niż jedną literę!")

            else:
                if number_of_letter == 0:
                    used_letters.append(letter)

                else:
                    print("Wprowadzoną tą samą literę!")

    found_indexes = find_indexes(word,letter)
    
    if len(letter) == 1:
        if Flag_special_character == 0:
            if number_of_letter == 0:
                if len(found_indexes) == 0:
                    print("Nie ma takiej litery!")
                    number_of_tries = number_of_tries - 1
        
        if number_of_tries == 0:
            hangman()
            show_state_of_game()
            print("Koniec gry!")
            print("\nSzukane słowo to: ", word)
            new_or_end()
            number_of_tries = 6
            start_game  = 1
            choice = 100
            
        else: 
            for index in found_indexes:
                user_word[index] = letter      

            if "".join(user_word) == word:
                hangman()
                show_state_of_game()
                print("Gratulacje, odgadłeś słowo:")
                print("\nSzukane słowo to: ","".join(user_word) )
                new_or_end()
                number_of_tries = 6
                start_game  = 1
                choice = 100
        
            hangman()
            show_state_of_game()



