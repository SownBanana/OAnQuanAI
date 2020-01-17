# OAnQuanAI
----
## Project Information

- **Neural Network**: trong `Oanquan/tensorflow/` `OAnQuanNNet.py` là mạng CNN 1 lớp, `NNet.py` chứa các hàm *train, predict*.
- **MCTS**: Logic cây MCTS nằm trong `MCTS.py`.
- **Game Ô ăn quan**: Logic game nằm trong `Oanquan/Logic.py`, tương tác với hệ thống `Oanquan/Game.py`
----
## Training

1. Ta train neural network bằng cách chạy `main.py`

1. Model khi train sẽ được lưu trong `temp/` (có thể chọn đường dẫn khác) bằng tên `best.ph.tar`. Thông tin của model cũng như examples gồm có `x.index``x.meta``x.data-00000-of-00001`.
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
`best.ph.tar.index``best.ph.tar.meta`
`best.ph.tar.data-00000-of-00001`

----
Base on Alpha Zero -https://github.com/suragnair/alpha-zero-general
