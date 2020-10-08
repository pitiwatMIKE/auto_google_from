from selenium import webdriver
import time
import random

web = webdriver.Chrome('C:/Users/Mike/Desktop/bot_python/chromedriver.exe')
web.get('https://docs.google.com/forms/d/e/1FAIpQLSfB635RPMnXLI4N9MndJ3TugTZG1R670NAkGFaKMDYj4Bn50A/viewform?fbclid=IwAR0QnQYAM4cnMEGvfBFVOtO33yc-Ev3cpPIcjbMyb3779SuJ1CRRSGTNwns')

time.sleep(2)


for i in range(0,100):
    #เพศ
    sex = []
    sex.append(web.find_element_by_xpath('//*[@id="i5"]/div[3]/div')) #ชาย
    sex.append(web.find_element_by_xpath('//*[@id="i8"]/div[3]/div')) #หญิง
    sex_choice = random.choice(sex)
    sex_choice.click()
    
    #คณะ 
    major = []
    major.append(web.find_element_by_xpath('//*[@id="i15"]/div[3]/div')) #วิศวกรรมศาสตร์
    major.append(web.find_element_by_xpath('//*[@id="i18"]/div[3]/div')) #บริหารธุรกิจ
    major.append(web.find_element_by_xpath('//*[@id="i21"]/div[3]/div')) #ศิลปกรรมศาสตร์
    major.append(web.find_element_by_xpath('//*[@id="i24"]/div[3]/div')) #สถาปัตยกรรม
    major_choice = random.choice(major)
    major_choice.click()

    #ชั้นปี
    level = []
    level.append(web.find_element_by_xpath('//*[@id="i31"]/div[3]/div')) #1
    level.append(web.find_element_by_xpath('//*[@id="i34"]/div[3]/div')) #2
    level.append(web.find_element_by_xpath('//*[@id="i37"]/div[3]/div')) #3
    level.append(web.find_element_by_xpath('//*[@id="i40"]/div[3]/div')) #4
    # level.append(web.find_element_by_xpath('//*[@id="i43"]/div[3]/div')) #5
    level_choice = random.choice(level)
    level_choice.click()

    #ได้รับเงินมามหาวิทยาลัยวันละกี่บาท
    money = []
    money.append(web.find_element_by_xpath('//*[@id="i53"]/div[3]/div')) #ต่ำกว่า 100 บาท
    money.append(web.find_element_by_xpath('//*[@id="i56"]/div[3]/div')) #100 - 200 บาท
    money.append(web.find_element_by_xpath('//*[@id="i59"]/div[3]/div')) #200 - 300 บาท
    money.append(web.find_element_by_xpath('//*[@id="i62"]/div[3]/div')) #มากกว่า 300 บาท
    money_choice = random.choice(money)
    money_choice.click()

    #ตอนที่ 2 ทัศนคติต่อการบริโภคผักของนักศึกษา
    question1 = []
    question1.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div')) #เห็นด้วย
    question1.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div')) #เฉยๆ
    question1.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div')) #ไม่เห็นด้วย
    question1_choice = random.choice(question1)
    question1_choice.click()

    question2 = []
    question2.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div')) #เห็นด้วย
    question2.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div')) #เฉยๆ
    question2.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div')) #ไม่เห็นด้วย
    question2_choice = random.choice(question2)
    question2_choice.click()

    question3 = []
    question3.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div')) #เห็นด้วย
    question3.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div')) #เฉยๆ
    question3.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]')) #ไม่เห็นด้วย
    question3_choice = random.choice(question3)
    question3_choice.click()

    question4 = []
    question4.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div')) #เห็นด้วย
    question4.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div')) #เฉยๆ
    question4.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div')) #ไม่เห็นด้วย
    question4_choice = random.choice(question4)
    question4_choice.click()

    question5 = []
    question5.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[10]/span/div[2]/div/div/div[3]/div')) #เห็นด้วย
    question5.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[10]/span/div[3]/div/div/div[3]/div')) #เฉยๆ
    question5.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[10]/span/div[4]/div/div/div[3]/div')) #ไม่เห็นด้วย
    question5_choice = random.choice(question5)
    question5_choice.click()

    question6 = []
    question6.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[12]/span/div[2]/div/div/div[3]/div')) #เห็นด้วย
    question6.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[12]/span/div[3]/div/div/div[3]/div')) #เฉยๆ
    question6.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[12]/span/div[4]/div/div/div[3]/div')) #ไม่เห็นด้วย
    question6_choice = random.choice(question6)
    question6_choice.click()

    question7 = []
    question7.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[14]/span/div[2]/div/div/div[3]/div')) #เห็นด้วย
    question7.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[14]/span/div[3]/div/div/div[3]')) #เฉยๆ
    question7.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[14]/span/div[4]/div/div/div[3]/div')) #ไม่เห็นด้วย
    question7_choice = random.choice(question7)
    question7_choice.click()

    question8 = []
    question8.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[16]/span/div[2]/div/div/div[3]/div')) #เห็นด้วย
    question8.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[16]/span/div[3]/div/div/div[3]/div')) #เฉยๆ
    question8.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[16]/span/div[4]/div/div/div[3]/div')) #ไม่เห็นด้วย
    question8_choice = random.choice(question8)
    question8_choice.click()

    question9 = []
    question9.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[18]/span/div[2]/div/div/div[3]/div')) #เห็นด้วย
    question9.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[18]/span/div[3]/div/div/div[3]/div')) #เฉยๆ
    question9.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[18]/span/div[4]/div/div/div[3]/div')) #ไม่เห็นด้วย
    question9_choice = random.choice(question9)
    question9_choice.click()
    
    question10 = []
    question10.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[20]/span/div[2]/div/div/div[3]/div')) #เห็นด้วย
    question10.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[20]/span/div[3]/div/div/div[3]/div')) #เฉยๆ
    question10.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[20]/span/div[4]/div/div/div[3]/div')) #ไม่เห็นด้วย
    question10_choice = random.choice(question10)
    question10_choice.click()

    #ตอนที่ 3 พฤติกรรมการบริโภคผักของนักศึกษา
    question2_1 = []
    question2_1.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div')) #ทุกครั้ง
    question2_1.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div')) #บางครั้ง
    question2_1.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div')) #ไม่เคย
    question2_1_choice = random.choice(question2_1)
    question2_1_choice.click()

    question2_2 = []
    question2_2.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div')) #ทุกครั้ง
    question2_2.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div')) #เบางครั้ง
    question2_2.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div')) #ไม่เคย
    question2_2_choice = random.choice(question2_2)
    question2_2_choice.click()

    question2_3 = []
    question2_3.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div')) #ทุกครั้ง
    question2_3.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div')) #บางครั้ง
    question2_3.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div')) #ไม่เคย
    question2_3_choice = random.choice(question2_3)
    question2_3_choice.click()

    question2_4 = []
    question2_4.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div')) #ทุกครั้ง
    question2_4.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div')) #บางครั้ง
    question2_4.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div')) #ไม่เคย
    question2_4_choice = random.choice(question2_4)
    question2_4_choice.click()

    question2_5 = []
    question2_5.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[10]/span/div[2]/div/div/div[3]/div')) #ทุกครั้ง
    question2_5.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[10]/span/div[3]/div/div/div[3]/div')) #บางครั้ง
    question2_5.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[10]/span/div[4]/div/div/div[3]/div')) #ไม่เคย
    question2_5_choice = random.choice(question2_5)
    question2_5_choice.click()

    question2_6 = []
    question2_6.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[12]/span/div[2]/div/div/div[3]/div')) #ทุกครั้ง
    question2_6.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[12]/span/div[3]/div/div/div[3]/div')) #บางครั้ง
    question2_6.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[12]/span/div[4]/div/div/div[3]/div')) #ไม่เคย
    question2_6_choice = random.choice(question2_6)
    question2_6_choice.click()

    question2_7 = []
    question2_7.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[14]/span/div[2]/div/div/div[3]/div')) #ทุกครั้ง
    question2_7.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[14]/span/div[3]/div/div/div[3]/div')) #บางครั้ง
    question2_7.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[14]/span/div[4]/div/div/div[3]/div')) #ไม่เคย
    question2_7_choice = random.choice(question2_7)
    question2_7_choice.click()

    question2_8 = []
    question2_8.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[16]/span/div[2]/div/div/div[3]/div')) #ทุกครั้ง
    question2_8.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[16]/span/div[3]/div/div/div[3]/div')) #บางครั้ง
    question2_8.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[16]/span/div[4]/div/div/div[3]/div')) #ไม่เคย
    question2_8_choice = random.choice(question2_8)
    question2_8_choice.click()

    question2_9 = []
    question2_9.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[18]/span/div[2]/div/div/div[3]/div')) #ทุกครั้ง
    question2_9.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[18]/span/div[3]/div/div/div[3]/div')) #บางครั้ง
    question2_9.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[18]/span/div[4]/div/div/div[3]/div')) #ไม่เคย
    question2_9_choice = random.choice(question2_9)
    question2_9_choice.click()

    question2_10 = []
    question2_10.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[20]/span/div[2]/div/div/div[3]/div')) #ทุกครั้ง
    question2_10.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[20]/span/div[3]/div/div/div[3]/div')) #บางครั้ง
    question2_10.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[20]/span/div[4]/div/div/div[3]/div')) #ไม่เคย
    question2_10_choice = random.choice(question2_10)
    question2_10_choice.click()

    question2_11 = []
    question2_11.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[22]/span/div[2]/div/div/div[3]/div')) #ทุกครั้ง
    question2_11.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[22]/span/div[3]/div/div/div[3]/div')) #บางครั้ง
    question2_11.append(web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[22]/span/div[4]/div/div/div[3]/div')) #ไม่เคย
    question2_11_choice = random.choice(question2_11)
    question2_11_choice.click()

    summit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div/span')
    summit.click()

    again = web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    again.click()
