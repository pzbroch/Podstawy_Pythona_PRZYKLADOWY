----------------------------------------------------------------------------------------
# **To jest tylko przykładowy egzamin ułożony przeze mnie, aby pokazać Wam jak może to wyglądać na żywo. Zawarte w nim pytania nie pojawią się jako zadania na egzaminie! Warto jednak spróbować swoich sił na sucho :-) Powodzenia!**
----------------------------------------------------------------------------------------

# Podstawy programowania w Pythonie &ndash; egzamin (`przykładowy przypominam  :) `).

Przed przystąpieniem do rozwiązywania zadań przeczytaj poniższe wskazówki

## Jak zacząć?

1. Stwórz [*fork*](https://guides.github.com/activities/forking/) repozytorium z zadaniami.
2. Sklonuj repozytorium na swój komputer. Użyj do tego komendy `git clone adres_repozytorium`
Adres repozytorium możesz znaleźć na stronie repozytorium po naciśnięciu w guzik "Clone or download".
3. Rozwiąż zadania i skomituj zmiany do swojego repozytorium. Użyj do tego komend `git add nazwa_pliku`.
Jeżeli chcesz dodać wszystkie zmienione pliki użyj `git add .` 
Pamiętaj że kropka na końcu jest ważna!
Następnie skommituj zmiany komendą `git commit -m "nazwa_commita"`
4. Wypchnij zmiany do swojego repozytorium na GitHubie.  Użyj do tego komendy `git push origin master`
5. Stwórz [*pull request*](https://help.github.com/articles/creating-a-pull-request) do oryginalnego repozytorium, gdy skończysz wszystkie zadania.

#### Pamiętaj, że pull request musi być stworzony, aby wykładowca dostał Twoje odpowiedzi.

* podczas egzaminu **możesz** korzystać z notatek, kodu napisanego wcześniej, internetu i prezentacji,
* zabroniona jest jakakolwiek komunikacja z innymi kursantami oraz osobami na zewnątrz.

##### Odpowiedzi na pytania opisowe umieszczaj w pliku *answers.txt*.
##### Odpowiedzi na pytania programistyczne umieszczaj w module *answers.py*.

**Powodzenia!**

----------------------------------------------------------------------------------------

#### Zadanie 1. (1pkt)

Jakie są podstawowe istotne różnice między Pythonem 2 oraz Pythonem 3?

#### Zadanie 2. (1pkt)

Czym jest moduł, jak go utworzyć? Czym jest pakiet, jak go utworzyć, z czego się składa?

#### Zadanie 3. (1pkt)

Jakie są podstawowe typy zmiennych przechowujące wartości numeryczne w Pythonie, czym się różnią?

#### Zadanie 4. (2pkt)

Napisz funkcję `revers_sentence`, która przyjmie dowolnie długi napis, po czym zwróci napis będący odwróconym zdaniem z zamianą na dużą literę wszystkich pierwszych liter słów.
przykład:
```python
rev = revers_sentence("Ala ma kota")
print(rev) # Atok Am Ala
```
```python
rev = revers_sentence("Python is easy")
print(rev) # Ysae Si Nohtyp
```

#### Zadanie 5. (3pkt)

Napisz funkcję `count_char`, która pobierze dowolnie długi łańcuch tekstowy oraz pojedynczy znak i sprawdzi, ilość wystąpień podanego znaku. Funkcja powinna zliczać znaki niezależnie od ich wielkości, tj. znaki `a` oraz `A` powinny być traktowane jako to samo! 
przykład:
```python
n = count_char("Ala ma kotA",'a')
print(n) # 4
n = count_char("ala ma kota",'A')
print(n) # 4
n = count_char("Python is easy",'a')
print(n) # 0
```
##### Podpowiedź: zawsze możesz najpierw sprowadzić oba podane napisy do dużych lub małych liter!


#### Zadanie 6. (3pkt)

Napisz funkcje `list_filter`, która przyjmie jako pierwszy argument listę `int_values` zawierającą wartości typu `int` oraz dowolną ( większą od zera ) ilość dodatkowych argumentów - dzielników typu `int` większych od `1`. Funkcja ma zwrócić nową listę z elementami z listy `int_values`, które nie dzielą się przez żaden z podanych dzielników.

##### Przykład:
```python
result = list_filter([1,8,15,20,11], 20)
print(result) # [1,8,15,11]
result = list_filter([1,8,15,20,11], 20,4)
print(result) # [1,15,11]
result = list_filter([1,8,15,20,11], 2, 5, 31)
print(result) # [1,11]
```

#### Zadanie 7. (4pkt)

Napisz funkcję `get_random_elements`, która przyjmie 2 parametry: 

* listę, 
* opcjonalnie: ilość zwracanych elementów, domyślne **1** ,

Następnie funkcja ma zwrócić odpowiednią ilość losowych elementów z pierwotnej listy.

Jeśli użytkownik poda jako ilość, wartość która nie jest całkowita i większą od **0** lub jest większa niż ilość elementów, funkcja ma wyrzucić wyjątek `Exception` z komunikatem "No way to do this!" 

##### Podpowiedź
```python
get_random_elements([1,2,6,3,7]) # [2]
get_random_elements([1,2,6,3,7],3) # [6,2,7]
get_random_elements([1,2,6,3,7],16) # Wyjątek!
```

#### Zadanie 8. (5pkt)

Zapoznaj się z modułem `my_phonebook` umieszczonym w pliku dołączonym do tego egzaminu. Znajdziesz tam listę zawierającą słowniki będące, książkom telefoniczną pewnego programisty.

 Używając Flaska, utwórz stronę, którą udostępnisz pod adresem `/pbk`:
 
 * jeśli użytkownik wejdzie na stronę metodą GET, wyświetl formularz, który:
    * będzie miał pole tekstowe o nazwie `nickname`,
    * będzie miał pole tekstowe o nazwie `number`
    * pola będą odpowiednio opisane

* jeśli użytkownik wejdzie na stronę metodą POST:
    * sprawdź, czy przynajmniej jedno z kryteriów zostało podane 
    * jeśli tak to wyświetl rekordy spełniające odpowiednie kryteria zakładając, że podane napisy mogą być tylko elementem (np. nickname `al` powinien wyświetlić zarówno rekordy dla `Ala Kowalska`, `Al` oraz `Jan Góralski`)
    * jeśli nie lub w przypadku gdy nie uda się nic znaleść, wyświetli napis "No record."
    
**Ważne:** Powołując aplikację Flaska, użyj zmiennej `app`!
