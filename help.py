HELP_TEXT = """
Aplikacja pozwala na zakodowanie i odkodowanie wiadomości w plikach HTML lub CSS.
Pierwszy z algorytmów o nazwie 1-RSA działa na pliku CSS. W przypadku pozostałych algorytmów
jako wejście należy wykorzystać plik HTML.

W pierwszym polu należy podać wiadomość którą chcemy ukryć. Następnie wybieramy Encode and Save,
oraz plik w odpowiednim formacie. Informacja o pliku wyjściowym pojawi się w drugim z pól tekstowych.

Aby wydobyć ukryte dane z pliku, należy wybrać plik przyciskiem Select File and Decode, a następnie
wiadomość zostanie wyświetlona w trzecim z pól tekstowych. W przypadku algorytmu 1, w folderze
powinien znajdować się klucz prywatny wygenerowany w procesie chowania wiadomości.

Algorytmy:
1-RSA - generowane są klucze publiczny i prywatny, wiadomość szyfrowana jest kluczem publicznym,
następnie strumień bitów jest zamieniany na spacje (0) i tabulatory (1) i umieszczany po pierwszym
tagu w pliku CSS na końcu linii.

2-Permutation - korzystamy z permutacji (n!) nazw atrybutów oraz wielkości liter tych atrybutów
(wielkie lub małe litery - 2^n) do ukrycia strumienia bitów (wiadomości). Dzięki temu w zaledwie
jednym atrybucie możemy ukryć n*log2(n!) bitów informacji, gdzie n to liczba atrybutów danego tagu.

3-Quot - wiadomość ukryta jest przy wykorzystaniu różnych apostrofów - '' lub "" przy atrybutach HTML.

4-lettercase - wiadomość ukrywana jest przy wykorzystaniu różnej wielkości liter w tagach HTML.

5-space - wewnątrz tagów HTML dodawane są białe znaki, które nie mają wpływu na wygląd strony.
Ich obecność lub jej brak może być wykorzystane do zakodowania 0 lub 1.

project_1 - do tagów dodajemy atrybuty ID, które zawierają zakodowane szesnastkowo, spermutowane
pary znaków (znaki zamieniamy na hex, a następnie permutujemy).

project_2 - zachowanie takie samo jak w przypadku project_1, z dodatkową pseudolosową permutacją
bitów które kodujemy. Wiadomość może być odtworzona dzięki ustalonemu wcześniej seedowi do generatora
pseudolosowego.
"""