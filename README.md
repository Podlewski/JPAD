# JPAD

<img src="https://static.dwcdn.net/css/flag-icons/flags/4x3/pl.svg" height="10" width="20"> Laboratoria z **Języków programowania w analizie danych** na Politechnice Łódzkiej (PŁ). Więcej informacji o przedmiocie: [karta przedmiotu](https://programy.p.lodz.pl/ectslabel-web/przedmiot_3.jsp?l=pl&idPrzedmiotu=172755&pkId=1149&s=1&j=0&w=informatyka%20stosowana&v=3).

<img src="https://static.dwcdn.net/css/flag-icons/flags/4x3/gb.svg" height="10" width="20"> **Programming Languages For Data Analysis** classes at Lodz University of Technology (TUL).

---

## Zadanie 1

Zadanie polega na przeprowadzeniu analizy statystycznej dla wybranego zbioru danych.

1. Dla danych **Abalone**:
    1. Dla poszczególnych atrybutów wyznaczyć medianę, minimum i maximum dla cech ilościowych i dominantę dla cech jakościowych.
    2. Narysować histogramy dla dwóch cech ilościowych najbardziej ze sobą skorelowanych.
    3. Zadbać o czytelność rezultatów oraz staranny i atrakcyjny wygląd histogramów.
2. Dla danych **Births**:
    1. Zbadać hipotezę, że dzienna średnia liczba urodzeń dzieci wynosi: 10000.
    2. Zwizualizować rozkłady na histogramie.
    3. Zaznaczyć na wykresie punkt dotyczący badanej hipotezy.

## Zadanie 2

Zadanie polega na przeprowadzeniu wstępnego przetwarzania danych w zakresie zastępowania danych brakujących oraz porównania charakterystyki zbioru przed / po imputacji:

1. Wczytać dane z brakami / wygenerować braki w danych (8%, 15%, 30% oraz 45%)
2. Wyznaczyć krzywą regresji dla braków bez danych
3. Uzupełnić braki wybraną metodą:
    1. Mean imputation
    2. Interpolacja
    3. Hot-Deck (wersja LOCF)
    4. Wartości uzyskane z krzywej regresji wyznaczonej na podstawie danych bez braków
4. Porównać charakterystykę zbiorów przed oraz po imputacji (średnia, odchylenie standardowe, kwartyle)
5. Wyznaczyć krzywą regresji dla danych po imputacji oraz porównać jak zmieniły się parametry krzywej

## Zadanie 3

Zadanie polega na przeprowadzeniu analizy eksploracyjnej dla wybranego zbioru danych:

1. Przeprowadzić klasyfikację za pomocą wybranej techniki klasyfikacji (np. MLP, SVM, **SGD**, etc.)
2. Wykonać wykres z przedstawioną skutecznością klasyfikatora (procent poprawnie sklasyfikowanych próbek) od liczby iteracji/epok.
3. Dokonać analizy głównych składowych (PCA) i zredukować liczbę cech do 2 składowych.
4. Ponownie przeprowadzić klasyfikację i porównać wyniki.
5. Dokonać wyboru cech pozostawiając tylko 2, a odrzucając cechy o a) największej wariancji, b) najmniejszej wariancji
6. Na zredukowanej liczbie cech przeprowadzić klasyfikację klasyfikatorem z wymagań na ocenę dostateczną.
7. Eksperyment powtórzyć wykorzystując do selekcji test niezależności chi^2.
8. Wykonać odpowiednie wykresy.
9. Dokonać analizy skupień przy pomocy wybranego algorytmu (np. k-means, meanshift, spectral clustering, etc.) używając cech wyznaczonych przez PCA w części zadania na ocenę dostateczną oraz cech wyznaczonych w wymaganiach na ocenę dobrą.
10. Sprawdzić jakość utworzonych skupień za pomocą wybranego przez siebie kryterium. Przeanalizować wyniki, wykreślić wykresy, jeśli są wskazane.
