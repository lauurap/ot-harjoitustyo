```mermaid
 classDiagram
      Board <|-- Game
      Humanplayer <|-- Game
      class Board{
          numbers
          print_board()
          set_mark()
          check_win()
          check_board_full()

      }
      class Game{
          start_game()
          play_game()
      }
      class Humanplayer{
          name
          mark
      }
```