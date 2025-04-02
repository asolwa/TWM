# Part 1

## Zad 1
Accuracy train: 100.000000
Accuracy test: 87.777778

Skutecznosc na zbiorze terningowym moze sugerowac wystoapienie overfitiingu.

## Zad 2
Funckja kosztu maleje wraz ze wzrostem liczby cech, az do momentu liczba cech == 14. nastpnie koszt dla zbioru walidacyjnego rosnie znaczaco, zas dla terningowego rosnie wciaz.
Jest to zgodne z przewydiwyaniami, Kolejen zwiekszanie cech, od 14, powoduje ze model uczy sie zapamietywac konkretne elementy zbioru treningowego, zamiast jakies ogolniejsze cechy podobne dla danej klasy opbiektow.

Na wykresioe skutecznosci rowniez wydac spadek skutecznosci dla liczby cech bedaceh wiekeszj niz 15.

Ze wzgledu na to, liczba cech 14 wydaje sie optymalna

## Zad 3

Zwiekszenie wilosci zbioru wykazuje tendencje wzrostowe skutecznosci i malejace dla kosztu.
Lecz z racji na spore zmiany skutecznosci dla zbioru terningowego, moze sugerowac ze dostrojenie modelu w poprzednich krokach spowodowalo ovefitting.

## Zad 4

Widac ponownie dendencje do overfittingu/przeluczenia. Do pewnego kroku model sie uczy. Lecz do pewnej iteracji, koszt zaczyna sie zwiekszac dla zbioru walidacyjnego.
Sugeruje to iz model zaczyna zapamietywac konkretne zdjecia w zbiorze testowym, nie zas uczyc sie generalnych cech klasyfikujacych dana klase obiektow.

Na podstawie wykresow wartosc iter_sel=20 zostala wybrana.
Dla takiej warotsci, model osiaga niska wartosc dla zbioru testowego, ale nie najnizszcza, gdyz ciage zwiekszanie makymalnej iteracji wciaz zmniejsza blad dla zbioru testowego.

## Zad 5
lambda = 0.0138
Skutecznosc 89.05

<!-- lambda = 0.001 -->
<!-- Skutecznosc 89.05 -->

Siatka byla kulkukrotnie przyblizana na zakresie zawierajacym maximum skutecznosci dla zbioru walidacyjnego.
Po 3 iteracja znalezion punkt lambda = 0.0138, dla ktorego sktuczenosci wynosila 89.52

## Zad 6
Accuracy train: 93.333333
Accuracy test: 87.777778

Wynik jest identyczny do wyniku uzyskanego w zadaniu 1.
Oznacza to iz regularyzacja nie poprawila wynikow, oznacza to iz model nie byl przeluczony, co uzycie regularyzacji mialo wykazac.


# Part 2

## Zadanie 2.1
Do wyboru k, dla k-cross-validacji, przetestowano zachowanie algorytmu, dla roznych warotsci k <2, 20>.
Dla uzyskanego wykresu wartosc 7. dawala najwieksza skutecznosc

## Zadanie 2.2 Code

## Zadanie 2.3
img 1
img 2


                                                                                             0.9
0.1000      0.8238    0.8714    0.8524    0.8619    0.8524    0.8619    0.8667    0.8667    0.8619    0.8571
22.3111     0.8714    0.9000    0.8857    0.8905    0.8619    0.8571    0.8857    0.8905    0.8952    0.8857
44.5222     0.8476    0.8905    0.8667    0.8810    0.8667    0.8619    0.8714    0.8762    0.8714    0.8810
66.7333     0.8476    0.9048    0.8667    0.8905    0.8667    0.8524    0.8571    0.8429    0.8905    0.8476
88.9444     0.8667    0.8952    0.8667    0.8857    0.8905    0.8619    0.8476    0.8810    0.8714    0.8476
111.1556    0.8714    0.8714    0.8619    0.8571    0.8667    0.8571    0.8286    0.8810    0.8667    0.8762
133.3667    0.8619    0.8905    0.8762    0.8810    0.8476    0.8762    0.8905    0.8762    0.8476    0.8810
155.5778    0.8524    0.8952    0.8762    0.8857    0.8667    0.8714    0.8714    0.8667    0.8476    0.8476
177.7889    0.8381    0.8714    0.8857    0.8762    0.8905    0.8667    0.8524    0.8619    0.8667    0.8524
200.0000    0.8619    0.8571    0.8857    0.8714    0.8429    0.8857    0.8714    0.8619    0.8619    0.8667

## Zadanie 3
best_c = 144.7625
best_gamma = 0.1362
best_cv_accuracy = 0.9095
