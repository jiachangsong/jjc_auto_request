from appium import webdriver
import time
desired_caps = {
    'platformName':'Android',
    'platformVersion':'6.0',
    'deviceName':'X2P0215C15008240',
    'appPackage':'com.haodf.android',
    'appActivity':'com.haodf.android.activity.SplashActivity',
    'unicodeKeyboard':True, #使用Unicode编码方式发送字符串
    'reserKeyboard':True #隐藏键盘
}
driver = webdriver.Remote('http://127.0.0.1:7788/wd/hub',desired_caps)

def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

#屏幕向上滑动
def swipeUp(t):
    l=getSize()
    x1=int(l[0]*0.5)
    y1=int(l[1]*0.75)
    y2=int(l[1]*0.25)
    driver.swipe(x1,y1,x1,y2,t)

def swipLeft(t):
    l=getSize()
    x1=int(l[0]*0.75)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.05)
    driver.swipe(x1,y1,x2,y1,t)

def homePage():
    driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
    time.sleep(1)
    driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
    time.sleep(1)
    driver.find_element_by_id("com.haodf.android:id/tv_host").click()
    swipLeft(1000)
    time.sleep(1)
    swipLeft(1000)
    time.sleep(1)
    driver.find_element_by_class_name("android.widget.ImageView").click()
    time.sleep(3)
    driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
    time.sleep(1)
    # 点击【我同意】按钮
    driver.find_element_by_id("com.haodf.android:id/tv_argee").click()
    time.sleep(2)

def login():
    # 点击底部导航【我】
    driver.find_element_by_id("com.haodf.android:id/home_button_4").click()
    time.sleep(2)
    # 点击【登录】按钮
    driver.find_element_by_id("com.haodf.android:id/tv_unlogin").click()
    time.sleep(1)
    # 登录方式：使用用户名密码方式登录
    driver.find_element_by_id("com.haodf.android:id/tv_username_login").click()
    time.sleep(1)
    # 输入账号
    driver.find_element_by_id("com.haodf.android:id/user_account").clear()
    driver.find_element_by_id("com.haodf.android:id/user_account").send_keys("lfstest")
    time.sleep(1)
    # 输入密码
    driver.find_element_by_id("com.haodf.android:id/password").clear()
    driver.find_element_by_id("com.haodf.android:id/password").send_keys("1122")
    time.sleep(1)
    #点击登录
    driver.find_element_by_id("com.haodf.android:id/tv_login").click()
    time.sleep(1)

def searchDoctor():
    # 点击底部导航【首页】
    driver.find_element_by_id("com.haodf.android:id/home_button_1").click()
    time.sleep(2)
    # 点击【搜索输入框】
    driver.find_element_by_id("com.haodf.android:id/tvSearchText").click()
    time.sleep(1)
    #输入医生姓名
    driver.find_element_by_id("com.haodf.android:id/et_search").clear()
    driver.find_element_by_id("com.haodf.android:id/et_search").send_keys("李胜文")
    #点击【搜索】
    driver.find_element_by_id("com.haodf.android:id/tv_cancel_or_search").click()
    time.sleep(10)
    #点击【图文问诊】按钮
    driver.find_element_by_id("com.haodf.android:id/tv_price_type1").click()
    time.sleep(3)
    driver.find_element_by_id("com.haodf.android:id/tv_service_name").click()
    time.sleep(2)
    driver.find_element_by_id("com.haodf.android:id/tvName").click()
    time.sleep(2)
    #选择图文问诊，点击【立即申请】
    driver.find_element_by_id("com.haodf.android:id/radioButton").click()
    driver.find_element_by_id("com.haodf.android:id/btnNextStep").click()
    time.sleep(10)
    #点击【符合】
    driver.find_element_by_id("com.haodf.android:id/btn_yes").click()
    time.sleep(3)
    #点击【接受】
    driver.find_element_by_id("com.haodf.android:id/tv_agree").click()
    time.sleep(2)
    #选择患者，点击【下一步】
    #fu_sun1 = '//*[@resource-id="com.haodf.android:id/patient_container"]/android.widget.LinearLayout[0]'
    #driver.find_element_by_xpath(fu_sun1).click()
    driver.find_element_by_android_uiautomator( 'new UiSelector().text("jisu")').click()
    #driver.find_element_by_id("com.haodf.android:id/add_new_patient").click()
    #print(driver.page_source())
    i=0
    while i < 20:
        try:
            # 尝试点击元素
            driver.find_element_by_id("com.haodf.android:id/btn_next").click()
            #time.sleep(1)
            break
        except Exception as e:
            swipeUp(1000)# 滑动屏幕
            #time.sleep(1)
            i = i + 1
    time.sleep(1)
    driver.find_element_by_id("com.haodf.android:id/btn1").click()
    time.sleep(1)
    driver.find_element_by_id("com.haodf.android:id/tv_disease").click()
    time.sleep(1)
    driver.find_element_by_id("com.haodf.android:id/btn_next").click()
    time.sleep(1)
    #选择没就诊
    driver.find_element_by_id("com.haodf.android:id/btn_no").click()
    #选择暂时没有
    driver.find_element_by_id("com.haodf.android:id/rb_not_have").click()
    #选择没有
    driver.find_element_by_id("com.haodf.android:id/rb_not_have").click()
    #点击【确认，下一步】
    driver.find_element_by_id("com.haodf.android:id/btn_next").click()
    # 点击【确认，下一步】
    driver.find_element_by_id("com.haodf.android:id/btn_next_step").click()
    #输入病情主诉
    driver.find_element_by_class_name("android.widget.EditText").clear()
    driver.find_element_by_class_name("android.widget.EditText").send_keys("12345678901234567890")
    time.sleep(1)
    swipeUp(1000)
    time.sleep(1)
    driver.find_element_by_id("com.haodf.android:id/btn_next_step").click()
    time.sleep(1)
    #需要医生提供的帮助
    # driver.find_element_by_class_name("android.widget.EditText").clear()
    # driver.find_element_by_class_name("android.widget.EditText").send_keys("12")
    whatHelp = '//*[@resource-id="com.haodf.android:id/edt_what_help"]/android.widget.LinearLayout/android.widget.EditText'
    driver.find_element_by_xpath(whatHelp).clear()
    driver.find_element_by_xpath(whatHelp).send_keys("12")
    time.sleep(1)
    #标题
    # driver.find_element_by_class_name("android.widget.EditText").clear()
    # driver.find_element_by_class_name("android.widget.EditText").send_keys("666")
    #title = '//*[@resource-id="com.haodf.android:id/edt_what_help"]/android.widget.LinearLayout[0]'
    driver.find_element_by_id("com.haodf.android:id/edt_title").clear()
    driver.find_element_by_id("com.haodf.android:id/edt_title").send_keys("66666")
    time.sleep(1)
    #点击【提交】
    driver.find_element_by_id("com.haodf.android:id/btn_submit").click()
    time.sleep(5)

    #点击【确认】
    driver.find_element_by_id("com.haodf.android:id/pay_btn").click()
    time.sleep(5)


if __name__ == '__main__':
    time.sleep(5)
    homePage()
    login()
    searchDoctor()

