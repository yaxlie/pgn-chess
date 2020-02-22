# Dostępne filtry

**Filtr #0:**
 * min_difference_filter(args):
 * Filtr przepuszcza dalej, jeżeli różnica w ocenie pozycji pomiędzy najlepszym, a drugim najlepszym ruchem jest większa niż podany parametr wejściowy cp

**Filtr #1:**
* simple_capture_filter(self, move, board)
* Filtr nie przepuszcza dalej, jeżeli ruch jest zbiciem (odbiciem) materiału, którego przeciwnik nie może 'odbić' w kolejnym ruchu

**Filtr #2:**
* simple_gain_or_exchange_filter(move, board)
* Filtr nie przepuszcza dalej, jeżeli ruch jest zbiciem figury o wyższej bądź tej samej wartości, co figura / pionek, która ją zbija
* Ważność bierek: królowa > wieża > goniec, skoczek > pionek
* Np.:
  * Filtr nie przepuści zbicia damy przez wieżę - jest to raczej oczwisty, mało interesujący ruch
  * Filtr przepuści zbicie wieży przez damę - biorąc pod uwagę, że najpierw ruch musi pomyślnie przejść przez Filtr #1, wiadome jest, że dama będzie mogła zostać zbita podczas ruchu przeciwnika. Taki ruch może być potencjalnie ciekawy i nietrywialny
  * Filtr przepuszcza także wszystkie ruchy, które nie są biciem


**Filtr #3:**
* difference_between_depth_filter(args, move, board, communicator, game)
* idea: przepuścić ruchy, które na pierwszy rzut oka (mała głębokość) wydają się być słabe, ale po dłuższym rozpatrzeniu (większa głębokość) wydają się być znacznie lepsze
* filtr można dostosować poprzez ustawienie:
  * mniejszej głębokości przeszukiwania
  * wymaganej różnicy cp pomiędzy najlepszym ruchem znalezionym na większej głębokości, a ruchem znalezionym na mniejszej głębokości
