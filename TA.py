from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

driver = webdriver.Edge()

username = input("请输入浙大统一身份认证用户名：")
password = input("请输入浙大统一身份认证密码：")

# 打开目标网页
driver.get('http://zdbk.zju.edu.cn/')
time.sleep(5)
button = driver.find_element(By.XPATH, '//*[@id="ssodl"]')
ActionChains(driver).move_to_element(button).click().perform()
time.sleep(5)
element = driver.find_element(By.ID, "username")
element.send_keys(username)
element = driver.find_element(By.ID, "password")
element.send_keys(password)
element = driver.find_element(By.ID, "rember")  # “记住我”
ActionChains(driver).move_to_element(element).click().perform()
element = driver.find_element(By.ID, "dl")
ActionChains(driver).move_to_element(element).click().perform()
time.sleep(5)
# 等待页面加载完成（根据需要调整等待时间）

# 通过 src 属性切换到 iframe
iframe = driver.find_element(By.XPATH, '//iframe[contains(@src, "index_initMenu.html")]')  # 通过 src 属性定位 iframe
driver.switch_to.frame(iframe)  # 切换到该 iframe

div_element = driver.find_element(By.ID, 'tab_zjpjpf_btns')
buttons = div_element.find_elements(By.TAG_NAME, 'button')

for button in buttons: # 遍历所有TA
    
    button.click()
    
    slider = driver.find_element(By.CLASS_NAME, 'slider-container')
    # 获取滑动条上需要拖动的指针（即 high pointer）
    pointer = driver.find_element(By.CLASS_NAME, 'pointer.high')
    # 通过 ActionChains 来模拟鼠标拖动
    action = ActionChains(driver)
    # 拖动滑动条，调整为目标值。此处的 500 是示例值，可能需要根据页面实际调整。
    inner_width = driver.execute_script("return window.innerWidth")
    max_offset = inner_width - pointer.location["x"]
    action.click_and_hold(pointer).move_by_offset(max_offset - 10, 0).release().perform()

    # 示例：选择“是”作为“是否推荐为优秀助教”
    yes_button = driver.find_element(By.XPATH, '//*[@id="zjpjpfAjaxForm"]/div/div[2]/div[2]/div/label[1]/input')
    if not yes_button.is_selected():
        yes_button.click()

    # 助教品行端正、公平诚信，不发表或转发不良观点及信息
    yes_button = driver.find_element(By.XPATH, '//input[@name="zbnr_3" and @value="是"]')
    if not yes_button.is_selected():
        yes_button.click()

    # 选择复选框 "随堂听课"
    attend_class_checkbox = driver.find_element(By.XPATH, '//input[@name="zbnr_4" and @value="随堂听课"]')
    if not attend_class_checkbox.is_selected():
        attend_class_checkbox.click()

    # 选择复选框 "组织讨论课或习题课"
    discussion_class_checkbox = driver.find_element(By.XPATH, '//input[@name="zbnr_4" and @value="组织讨论课或习题课"]')
    if not discussion_class_checkbox.is_selected():
        discussion_class_checkbox.click()

    # 选择复选框 "课堂管理或指导"
    management_checkbox = driver.find_element(By.XPATH, '//input[@name="zbnr_4" and @value="课堂管理或指导"]')
    if not management_checkbox.is_selected():
        management_checkbox.click()

    # 选择复选框 "课外辅导与答疑"
    tutoring_checkbox = driver.find_element(By.XPATH, '//input[@name="zbnr_4" and @value="课外辅导与答疑"]')
    if not tutoring_checkbox.is_selected():
        tutoring_checkbox.click()

    # 选择复选框 "批改作业或实验报告"
    grading_checkbox = driver.find_element(By.XPATH, '//input[@name="zbnr_4" and @value="批改作业或实验报告"]')
    if not grading_checkbox.is_selected():
        grading_checkbox.click()

    # 选择复选框 "参与教学（含实验）准备与考核"
    preparation_checkbox = driver.find_element(By.XPATH, '//input[@name="zbnr_4" and @value="参与教学（含实验）准备与考核"]')
    if not preparation_checkbox.is_selected():
        preparation_checkbox.click()

    # 保存
    save_button = driver.find_element(By.ID, 'btn_bc')
    save_button.click()

    btn_ok = driver.find_element(By.ID, 'btn_ok')
    btn_ok.click()

# 提交表单
submit_button = driver.find_element(By.ID, 'btn_tj')
submit_button.click()

os.system("pause")  # 暂停程序，等待手动提交