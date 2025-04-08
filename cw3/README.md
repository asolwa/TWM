# Part 1

## Zad 1
* Accuracy train: 100.000000
* Accuracy test: 87.777778

Skuteczność na zbiorze treningowym może wskazywać na wystąpienie overfittingu.

## Zad 2
Funkcja kosztu maleje wraz ze wzrostem liczby cech, aż do momentu, gdy liczba cech wynosi 14. Następnie koszt dla zbioru walidacyjnego znacząco rośnie, podczas gdy dla zbioru treningowego nadal maleje.

Jest to zgodne z przewidywaniami – dalsze zwiększanie liczby cech powyżej 14 powoduje, że model zaczyna zapamiętywać konkretne przykłady ze zbioru treningowego zamiast uczyć się ogólnych cech charakterystycznych dla danej klasy obiektów.

Na wykresie skuteczności również widać jej spadek przy liczbie cech większej niż 15.

Z tego powodu liczba cech równa 14 wydaje się optymalnym wyborem.

Koszt | Skutecznosc
:-------------------------:|:-------------------------:
![img1](task2cost.png) | ![img1](task2accuracy.png)

## Zad 3

Zwiększenie rozmiaru zbioru wykazuje tendencję wzrostową skuteczności oraz spadkową dla kosztu.
Jednak ze względu na duże wahania skuteczności na zbiorze treningowym może to sugerować, że wcześniejsze dostrojenie modelu doprowadziło do overfittingu.

Koszt | Skutecznosc
:-------------------------:|:-------------------------:
![img1](task3cost.png) | ![img1](tesk3accuracy.png)

## Zad 4

Ponownie można zauważyć tendencję do overfittingu. Do pewnego momentu model skutecznie się uczy, jednak po określonej liczbie iteracji koszt dla zbioru walidacyjnego zaczyna rosnąć.

Sugeruje to, że model zaczyna zapamiętywać konkretne obrazy w zbiorze treningowym zamiast uczyć się ogólnych cech pozwalających na poprawną klasyfikację obiektów.

Na podstawie wykresów wybrano wartość `iter_sel = 20`. Przy tej wartości model osiąga niski koszt dla zbioru testowego, choć nie najniższy, ponieważ dalsze zwiększanie maksymalnej liczby iteracji wciąż zmniejsza błąd na zbiorze testowym.

Koszt | Skutecznosc
:-------------------------:|:-------------------------:
![img1](task4cost.png) | ![img1](task4accuracy.png)

## Zad 5
* lambda = 0.0138
* Skutecznosc 89.05

Siatka była kilkukrotnie zagęszczana w zakresie obejmującym maksimum skuteczności dla zbioru walidacyjnego.
Po trzech iteracjach znaleziono punkt lambda = 0.0138, dla którego skuteczność wyniosła 89,52%.

Koszt | Skutecznosc
:-------------------------:|:-------------------------:
![img1](task5cost1.png) | ![img1](task5acc1.png)

Koszt | Skutecznosc
:-------------------------:|:-------------------------:
![img1](task5cost2.png) | ![img1](task5acc2.png)

Koszt | Skutecznosc
:-------------------------:|:-------------------------:
![img1](task5cost3.png) | ![img1](task5acc3.png)

## Zad 6
* Accuracy train: 93.333333
* Accuracy test: 87.777778

Wynik jest identyczny do tego uzyskanego w zadaniu 1. Oznacza to, że regularyzacja nie poprawiła wyników, co sugeruje, że model nie był przeuczony, a zatem zastosowanie regularyzacji nie miało wpływu na jego działanie.

# Część 2

## Zadanie 2.1
Do wyboru wartości k dla k-cross-validation przetestowano zachowanie algorytmu dla różnych wartości k w zakresie <2, 20>. Na podstawie uzyskanego wykresu, wartość k = 7 zapewniała najwyższą skuteczność.

![img1](task3.1cv.png)

## Zadanie 2.2 Code

## Zadanie 2.3
Znalezione najlepsze parametry:
* gamma = 0.215
* c = 100
* cv accuracy = 0.9095
* test accuracy 0.9

gamma=logspace(-4, 1, 10); | gamma2=logspace(-2, 1, 10); | gamma=logspace(-1, 0, 10)
:-------------------------:|:-------------------------:|:-------------------------:
c=logspace(-1, 2, 10) | c=logspace(-1, 2, 10) | c=logspace(-1, 2, 10)
:-------------------------:|:-------------------------:|:-------------------------:
![img1](gamma1.png) | ![img1](gamma2.png) | ![img1](gamma3.png)


| C \ Gamma | 0.1   | 0.1292 | 0.16668 | 0.2154 | 0.2783 | 0.3594 | 0.4642 | 0.5995 | 0.7743 | 1.0   |
|-----------|--------|--------|---------|--------|--------|--------|--------|--------|--------|--------|
| 0.1000    | 0.8524 | 0.8667 | 0.8762  | 0.8714 | 0.8714 | 0.8667 | 0.8714 | 0.8714 | 0.8524 | 0.8524 |
| 0.2154    | 0.8714 | 0.8524 | 0.8857  | 0.8810 | 0.8810 | 0.8714 | 0.8762 | 0.8619 | 0.8571 | 0.8571 |
| 0.4642    | 0.8429 | 0.8810 | 0.8952  | 0.8810 | 0.8810 | 0.8857 | 0.8667 | 0.8619 | 0.8619 | 0.8762 |
| 1.0000    | 0.8571 | 0.8714 | 0.8857  | 0.9048 | 0.8905 | 0.8857 | 0.8714 | 0.8714 | 0.8762 | 0.8571 |
| 2.1544    | 0.8524 | 0.8524 | 0.8762  | 0.8810 | 0.9000 | 0.8952 | 0.8810 | 0.8762 | 0.8762 | 0.8714 |
| 4.6416    | 0.8476 | 0.8905 | 0.8905  | 0.8857 | 0.8857 | 0.9048 | 0.8857 | 0.8905 | 0.8762 | 0.8762 |
| 10.0000   | 0.8667 | 0.8905 | 0.8810  | 0.8952 | 0.8810 | 0.8762 | 0.8810 | 0.9048 | 0.8905 | 0.8857 |
| 21.5443   | 0.8571 | 0.8810 | 0.9000  | 0.8810 | 0.8857 | 0.8667 | 0.8429 | 0.8714 | 0.8857 | 0.8952 |
| 46.4159   | 0.8619 | 0.8857 | 0.8952  | 0.8905 | 0.8714 | 0.8667 | 0.8619 | 0.8762 | 0.8857 | 0.8810 |
| 100.0000  | 0.8667 | 0.8667 | 0.8905  | 0.9095 | 0.9095 | 0.8667 | 0.8571 | 0.8714 | 0.8524 | 0.8762 |


## Zadanie 3
Najlepsze parametry zostały znalezione przy użyciu narzędzi do przeszukiwania przestrzeni parametrów:
* c = 144.7625
* gamma = 0.1362
* cv accuracy = 0.9095
* train accuracy = 1.0
* test accuracy = 0.911111
