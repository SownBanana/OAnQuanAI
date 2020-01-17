# AlphaZero play Ô ăn quan
----
## Project Information
- **Neural Network**: `Oanquan/tensorflow/` `OAnQuanNNet.py` là mạng CNN 1 lớp, `NNet.py` chứa các hàm *train, predict*.
- **MCTS**: Logic cây MCTS nằm trong `MCTS.py`.
- **Game Ô ăn quan**: Logic game nằm trong `Oanquan/Logic.py`, tương tác với hệ thống `Oanquan/Game.py`
- **Huấn luyện**: `Coach.py`
- **Môi trường thi đấu** `Arena.py`
----
## Training - Tự học thông qua Selfplay
1. Ta train neural network bằng cách chạy `main.py`

1. Model khi train sẽ được lưu trong `temp/` (có thể chọn đường dẫn khác) bằng tên `best.ph.tar`. Thông tin của model cũng như examples gồm có `x.index` `x.meta` `x.data-00000-of-00001`.
1. Ban đầu, khi chưa có model, phải để giá trị `checkpoint` là *False*.

1. Một số giá trị args cần lưu ý khi train:

>numEps: số lần selfplay để lấy examples

>updateThreshold: tỉ lệ thắng tối thiểu để chấp nhận model mới

>numMCTSSims: số nước giả lập

>load_model: True để tiếp tục train model cũ

>checkpoint: cài đặt nơi lưu examples và model được train (best.ph.tar)

>load\_folder\_file: ('thư mục cha', 'model') - chọn model để train tiếp


----
## Backup
 Có thể lưu lại `best.ph.tar` vào thư mục khác để dùng sau này.
 
 Lưu ý, cần lưu trữ cả 3 file
 `best.ph.tar.index` `best.ph.tar.meta` `best.ph.tar.data-00000-of-00001`
 
 [Model đã được train]()

----
## Play
 #### 1. With Command Line

 > player 1 | 0 | 1 | 2 | 3 | 4 | 5 |
 
 > player -1| 5 | 4 | 3 | 2 | 1 | 0 |

 - Nếu không cần sử dụng giao diện, thi đấu bằng cách chạy `pitOAQ.py`
 - Chọn người chơi bằng cách gán cho `player1` và `player2`:
  - `random_fighter`: nước đi được chọn ngẫu nhiên.
  - `human_player`: người chơi chọn số *x* từ 0-11 theo luật:
    - từ 0-5 để đi theo chiều kim đồng hồ ở ô *x*.
    - từ 6-11 để đi ngược chiều kim đồng hồ ở ô *x-5*
  - `fist_mcst_fighter` và `second_mcst_fighter`: AI với neural network và numMCTSSims được chọn. Cây MCTS sẽ được duy trì mở rộng.
 
 #### 2. With User Interface
 Giao diện nằm trong `OAnQuanUI\`.
 
 Cách chơi bằng giao diện:
 - Chạy `OAnQuanUI\ASever.jar`, chọn chế độ chơi qua mạng, click vào *Kết Nối*
 - Chạy 2 file `OAnQuanUI\AClient.jar`, sửa lại đường dẫn hoặc tên của file send.txt và receive.txt của 2 client cho khác nhau.
 - Để AI chơi bằng giao diện:
   - Mở `fighter.py`
   - Sửa lại đường dẫn của send và receive trong `fighter.py` cho khớp với đường dẫn send và receive của 1 trong 2 Client đã cài đặt ở trên.
   - Chọn model chơi ở **net.load_checkpoint**. VD: `net.load_checkpoint('./BackupBest/', 'bestofbest.pth.tar')`
   - Chọn **numMCTSSims**, số giả lập càng lớn thì càng 'thông minh' nhưng sẽ tăng thời gian 'suy nghĩ'.
   - Chạy `fighter.py`
   - Nếu muốn 2 máy đấu với nhau, mở `a.py` em đã copy sẵn và cài đặt tương tự như `fighter`
 - Trở lại với 2 `AClient.jar`, click *CONNECT*, đợi connect xong.
 - Trên `ASever.jar`, đến khi có đủ 2 kết nối, ta có thể click *Vào game* để bắt đầu chơi.
 
----
 ## Library
 `tensorflow` `pytorch` `numpy` `pandas` 
