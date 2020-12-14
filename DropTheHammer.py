import time
import pyautogui as pag

# 충전 페이지 URL : c
pag.PAUSE = 0.1
totalCounter = 0

# mouse click
def move_and_click(coords):
    pag.moveTo(x=coords[0]+10, y=coords[1]+5, duration=0.0)
    pag.click()

# 키보드 버튼 누르기
def press_button(button_code):
    #pag.press(button_code)
    pag.keyDown(button_code)
    pag.keyUp(button_code)



if __name__ == '__main__':

    # # 더 충전하기 한번 클릭
    # plus5_button_center = pag.locateOnScreen('./plus5_button_2.PNG')
    # # print(plus5_button_center)8
    # # if plus5_button_center == None :
    # #     plus5_button_center = pag.locateOnScreen('../plus5_button_2.PNG')
    # #     if plus5_button_center == None :
    # #         plus5_button_center = pag.locateOnScreen('../plus5_button_3.PNG')
    #
    # print(plus5_button_center)
    #
    # move_and_click(plus5_button_center)
    #
    #
    # #첫번째 칸으로 이동
    # columnName_PIN_button_center = pag.locateOnScreen('./columnName_PIN_2.PNG')
    # print(columnName_PIN_button_center)
    # # if columnName_PIN_button_center == None :
    # #     columnName_PIN_button_center = pag.locateOnScreen('../columnName_PIN_2.PNG')
    # #     if columnName_PIN_button_center == None:
    # #         columnName_PIN_button_center = pag.locateOnScreen('../columnName_PIN_3.PNG')
    #
    # print(columnName_PIN_button_center)
    # move_and_click(columnName_PIN_button_center)

    # 파일읽기
    with open('./ticketNumbers.txt', "r") as FILE:
        numbers = FILE.read()
    print(numbers)
    #print('1111')
    #파일 내 공백 대쉬 언더라인 지우기
    numbers = numbers.replace(',', '').replace('-', '').replace('_', '').replace(' ', '').replace('\n', '')
    #길이 240 필요함 4+4+4+4+8 = 24 * 10
    #print(len(numbers))

    # 첫번째칸 위에 놓으세요~ 아니면 아래 탭을 주석처리~!!
    #press_button('tab')
    time.sleep(1)

    if len(numbers) != 240 :
        print("번호입력 10개 다한거 맞음?")
    else :
        #번호 입력 10개.
        for atom in numbers :
            totalCounter = totalCounter + 1  # start with 0
            print(atom)
            press_button(atom)

            # # 앞에 핀번호 16자리는 4자리마다 입력 후 탭 누름(칸 이동)
            if (totalCounter % 4 == 0) and (totalCounter <= 17):
                press_button('tab')
            # 24번째는 다음줄로
            elif totalCounter == 24 :
                press_button('tab')

            #한줄 초과 시 카운터 초기화
            if totalCounter > 24 :
                totalCounter = 1



