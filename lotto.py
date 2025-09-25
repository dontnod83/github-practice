import tkinter
import tkinter.font
import random

lotto_num = range(1, 46)

def buttonClick():
    nums = sorted(random.sample(lotto_num, 6))   # 6개 번호 추출 후 정렬
    print(nums)                                  # 터미널에도 출력
    label_var.set(" ".join(map(str, nums)))      # GUI 라벨에 표시

window = tkinter.Tk()
window.title("lotto")
window.geometry("500x300")
window.resizable(False, False)

# 결과를 보여줄 라벨 변수
label_var = tkinter.StringVar()
label_var.set("버튼을 눌러 번호를 생성하세요")

# 결과 라벨
label = tkinter.Label(window, textvariable=label_var, font=("Arial", 20))
label.pack(pady=20)

# 버튼
button = tkinter.Button(window, overrelief="solid",
                        text="번호확인", width=15, command=buttonClick,
                        repeatdelay=1000, repeatinterval=100)
button.pack()

window.mainloop()
