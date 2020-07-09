def is_element_present(driver, how, what):  # 定义一个判断元素是否存在的函数，传3个参数

    print('start is_element_present ===>>>>')

    apppresent = False
    try:  # 正常结果
        driver = driver.find_element(by = how, value = what)
        if driver.is_displayed():   #   如果元素出现
            apppresent = True
            print("找到当前元素")
    except NoSuchElementException as e:    #  错误结果
        apppresent = False
        print(e)

    print('end is_element_present ===>>>>')
    return apppresent

