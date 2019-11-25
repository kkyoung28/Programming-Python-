#2303 김가영
#여러떡볶이집 떡볶이를 한번에 여러 개를 시킬 수 있는 프로그램
#금액 지불 후 거스름 돈도 볼 수 있으며 주문 취소도 가능.

class bokki:
    _sauces = ["짜장", "착함", "기본", "핫", "핫핫핫"]
    _tteoks = ["밀가루","쌀","치즈","고구마"]
    _tteokadds = ["튀김(떡볶이에)","치즈","김","선택하지않음"]
    _menuadds = ["튀김","어묵","계란찜","음료","선택하지않음"]

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.sauce = 2 #0:짜장, 1:착함, 2:기본, 3:핫, 4:핫핫핫
        self.tteok = 0 #0:밀가루, 1:쌀, 2:치즈(+500), 3:고구마(+500)
        self.tteokadd = 3 #0:튀김(떡볶이/+1500), 1:치즈(+500), 2:김(+500), 3:선택하지않음
        self.menuadd = 4 #0:튀김, 1:어묵, 2:계란찜, 3:음료, 4:선택하지않음

    def set_sauce(self):
        self.sauce = input("소스를 선택하세요.(0:짜장 1:착함 2:기본 3:핫 4:핫핫핫)")
        if self.sauce == "": #그냥 엔터치면 기본값 설정
          self.sauce = 2
        else:
            self.sauce = int(self.sauce)

    def set_tteok(self):
        self.tteok = input("떡볶이에 들어갈 떡을 선택하세요.(0:밀가루, 1:쌀, 2:치즈(+500), 3:고구마(+500))")
        if self.tteok == "":
          self.tteok = 0
        else:
          self.tteok = int(self.tteok)

        if self.tteok == 2: #치즈 선택시 500원 추가
          self.price += 500
        elif self.tteok == 3: #고구마 선택시 500원 추가
          self.price += 500         

    def set_tteokadd(self):
        self.tteokadd = input("떡볶이에 추가할 것을 선택하세요.(0:튀김(떡볶이/+1500), 1:치즈(+500), 2:김(+500), 3:선택하지않음)")
        if self.tteokadd == "":
          self.tteokadd = 3
        else:
          self.tteokadd = int(self.tteokadd)

        if self.tteokadd == 0: #튀김 선택시 1500원 추가
          self.price += 1500
        elif self.tteokadd == 1: #치즈 선택시 500원 추가
          self.price += 500
        elif self.tteokadd == 2: #김 선택시 500원 추가
          self.price += 500  

    def set_menuadd(self):
        self.menuadd = input("추가할 메뉴를 선택하세요 (0:튀김(+3000), 1:어묵(+500), 2:계란찜(+2500), 3:음료(+1500), 4:선택하지않음)")
        if self.menuadd == "":
          self.menuadd = 4
        else:
          self.menuadd = int(self.menuadd)     

        if self.menuadd == 0: #튀김 선택시 3000원 추가
          self.price += 3000
        elif self.menuadd == 1: #어묵 선택시 500원 추가
          self.price +=500
        elif self.menuadd == 2: #계란찜 선택시 2500원 추가 
          self.price +=2500
        elif self.menuadd == 3: #음료 선택시 1500원 추가
          self.price +=1500   

    def __str__(self): #이름:self.name\t컵사이즈:self.sauce\t얼음량:self.tteok\t당도:self.tteok add
        return "이름:"+self.name+"\t가격:"+str(self.price)+"\t소스:"+bokki._sauces[self.sauce]+"\t떡:"+bokki._tteoks[self.tteok]+"\t떡볶이에 추가할 것:"+bokki._tteokadds[self.tteokadd]+"\t추가할 메뉴:"+bokki._menuadds[self.menuadd]

    def order(self):
      self.set_sauce()
      self.set_tteok()
      self.set_tteokadd()
      self.set_menuadd()

class sinjeon(bokki):
    _cuprices=["치즈 1500원","참치마요 1500원","스팸마요 1500원","선택하지않음"]
    def __init__(self, name, price):
        super().__init__(name, price)
        self.cuprice = 0 #0:치즈 1500원, 1:참치마요 1500원, 2:스팸마요 1500원, 3:선택하지않음

    def set_cuprice(self):
        self.cuprice = input("컵밥을 선택하세요(0:치즈 1500원, 1:참치마요 1500원, 2:스팸마요 1500원, 3:선택하지않음)")
        if self.cuprice == "":
          self.cuprice = 3
        else:
          self.cuprice = int(self.cuprice)

        if self.menuadd == 0: #치즈 선택시 3000원 추가
          self.price += 3000
        elif self.menuadd == 1: #참치마요 선택시 3000원 추가
          self.price += 3000
        elif self.menuadd == 2: #스팸마요 선택시 3000원 추가
         self.price += 3000
        
    def __str__(self):
        return super().__str__()+"\t컵밥:"+sinjeon._cuprices[self.cuprice]

    def order(self):
      super().order()
      self.set_cuprice()

class jaws(bokki):
    pass

class Order:
  
  def __init__(self):
    self.order_menu = []

  def show_menu(self):
    print("0:신전떡볶이 3000원, 1:죠스떡볶이 3500원")

  def order_bokki(self):
    
    while True:
      #1. show menu 반복
      self.show_menu()
      
      #2. 주문받기 떡볶이선택  반복
      order = input("무엇을 고르시겠습니까? (엔터 누를 시 주문)")
      if order == "":
      
      #3. 주문한 떡볶이 내용
        for d in self.order_menu:
          print(d)
      
      #4. 합계 금액, 지불 금액 입력 후 거스름 돈 보여주기
        print("총금액: "+str(self.sum_price())+"원")  
        pay = 0
        pay = int(input("지불 금액을 입력하세요 : "))
        change = pay - self.sum_price()
        print('거스름 : ', change, '원')
        self.delete_menu()
        for d in self.order_menu:
          print(d)
        return
      elif int(order) == 0:
        bokki = sinjeon("신전 떡볶이", 3000)
      elif int(order) == 1:
        bokki = jaws("죠스 떡볶이", 3500)
        
      # 떡볶이옵션선택
      bokki.order()
      self.order_menu.append(bokki)
    
    
      #4-2 합계금액
  def sum_price(self):
    sum = 0
    for d in self.order_menu:
      sum += d.price

    return sum

      #6. 주문 취소 후 합계 금액과 지불 금액 거스름 돈
  def delete_menu(self):  
    order = input("주문을 취소하시겠습니까? 0:그대로 진행 1:주문취소")
    if order == 0:
      return
    elif int(order) == 1:
     
      i=0
      for d in self.order_menu:
        print(str(i)+" : "+ str(d))
        i+=1
      while True:  
        delete_menu = input("몇번을 취소하시겠습니까? 엔터 누를 시 주문 끝")
        if delete_menu == "":
          break
        else:
          self.order_menu.pop(int(delete_menu))
        print("총금액: "+str(self.sum_price())+"원")  
        pay = 0
        pay = int(input("지불 금액을 입력하세요 : "))
        change = pay - self.sum_price()
        print('거스름 : ', change, '원')

o = Order()
o.order_bokki()



