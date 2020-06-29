def is_element_present(driver, how, what):  # 定义一个判断元素是否存在的函数，传3个参数
    apppresent = False
    try:  # 正常结果
        driver = self.driver.find_element(by='how', value='what')
        if driver.is_displayed():   #   如果元素出现
            apppresent = True
        else:
            apppresent = False
    except NoSuchElementExecption as e:    #  错误结果
        apppresent = False
    return apppresent
    assertTrue(apppresent, msg = "登陆失败")