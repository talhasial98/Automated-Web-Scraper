#!/usr/bin/env python
# coding: utf-8

# In[4]:


error_ajk=[]
error_bal=[]
error_isb=[]
error_kpk=[]
error_pun=[]
error_sin=[]
import urllib.request
import tkinter
import threading
from tkinter import *
from tkinter import ttk
import time
import winsound
from tkinter.filedialog import asksaveasfile
import pandas as pd
#import xlsxwriter
event=threading.Event()
event2=threading.Event()
event3=threading.Event()
event4=threading.Event()
event5=threading.Event()
eventbal=threading.Event()
event2bal=threading.Event()
event3bal=threading.Event()
event4bal=threading.Event()
event5bal=threading.Event()
eventisb=threading.Event()
event2isb=threading.Event()
event3isb=threading.Event()
event4isb=threading.Event()
event5isb=threading.Event()
eventkpk=threading.Event()
event2kpk=threading.Event()
event3kpk=threading.Event()
event4kpk=threading.Event()
event5kpk=threading.Event()
eventpun=threading.Event()
event2pun=threading.Event()
event3pun=threading.Event()
event4pun=threading.Event()
event5pun=threading.Event()
eventsin=threading.Event()
event2sin=threading.Event()
event3sin=threading.Event()
event4sin=threading.Event()
event5sin=threading.Event()
def isb_ms():
    import requests
    import lxml.html as lh
    import pandas as pd
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    try:
        driver.get('https://www.au.edu.pk/Pages/Admission/eligibility_criteria.aspx')
        air=[]
        driver.find_element_by_xpath("/html/body/form/div[3]/div/div[2]/div/div/div[2]/div[1]/h4/a").click()
        name=driver.find_elements_by_xpath("/html/body/form/div[3]/div/div[2]/div/div/div[2]/div[2]/ul/li/span/a")
        for a in name:
            if (a.text.startswith('M')):
                air.append(a.text)
        driver.find_element_by_xpath("/html/body/form/div[3]/div/div[2]/div/div/div[3]/div[1]/h4/a").click()
        name=driver.find_elements_by_xpath("/html/body/form/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li/span/a")
        for a in name:
            if (a.text.startswith('M')):
                air.append(a.text)
        air_uni=pd.DataFrame(air,columns=["Air University"])
    except:
            error_isb.append("Air University")
            air_uni=pd.DataFrame(columns=["Air University"])
    try:
        driver.get('https://www.aiou.edu.pk/ProgrammesList.asp?P=MPHIL%20/%20MS')
        iqbal=[]
        courses=driver.find_elements_by_xpath("/html/body/div[2]/div[4]/div[1]/table/tbody/tr/td")
        for z in courses:
            iqbal.append(z.text)
        driver.get('https://www.aiou.edu.pk/ProgrammesList.asp?P=MASTER')
        courses=driver.find_elements_by_xpath("/html/body/div[2]/div[4]/div[1]/table/tbody/tr/td")
        for z in courses:
            iqbal.append(z.text)
        iqbal_uni=pd.DataFrame(iqbal,columns=["Allama Iqbal Open University"])
    except:
        error_isb.append("Allama Iqbal Open University")
        iqbal_uni=pd.DataFrame(columns=["Allama Iqbal Open University"])
    try:
        def func():
            bahria=[]
            courses=driver.find_elements_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/table/tbody/tr/td[1]/a")
            for z in courses:
                bahria.append(z.text)
            courses=driver.find_elements_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[1]/a")
            for z in courses:
                bahria.append(z.text)
        driver.get('https://www.bahria.edu.pk/academics/graduate-programs/')
        func()
        bahria_uni=pd.DataFrame(bahria,columns=["Bahria University"])
    except:
        error_isb.append("Bahria University")
        bahria_uni=pd.DataFrame(columns=["Bahria University"])
    try:
        driver.get('https://www.comsats.edu.pk/Offices/graduate_programs.aspx')
        comsats=[]
        for z in range(1,41):
            coursesm1=driver.find_element_by_xpath("/html/body/form/div[10]/div/div/div/div/table[1]/tbody/tr["+str(z)+"]/td[1]/p").text
            comsats.append('Master in',coursesm1)
        comsats_uni=pd.DataFrame(comsats,columns=["COMSATS Institute of Information Technology"])
    except:
        error_isb.append("COMSATS Institute of Information Technology")
        comsats_uni=pd.DataFrame(columns=["COMSATS Institute of Information Technology"])
    try:
        driver.get('https://cust.edu.pk/')
        cap=[]
        driver.find_element_by_xpath("/html/body/div[4]/div/div").click()
        from selenium.webdriver.common.action_chains import ActionChains
        a = ActionChains(driver)
        m = driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div/div/div/nav/ul/nav/ul/li[3]/a/span")
        n = driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div/div/div/nav/ul/nav/ul/li[3]/ul/li[8]/a/span")
        a.move_to_element(m).perform()
        a.move_to_element(n).perform()
        course=driver.find_elements_by_xpath("/html/body/div[1]/div/header/div/div/div/div/nav/ul/nav/ul/li[3]/ul/li[8]/ul/li/a/span")
        for z in course:
            if(z.text.startswith('M')):
                cap.append(z.text)
        a = ActionChains(driver)
        m = driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div/div/div/nav/ul/nav/ul/li[3]/a/span")
        n = driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div/div/div/nav/ul/nav/ul/li[3]/ul/li[9]/a/span")
        a.move_to_element(m).perform()
        a.move_to_element(n).perform()
        course=driver.find_elements_by_xpath("/html/body/div[1]/div/header/div/div/div/div/nav/ul/nav/ul/li[3]/ul/li[9]/ul/li/a/span")
        for z in course:
            if(z.text.startswith('M')):
                cap.append(z.text)
        cap_uni=pd.DataFrame(cap,columns=[" Capital University of Science & Technology"])
    except:
        error_isb.append(" Capital University of Science & Technology")
        cap_uni=pd.DataFrame(columns=[" Capital University of Science & Technology"])
    try:
        driver.get('https://www.eduvision.edu.pk/federal-urdu-university-of-arts-science-technology-fuuast-islamabad-ins-3149')
        fed=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            fed.append(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            fed.append(a.text)
        fed_uni=pd.DataFrame(fed,columns=["Federal Urdu University of Arts, Sciences & Technology"])
    except:
        error_isb.append("Federal Urdu University of Arts, Sciences & Technology")
        fed_uni=pd.DataFrame(columns=["Federal Urdu University of Arts, Sciences & Technology"])
    try:
        driver.get('https://fui.edu.pk/admissions/Eligibility-Criteria.php')
        found=[]
        name=driver.find_elements_by_xpath("/html/body/main/div/div/article/div[2]/div/table/tbody/tr/td[1]")
        for a in name:
            if(a.text.startswith('M')):
                found.append(a.text)
        found_uni=pd.DataFrame(found,columns=["Foundation University, Islamabad"])
    except:
        error_isb.append("Foundation University, Islamabad")
        found_uni=pd.DataFrame(columns=["Foundation University, Islamabad"])
    try:
        driver.get('http://www.hsa.edu.pk/?page_id=627')
        hsa=[]
        course=driver.find_elements_by_xpath("/html/body/div/div[4]/div[1]/div/div[2]/table[1]/tbody/tr/td[1]/a")
        for z in course:
            hsa.append(z.text)
        hsa_uni=pd.DataFrame(hsa,columns=["Health Services Academy"])
    except:
        error_isb.append("Health Services Academy")
        hsa_uni=pd.DataFrame(columns=["Health Services Academy"])
    try:
        driver.get('https://www.ist.edu.pk/academics-degrees-programs-graduate-ms')
        ist=[]
        time.sleep(3)
        unilist=driver.find_elements_by_xpath("/html/body/div[1]/form/div[3]/div[4]/div/div/div[2]/div[1]/div/div/div/a/h5")
        for a in unilist:
            ist.append(a.text)
        ist_uni=pd.DataFrame(ist,columns=["Institute of Space Technology"])
    except:
        error_isb.append("Institute of Space Technology")
        ist_uni=pd.DataFrame(columns=["Institute of Space Technology"])
    try:
        driver.get('https://admission.iiu.edu.pk/programes')
        iiu=[]
        unilist=driver.find_elements_by_xpath("/html/body/div[4]/div[1]/div/div/div/i")
        for a in unilist:
            if(a.text.startswith('M')):
                iiu.append(a.text)
        iiu_uni=pd.DataFrame(iiu,columns=["International Islamic University"])
    except:
        error_isb.append("International Islamic University")
        iiu_uni=pd.DataFrame(columns=["International Islamic University"])
    try:
        driver.get('https://myu.edu.pk/admission-criteria')
        my=[]
        courses=driver.find_elements_by_xpath("/html/body/div[2]/div/div[2]/h3")
        for z in range(3,5):
            my.append(courses[z].text)
        my_uni=pd.DataFrame(my,columns=["Muslim Youth University"])
    except:
        error_isb.append("Muslim Youth University")
        my_uni=pd.DataFrame(columns=["Muslim Youth University"])
    try:
        driver.get('https://ndu.edu.pk/fcs/fcs_admission.php')
        ndu=[]
        courses=driver.find_elements_by_xpath("/html/body/center/div[3]/div/div[1]/div[4]/table/tbody/tr/td[3]/p")
        for z in courses:
            ndu.append(z.text)
        ndu_uni=pd.DataFrame(ndu,columns=["National Defense University"])
    except:
        error_isb.append("National Defense University")
        ndu_uni=pd.DataFrame(columns=["National Defense University"])
    try:
        driver.get('https://www.nu.edu.pk/Degree-Programs')
        nuces=[]
        time.sleep(5)
        for r in range(15,29):
            try:
                value=driver.find_element_by_xpath("//*[@id='page-wrapper']/div/div/div[2]/div/div/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a").text
                nuces.append(value) 
            except NoSuchElementException:
                pass
        nuces_uni=pd.DataFrame(nuces,columns=["National University of Computer & Emerging Sciences"])
    except:
        error_isb.append("National University of Computer & Emerging Sciences")
        nuces_uni=pd.DataFrame(columns=["National University of Computer & Emerging Sciences"])
    try:
        driver.get('https://numspak.edu.pk/acad/postgraduate')
        nums=[]
        time.sleep(5)
        for r in range(6,76):
            try:
                value=driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/ul/li["+str(r)+"]/a").text
                nums.append(value) 
            except NoSuchElementException:
                pass
        nums_uni=pd.DataFrame(nums,columns=["National University of Medical Sciences"])
    except:
        error_isb.append("National University of Medical Sciences")
        nums_uni=pd.DataFrame(columns=["National University of Medical Sciences"])
    try:
        driver.get('https://www.numl.edu.pk/programs/graduate')
        time.sleep(5)
        button=driver.find_element_by_xpath("//*[@id='headingOne1']/a/h5")
        button.click()
        time.sleep(1)
        numl=[]
        for c in range(1,36):
            try:
                for r in range(1,20):
                    try:
                        value=driver.find_element_by_xpath("//*[@id='collapseOne_0']/div/ul["+str(c)+"]/ul/li["+str(r)+"]/a/span").text
                        numl.append(value) 
                    except NoSuchElementException:
                        pass
            except NoSuchElementException:
                pass
        numl_uni=pd.DataFrame(numl,columns=["National University of Modern Languages"])
    except:
        error_isb.append("National University of Modern Languages")
        numl_uni=pd.DataFrame(columns=["National University of Modern Languages"])
    try:
        driver.get('https://nust.edu.pk/academic/mastersprogrammes/')
        nust=[]
        time.sleep(5)
        for q in range(1,4):
            for c in range(1,28):
                try:
                    for r in range(1,30):
                        try:
                            value= driver.find_element_by_xpath("//*[@id='primary']/div/div/div[1]/div["+str(q)+"]/div["+str(c)+"]/div/div[2]/ul/li["+str(r)+"]/a").text
                            nust.append(value)                         
                        except NoSuchElementException:
                            pass
                except NoSuchElementException:
                    pass
        nust_uni=pd.DataFrame(nust,columns=["National University of Sciences & Technology"])
    except:
        error_isb.append("National University of Sciences & Technology")
        nust_uni=pd.DataFrame(columns=["National University of Sciences & Technology"])
    try:
        driver.get('http://admissions.pieas.edu.pk/Admissions/MS.html')
        pieas=[]
        time.sleep(5)
        for c in range(1,15):
            try:
                for r in range(1,3):
                    try:
                        value= driver.find_element_by_xpath("//*[@id='blog-full-width']/div/div/div[2]/article/div/table/tbody/tr["+str(c)+"]/td["+str(r)+"]").text
                        pieas.append(value)                  
                    except NoSuchElementException:
                        pass
            except NoSuchElementException:
                pass
        pieas_uni=pd.DataFrame(pieas,columns=["Pakistan Institute of Engineering & Applied Sciences"])
    except:
        error_isb.append("Pakistan Institute of Engineering & Applied Sciences")
        pieas_uni=pd.DataFrame(columns=["Pakistan Institute of Engineering & Applied Sciences"])
    try:
        driver.get('https://qau.edu.pk/faculty-of-social-sciences-2/')
        qau=[]
        time.sleep(5)
        action = ActionChains(driver);
        for c in range(2,8):
            try:
                parent_level_menu = driver.find_element_by_xpath("//*[@id='menu-item-Postgraduate ']/a")
                action.move_to_element(parent_level_menu).perform()
                parent_level_menu = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[4]/ul/li["+str(c)+"]/a")
                action.move_to_element(parent_level_menu).perform()
                for r in range(1,18):
                    try:
                        value=driver.find_element_by_xpath("//html/body/div[3]/div/div[3]/ul/li[4]/ul/li["+str(c)+"]/ul/li["+str(r)+"]/a/span").text
                        qau.append(value)                
                    except NoSuchElementException:
                        pass
            except NoSuchElementException:
                pass
        qau_uni=pd.DataFrame(qau,columns=["Quaid-i-Azam University"])
    except:
        error_isb.append("Quaid-i-Azam University")
        qau_uni=pd.DataFrame(columns=["Quaid-i-Azam University"])
    try:
        driver.get('https://www.riphah.edu.pk/all-post-graduate-programs/')
        rip=[]
        time.sleep(5)
        for r in range(2,70):
            try:
                value=driver.find_element_by_xpath("//*[@id='kingster-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div/article/div/div/div/table/tbody/tr["+str(r)+"]").text
                rip.append(value) 
            except NoSuchElementException:
                pass
        rip_uni=pd.DataFrame(rip,columns=["Ripha International"])
    except:
        error_isb.append("Ripha International")
        rip_uni=pd.DataFrame(columns=["Ripha International"])
    try:
        driver.get('http://www.szabmu.edu.pk/admission/postgraduate-admission')
        szabmu=[]
        time.sleep(5)
        for q in range(1,6,2):
            for c in range(1,20):
                try:
                    for r in range(2,5,2):
                        try:
                            value= driver.find_element_by_xpath("//*[@id='maincontent']/div/div/div/div[2]/div/div/div["+str(q)+"]/table/tbody/tr["+str(c)+"]/td["+str(r)+"]").text
                            szabmu.append(value)                  
                        except NoSuchElementException:
                            pass
                except NoSuchElementException:
                    pass
        szabmu_uni=pd.DataFrame(szabmu,columns=["Shaheed Zulfiqar Ali Bhutto Medical University"])
    except:
        error_isb.append("Shaheed Zulfiqar Ali Bhutto Medical University")
        szabmu_uni=pd.DataFrame(columns=["Shaheed Zulfiqar Ali Bhutto Medical University"])
    try:
        driver.get('https://stmu.edu.pk/admissions/eligibility-criteria/')
        action = ActionChains(driver);
        stmu=[]
        time.sleep(5)
        parent_level_menu = driver.find_element_by_xpath("//*[@id='menu-item-512']/a/span")
        action.move_to_element(parent_level_menu).perform()
        parent_level_menu = driver.find_element_by_xpath("//*[@id='menu-item-521']/a")
        action.move_to_element(parent_level_menu).perform()
        parent_level_menu = driver.find_element_by_xpath("//*[@id='menu-item-523']/a")
        action.move_to_element(parent_level_menu).perform()
        for r in range(1,15):
            try:
                value=driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[3]/div[2]/div/nav/ul/li[3]/ul/li[5]/ul/li[2]/ul/li["+str(r)+"]/a").text
                stmu.append(value) 
            except NoSuchElementException:
                pass
        stmu_uni=pd.DataFrame(stmu,columns=["Shifa Tameer-e-Millat University"])
    except:
        error_isb.append("Shifa Tameer-e-Millat University")
        stmu_uni=pd.DataFrame(columns=["Shifa Tameer-e-Millat University"])
    try:
        driver.get('https://www.case.edu.pk/graduate.aspx')
        case=[]
        time.sleep(5)
        for r in range(1,66):
            try:
                value=driver.find_element_by_xpath("//*[@id='aspnetForm']/div[3]/div[2]/div/div/div/div["+str(r)+"]/a/span").text
                case.append(value) 
            except NoSuchElementException:
                pass
        case_uni=pd.DataFrame(case,columns=["Sir Syed (CASE) Institute of Technology, Islamabad"])
    except:
        error_isb.append("Sir Syed (CASE) Institute of Technology, Islamabad")
        case_uni=pd.DataFrame(case,columns=["Sir Syed (CASE) Institute of Technology, Islamabad"])
    global pdList_isb
    global isb_df
    pdList_isb=[air_uni,iqbal_uni,bahria_uni,comsats_uni,cap_uni,
            fed_uni,found_uni,hsa_uni,iiu_uni,my_uni,ndu_uni,
            nuces_uni,nums_uni,numl_uni,nust_uni,pieas_uni,
            qau_uni,rip_uni,szabmu_uni,stmu_uni,case_uni]
    isb_df=pd.concat(pdList_isb, axis=1)
    print(isb_df)
    eventisb.set()
    event2isb.set()
    event3isb.set()
    event4isb.set()
    event5isb.set()
def bal_ms():
    import requests
    import lxml.html as lh
    import pandas as pd
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    try:
        driver.get('http://www.aiu.edu.pk/site/2021/01/04/admission/')
        driver.find_element_by_xpath("/html/body/div[1]/header/div/div[3]/nav/div/div/ul/li[3]/a")
        hamd=[]
        from selenium.webdriver.common.action_chains import ActionChains
        a = ActionChains(driver)
        m = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[3]/nav/div/div/ul/li[3]/a")
        a.move_to_element(m).perform()
        n = driver.find_elements_by_xpath("/html/body/div[1]/header/div/div[3]/nav/div/div/ul/li[3]/ul/li/a")
        for j in range(1,len(n)+1):
            b = ActionChains(driver)
            k = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[3]/nav/div/div/ul/li[3]/ul/li["+str(j)+"]/a")
            b.move_to_element(k).perform()
            courses=driver.find_elements_by_xpath("/html/body/div[1]/header/div/div[3]/nav/div/div/ul/li[3]/ul/li["+str(j)+"]/ul/li/a")
            for z in courses:
                if (z.text.startswith('M')):
                    hamd.append(z.text)
        hamd_uni=pd.DataFrame(hamd,columns=["Al-Hamd Islamic University"])
    except:
        error_bal.append("Al-Hamd Islamic University")
        hamd_uni=pd.DataFrame(columns=["Al-Hamd Islamic University"])
    try:
        driver.get('http://www.buetk.edu.pk/')
        buet=[]
        from selenium.webdriver.common.action_chains import ActionChains
        a = ActionChains(driver)
        m = driver.find_element_by_xpath("/html/body/div[3]/div/header/div[2]/div/div[2]/div[1]/ul/li[3]/a")
        a.move_to_element(m).perform()
        courses=driver.find_elements_by_xpath("/html/body/div[3]/div/header/div[2]/div/div[2]/div[1]/ul/li[3]/div/div/div[3]/div/ul/li/a")
        for z in courses:
            buet(z.text)
        buet_uni=pd.DataFrame(buet,columns=["Balochistan University of Engineering & Technology"])
    except:
        error_bal.append("Balochistan University of Engineering & Technology")
        buet_uni=pd.DataFrame(columns=["Balochistan University of Engineering & Technology"])
    try:
        driver.get('http://www.buitms.edu.pk/Programs/#Graduate')
        buit=[]
        courses=driver.find_elements_by_xpath("/html/body/form/section[4]/div/div/div/div/div[2]/div/a/span")
        for z in courses:
            if (z.text.startswith('MS ')):
                buit(z.text)
        buit_uni=pd.DataFrame(buit,columns=["Balochistan University of Information Technology, Engineering & Management Sciences"])
    except:
        buit_uni=pd.DataFrame(columns=["Balochistan University of Information Technology, Engineering & Management Sciences"])
        error_bal.append("Balochistan University of Information Technology, Engineering & Management Sciences")
    try:
        driver.get('https://www.luawms.edu.pk/postgraduate/')
        las=[]
        course=driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/article/div/div/div[2]/div/div/div/div/h4")
        for z in range(0,8):
            las.append(course[z].text)
        las_uni=pd.DataFrame(las,columns=["Lasbela University of Agriculture, Water & Marine Sciences"])
    except:
        error_bal.append("Lasbela University of Agriculture, Water & Marine Sciences")
        las_uni=pd.DataFrame(columns=["Lasbela University of Agriculture, Water & Marine Sciences"])
    try:
        driver.get('https://sbkwu.edu.pk/department-of-economics/')
        action = ActionChains(driver);
        sar=[]
        time.sleep(5)
        parent_level_menu = driver.find_element_by_xpath("//*[@id='menu-item-25']/a")
        action.move_to_element(parent_level_menu).perform()
        for r in range(1,15):
            try:
                value=driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[2]/div/ul/li[2]/ul/li["+str(r)+"]/a").text
                sar.append(value) 
            except NoSuchElementException:
                pass
        sar_uni=pd.DataFrame(sar,columns=["Sardar Bahadur Women Uni"])
    except:
        error_bal.append("Sardar Bahadur Women Uni")
        sar_uni=pd.DataFrame(columns=["Sardar Bahadur Women Uni"])
    try:
        driver.get('https://www.eduvision.edu.pk/university-of-balochistan-uob-quetta-ins-37')
        uob=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]')
        button.click()
        for r in range(1,40):
            try:
                value=driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                uob.append(value)                     
            except NoSuchElementException:
                pass
        uob_uni=pd.DataFrame(uob,columns=["University of Balochistan"])
    except:
        error_bal.append("University of Balochistan")
        uob_uni=pd.DataFrame(columns=["University of Balochistan"])
    try:
        driver.get('https://uot.edu.pk/admissions/find-programs?degree=graduate')
        uot=[]
        time.sleep(5)
        for page in range(1,15):
            try:
                value=driver.find_element_by_xpath("/html/body/main/div/div/div/section/div["+str(page)+"]/div/div/a/div").text
                uot.append(value)                  
            except NoSuchElementException:
                pass 
        uot_uni=pd.DataFrame(uot,columns=["University of Turbat"])
    except:
        error_bal.append("University of Turbat")
        uot_uni=pd.DataFrame(columns=["University of Turbat"])
    global bal_df
    global pdList_bal
    pdList_bal=[hamd_uni,buet_uni,buit_uni,las_uni,sar_uni,uob_uni,uot_uni]
    bal_df=pd.concat(pdList_bal, axis=1)
    print(bal_df)
    eventbal.set()
    event2bal.set()
    event3bal.set()
    event4bal.set()
    event5bal.set()
def ajk_gb_ms():
    import requests
    import lxml.html as lh
    import pandas as pd
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    try:
        driver.get('https://admissions.kiu.edu.pk/all-degrees?program=2')
        kar=[]
        name=driver.find_elements_by_xpath("/html/body/div/div/div/div/div[1]/section/ol/li")
        for a in name:
            if (a.text.startswith('M')):
                kar.append(a.text)
        kar_uni=pd.DataFrame(kar,columns=["Karakurum International University"])
    except:
        error_ajk.append("Karakurum International University")
        kar_uni=pd.DataFrame(columns=["Karakurum International University"])
    try:
        driver.get('https://www.eduvision.edu.pk/mirpur-university-of-science-and-technology-must-mir-pur-ajk-ins-1311594007')
        mir=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            mir.append(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            mir.append(a.text)
        mir_uni=pd.DataFrame(mir,columns=["Mirpur University of Science & Technology"])
    except:
        error_ajk.append("Mirpur University of Science & Technology")
        mir_uni=pd.DataFrame(columns=["Mirpur University of Science & Technology"])
    try:
        driver.get('https://www.eduvision.edu.pk/mohi-ud-din-islamic-university-miu-mir-pur-ajk-ins-62')
        moh=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            moh.append(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            moh.append(a.text)
        moh_uni=pd.DataFrame(moh,columns=["Mohi-ud-Din Islamic University"])
    except:
        error_ajk.append("Mohi-ud-Din Islamic University")
        moh_uni=pd.DataFrame(columns=["Mohi-ud-Din Islamic University"])
    try:
        driver.get('https://www.eduvision.edu.pk/university-of-azad-jammu-kashmir-uajk-muzaffarabad-ins-36')
        uoajk=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]')
        button.click()
        for r in range(1,20):
            try:
                value=driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                uoajk.append(value)                    
            except NoSuchElementException:
                pass
        uoajk_uni=pd.DataFrame(uoajk,columns=["University of Azad Kashmir"])
    except:
        error_ajk.append("University of Azad Kashmir")
        oajk_uni=pd.DataFrame(columns=["University of Azad Kashmir"])
    try:
        driver.get('https://uobs.edu.pk/index.php/admissions/fee-structure')
        time.sleep(5)
        uobs=[]
        for r in range(14,25):
            try:
                value=driver.find_element_by_xpath("//*[@id='t3-content']/div[2]/article/section/table/tbody/tr["+str(r)+"]/td[2]/span").text   
                uobs.append(value)
            except NoSuchElementException:
                pass
        uobs_uni=pd.DataFrame(uobs,columns=["University of Baltistan"])
    except:
        error_ajk.append("University of Baltistan")
        uobs_uni=pd.DataFrame(columns=["University of Baltistan"])
    try:
        driver.get('http://www.uokajk.edu.pk/home/page/admission')
        kot=[]
        time.sleep(5)
        for r in range(2,4):
            for c in range(1,25):
                try:
                    value=driver.find_element_by_xpath("//*[@id='nestable']/ol/li["+str(r)+"]/ol/li["+str(c)+"]").text
                    kot.append(value)
                except NoSuchElementException:
                    pass  
        kot_uni=pd.DataFrame(kot,columns=["University of Kotli, Azad Jammu and Kashmir"])
    except:
        error_ajk.append("University of Kotli, Azad Jammu and Kashmir")
        kot_uni=pd.DataFrame(columns=["University of Kotli, Azad Jammu and Kashmir"])
    try:
        driver.get('https://www.eduvision.edu.pk/unversity-of-the-poonch-rawala-kot-upr-rawala-kot-ins-1348331999')
        poo=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]')
        button.click()
        for r in range(1,60):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                poo.append(value)                   
            except NoSuchElementException:
                pass
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]')
        button.click()
        for r in range(1,60):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                poo.append(value)                   
            except NoSuchElementException:
                pass
        poo_uni=pd.DataFrame(poo,columns=["University of the Poonch, Rawalakot"])
    except:
        error_ajk.append("University of the Poonch, Rawalakot")
        poo_uni=pd.DataFrame(columns=["University of the Poonch, Rawalakot"])
    try:
        driver.get('https://wuajk.edu.pk/programs-offered')
        wuajk=[]
        time.sleep(5)
        for c in range(2,4):
            for r in range(1,15):
                try:
                    value=driver.find_element_by_xpath("//*[@id='page-container']/div[2]/div/div[1]/ul["+str(c)+"]/li["+str(r)+"]").text
                    wuajk.append(value)
                except NoSuchElementException:
                    pass  
        wuajk_uni=pd.DataFrame(wuajk,columns=["Women University of Azad Jammu & Kashmir"])
    except:
        error_ajk.append("Women University of Azad Jammu & Kashmir")
        wuajk_uni=pd.DataFrame(columns=["Women University of Azad Jammu & Kashmir"])
    global pdList_ajk
    global ajk_df
    pdList_ajk=[kar_uni,mir_uni,moh_uni,uoajk_uni,uobs_uni,kot_uni,poo_uni,wuajk_uni]
    ajk_df=pd.concat(pdList_ajk, axis=1)
    print(ajk_df)
    event.set()
    event2.set()
    event3.set()
    event4.set()
    event5.set()
def kpk_ms():
    import requests
    import lxml.html as lh
    import pandas as pd
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.keys import Keys
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    try:
        driver.get('http://peshawar.abasyn.edu.pk/Home/Graduate')
        aba=[]
        name=driver.find_elements_by_xpath("/html/body/div[2]/section[1]/div/div/div/ul/li/a")
        for a in name:
            aba.append(a.text)
        aba_uni=pd.DataFrame(aba,columns=["Abasyn University"])
    except:
        error_kpk.append("Abasyn University")
        aba_uni=pd.DataFrame(columns=["Abasyn University"])
    try:
        driver.get('https://aust.edu.pk/')
        abott=[]
        arr=[]
        from selenium.webdriver.common.action_chains import ActionChains
        a = ActionChains(driver)
        m = driver.find_element_by_xpath("/html/body/div[2]/div[2]/header/ul/li[4]/a/span/span")
        a.move_to_element(m).perform()
        n = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/header/ul/li[4]/ul/li/a/span/span")
        for j in range(1,len(n)+1):
            b = ActionChains(driver)
            k = driver.find_element_by_xpath("/html/body/div[2]/div[2]/header/ul/li[4]/ul/li["+str(j)+"]/a")
            b.move_to_element(k).perform()
            courses=driver.find_elements_by_xpath("/html/body/div[2]/div[2]/header/ul/li[4]/ul/li["+str(j)+"]/ul/li/a")
            for z in courses:
                arr.append(z.get_attribute('href'))
        for h in arr:
            driver.get(h)
            time.sleep(2)
            coursesname=driver.find_elements_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div/div/div/div/section[3]/div/div/div[1]/div/div/section/div/div/div/div/div/div[2]/div/div/table/tbody/tr/td[2]/ul/li/span")
            for m in coursesname:
                if (m.text.startswith('M')):
                    abott.append(m.text)
        abott_uni=pd.DataFrame(abott,columns=["Abbottabad University of Science and Technology"])
    except:
        error_kpk.append("Abbottabad University of Science and Technology")
        abott_uni=pd.DataFrame(columns=["Abbottabad University of Science and Technology"])
    try:
        driver.get('https://awkum.edu.pk/admissions/program-details/')
        awku=[]
        driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/div/div/div/div[2]/h3/a").click()
        name=driver.find_elements_by_xpath("/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div/table/tbody/tr/td[2]/span/strong[1]")
        for a in name:
            awku.append(a.text) 
        awku_uni=pd.DataFrame(awku,columns=["Abdul Wali Khan University"])
    except:
        error_kpk.append("Abdul Wali Khan University")
        awku_uni=pd.DataFrame(columns=["Abdul Wali Khan University"])
    try:
        driver.get('https://www.eduvision.edu.pk/bacha-khan-university-bku-charsadda-ins-1348767933')
        bacha=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            bacha.append(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            bacha.append(a.text)
        bacha_uni=pd.DataFrame(bacha,columns=["Bacha Khan University"])
    except:
        error_kpk.append("Bacha Khan University")
        bacha_uni=pd.DataFrame(columns=["Bacha Khan University"])
    try:
        driver.get('https://www.eduvision.edu.pk/cecos-university-of-information-tech-emerging-sciences-cecos-peshawar-ins-48')
        cecos=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            cecos.append(a.text)
        cecos_uni=pd.DataFrame(cecos,columns=["CECOS University of Information Technology & Emerging Sciences"]) 
    except:
        error_kpk.append("CECOS University of Information Technology & Emerging Sciences")
        cecos_uni=pd.DataFrame(columns=["CECOS University of Information Technology & Emerging Sciences"]) 
    try:
        driver.get('http://www.cityuniversity.edu.pk/cusitnew/index.php')
        city=[]
        arr=[]
        from selenium.webdriver.common.action_chains import ActionChains
        a = ActionChains(driver)
        m = driver.find_element_by_xpath("/html/body/div[1]/nav/div/div[2]/ul/li[4]/a")
        a.move_to_element(m).perform()
        for b in driver.find_elements_by_xpath("/html/body/div[1]/nav/div/div[2]/ul/li[4]/ul/li/a"):
            arr.append(b.get_attribute('href'))
        p=[]
        for a in arr:
            driver.get(a)
            driver.execute_script("window.scrollTo(0, 1400)")
            time.sleep(3)
            course=driver.find_elements_by_xpath("/html/body/div/div/div/div/div/h4")
            for z in course:
                city.append(z.text)
        for n in p:
            if (n.startswith('M')):
                city.append(n)
        city_uni=pd.DataFrame(city,columns=["City University of Science and Information Technology"])
    except:
        error_kpk.append("City University of Science and Information Technology")
        city_uni=pd.DataFrame(columns=["City University of Science and Information Technology"])
    try:
        driver.get('https://www.eduvision.edu.pk/gandhara-university-gu-peshawar-ins-3227')
        gand=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            gand(a.text)
        gand_uni=pd.DataFrame(gand,columns=["Gandhara University"])  
    except:
        error_kpk.append("Gandhara University")
        gand_uni=pd.DataFrame(columns=["Gandhara University"])
    try:
        driver.get('https://www.giki.edu.pk/Admissions/Graduate/Overview')
        giki=[]
        coursesname=driver.find_elements_by_xpath("/html/body/div[3]/div[2]/div[1]/div[2]/div/ul[1]/li")
        for m in coursesname:
            giki.append('MS',m.text)
        giki_uni=pd.DataFrame(giki,columns=["Ghulam Ishaq Khan Institute of Engineering Sciences & Technology"])
    except:
        error_kpk.append("Ghulam Ishaq Khan Institute of Engineering Sciences & Technology")
        giki_uni=pd.DataFrame(columns=["Ghulam Ishaq Khan Institute of Engineering Sciences & Technology"])
    try:
        driver.get('https://www.eduvision.edu.pk/gomal-university-gu-di-khan-ins-11')
        gom=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            gom.append(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            gom.append(a.text)
        gom_uni=pd.DataFrame(gom,columns=["Gomal University"]) 
    except:
        error_kpk.append("Gomal University")
        gom_uni=pd.DataFrame(columns=["Gomal University"]) 
    try:
        driver.get('http://www.hu.edu.pk/programs/02%20Years')
        haz=[]
        vah1=driver.find_elements_by_xpath("/html/body/div[4]/div/div[2]/table/tbody/tr/td[1]")
        vah2=driver.find_elements_by_xpath("/html/body/div[4]/div/div[2]/table/tbody/tr/td[3]")
        vah=vah1[0].text+vah2[0].text
        for a in range(0,len(vah1)):
            vah=vah1[a].text+vah2[a].text
            if  (vah.startswith('M')):
                  haz.append(vah)
        driver.get('http://www.hu.edu.pk/programs/04%20Years')
        vah1=driver.find_elements_by_xpath("/html/body/div[4]/div/div[2]/table/tbody/tr/td[1]")
        vah2=driver.find_elements_by_xpath("/html/body/div[4]/div/div[2]/table/tbody/tr/td[3]")
        vah=vah1[0].text+vah2[0].text
        for a in range(0,len(vah1)):
            if  (vah.startswith('M')):
                  haz.append(vah)
        haz_uni=pd.DataFrame(haz,columns=["Hazara University"])
    except:
        error_kpk.append("Hazara University")
        haz_uni=pd.DataFrame(columns=["Hazara University"])
    try:
        driver.get('https://imsciences.edu.pk/graduate/')
        ims=[]
        course=driver.find_elements_by_xpath("/html/body/div[1]/section/div/div/div[1]/div/div/div/ul/li")
        for z in course:
            if (z.text.startswith('M')):
                ims.append(z.text)
        driver.get('https://imsciences.edu.pk/research-degrees/')
        course=driver.find_elements_by_xpath("/html/body/div[1]/section/div/div/div[1]/div/div/div/ul/li")
        for z in course:
            if (z.text.startswith('M')):
                ims.append(z.text)
        ims_uni=pd.DataFrame(ims,columns=["Institute of Management Sciences"])
    except:
        error_kpk.append("Institute of Management Sciences")
        ims_uni=pd.DataFrame(columns=["Institute of Management Sciences"])
    try:
        driver.get('http://www.inu.edu.pk/program-offering/')
        iqra=[]
        rows=len(driver.find_elements_by_xpath("/html/body/div[2]/div/div/section[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr/td[2]"))
        l=driver.find_elements_by_xpath("/html/body/div[2]/div/div/section[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr/td[2]")
        for a in range(0,rows):
            result1 = l[a].text.startswith('B')
            result2 = l[a].text.startswith('Required')
            result3 = l[a].text.startswith('Doctor')
            result4 = l[a].text.startswith('Ph')
            if  not (result1 or  result2 or result3 or result4):
                iqra.append(l[a].text)
        iqra_uni=pd.DataFrame(iqra,columns=["Iqra National University"])
    except:
        error_kpk.append("Iqra National University")
        iqra_uni=pd.DataFrame(columns=["Iqra National University"])
    try:
        driver.get('https://www.kkkuk.edu.pk/admission-open-fall-2020/')
        kkk=[]
        value=driver.find_elements_by_xpath("/html/body/div[1]/main/div/div/div/div/div/div[3]/div[3]/table[2]/tbody/tr/td[2]/p")
        for a in value:
            if (a.text.startswith('M')):
                kkk.append(a.text)
        value=driver.find_elements_by_xpath("/html/body/div[1]/main/div/div/div/div/div/div[3]/div[3]/table[3]/tbody/tr/td[2]/p")
        for a in value:
            if (a.text.startswith('M')):
                kkk.append(a.text)
        kkk_uni=pd.DataFrame(kkk,columns=["Khushal Khan Khattak University"])
    except:
        error_kpk.append("Khushal Khan Khattak University")
        kkk_uni=pd.DataFrame(columns=["Khushal Khan Khattak University"])
    try:
        driver.get('https://www.eduvision.edu.pk/khyber-medical-university-kmu-peshawar-ins-1310413172')
        kmu=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            kmu.append(a.text)
        kmu_uni=pd.DataFrame(kmu,columns=["Khyber Medical University"])
    except:
        error_kpk.append("Khyber Medical University")
        kmu_uni=pd.DataFrame(columns=["Khyber Medical University"])
    try:
        driver.get('https://www.eduvision.edu.pk/kohat-university-of-science-technology-kust-kohat-ins-17')
        kust=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            kust.append(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            kust.append(a.text)
        kust_uni=pd.DataFrame(kust,columns=["Kohat University of Science and Technology"])
    except:
        error_kpk.append("Kohat University of Science and Technology")
        kust_uni=pd.DataFrame(columns=["Kohat University of Science and Technology"])
    try:
        driver.get('http://www.northern.edu.pk/#')
        north=[]
        time.sleep(5)
        action = ActionChains(driver);
        for c in range(1,6):
            try:
                parent_level_menu = driver.find_element_by_xpath("//*[@id='drop-down-left']/li[3]/a")
                action.move_to_element(parent_level_menu).perform()
                parent_level_menu = driver.find_element_by_xpath("//*[@id='drop-down-left']/li[3]/ul/li["+str(c)+"]")
                action.move_to_element(parent_level_menu).perform()
                for r in range(1,30):
                    try:
                        value=driver.find_element_by_xpath("//*[@id='drop-down-left']/li[3]/ul/li["+str(c)+"]/ul/li["+str(r)+"]/a").text
                        north.append(value) 
                    except NoSuchElementException:
                        pass
            except NoSuchElementException:
                pass
        north_uni=pd.DataFrame(north,columns=["Northern University"])
    except:
        error_kpk.append("Northern University")
        north_uni=pd.DataFrame(columns=["Northern University"])
    try:
        driver.get('https://www.eduvision.edu.pk/admissions/qurtuba-university-of-science-information-technology-peshawar-admissions-bachelor-level-66')
        qur=[]
        time.sleep(5)
        for r in range(7,76):
            try:
                value=driver.find_element_by_xpath("//*[@id='post_content']/article/div[1]/div/ul/a["+str(r)+"]/li").text
                qur.append(value) 
            except NoSuchElementException:
                pass
        qur_uni=pd.DataFrame(qur,columns=["Qurtaba University of Science & Information Technology"])
    except:
        error_kpk.append("Qurtaba University of Science & Information Technology")
        qur_uni=pd.DataFrame(columns=["Qurtaba University of Science & Information Technology"])
    try:
        driver.get('https://www.eduvision.edu.pk/admissions/sarhad-university-of-science-information-technology-peshawar-admissions-bachelor-level-67')
        action = ActionChains(driver);
        sar=[]
        time.sleep(5)
        for r in range(25,50):
            try:
                value=driver.find_element_by_xpath("//*[@id='post_content']/article/div[1]/div/ul/a["+str(r)+"]/li").text
                sar.append(value) 
            except NoSuchElementException:
                pass
        sar_uni=pd.DataFrame(sar,columns=["Sarhad University"])
    except:
        error_kpk.append("Sarhad University")
        sar_uni=pd.DataFrame(columns=["Sarhad University"])
    try:
        driver.get('http://sbbwu.edu.pk/sbbwu/Academics/index/MS_MPhil_programs')
        sbbwu=[]
        time.sleep(5)
        for r in range(1,66):
            try:
                value=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/div/div/div/p/a["+str(r)+"]").text
                sbbwu.append(value)
            except NoSuchElementException:
                pass
        driver.get('http://sbbwu.edu.pk/sbbwu/Academics/index/master')
        time.sleep(5)
        for r in range(1,66):
            try:
                value=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/div/div/div/p["+str(r)+"]/a").text
                sbbwu.append(value)
            except NoSuchElementException:
                pass
        sbbwu_uni=pd.DataFrame(sbbwu,columns=["Shaheed Benazir Bhutto Women University"])
    except:
        error_kpk.append("Shaheed Benazir Bhutto Women University")
        sar_uni=pd.DataFrame(columns=["Sarhad University"])
    try:
        driver.get('https://www.eduvision.edu.pk/islamia-college-university-icu-peshawar-ins-219')
        isl=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]')
        button.click()
        for r in range(1,12):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                isl.append(value)                  
            except NoSuchElementException:
                pass
        isl_uni=pd.DataFrame(isl,columns=["Islamia College"])
    except:
        error_kpk.append("Islamia College")
        isl_uni=pd.DataFrame(columns=["Islamia College"])
    try:
        driver.get('https://www.eduvision.edu.pk/the-university-of-agriculture-uap-peshawar-ins-25')
        uoap=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]')
        button.click()
        for r in range(1,25):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                uoap.append(value)                  
            except NoSuchElementException:
                pass
        uoap_uni=pd.DataFrame(uoap,columns=["Uni of Agriculture Peshawar "])
    except:
        error_kpk.append("Uni of Agriculture Peshawar")
        uoap_uni=pd.DataFrame(columns=["Uni of Agriculture Peshawar "])
    try:
        driver.get('https://www.eduvision.edu.pk/the-university-of-lakki-marwat-ulm-lakki-marwat-ins-1522085320')
        lak=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]')
        button.click()
        for r in range(1,20):
            try:
                value=driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                lak.append(value)
            except NoSuchElementException:
                pass
        lak_uni=pd.DataFrame(lak,columns=["University of Lakki Marwat"])
    except:
        error_kpk.append("University of Lakki Marwat")
        lak_uni=pd.DataFrame(columns=["University of Lakki Marwat"])
    try:
        driver.get('https://www.eduvision.edu.pk/the-university-of-buner-uob-buner-ins-1505707037')
        time.sleep(5)
        buner=[]
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]')
        button.click()
        for r in range(1,25):
            try:
                value=driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text   
                buner.append(value)
            except NoSuchElementException:
                pass
        buner_uni=pd.DataFrame(buner,columns=["University of Buner"])
    except:
        error_kpk.append("University of Buner")
        buner_uni=pd.DataFrame(columns=["University of Buner"])
    try:
        driver.get('https://uoch.edu.pk/index.php/admissions/graduate/')
        time.sleep(5)
        chitral=[]
        for r in range(1,20):
            try:
                value=driver.find_element_by_xpath("//*[@id='panel-63-0-1-0']/div/div/div/ol/li["+str(r)+"]").text   
                chitral.append(value)
            except NoSuchElementException:
                pass
        chitral_uni=pd.DataFrame(chitral,columns=["University of Chitral"])
    except:
        error_kpk.append("University of Chitral")
        chitral_uni=pd.DataFrame(columns=["University of Chitral"])
    try:
        driver.get('https://uetpeshawar.edu.pk/dpgs/index.php')
        time.sleep(5)
        uetp=[]
        for r in range(1,30):
            try:
                value=driver.find_element_by_xpath("//*[@id='solusi-content']/blockquote/table/tbody/tr["+str(r)+"]/td").text   
                uetp.append(value)
            except NoSuchElementException:
                pass
        uetp_uni=pd.DataFrame(uetp,columns=["UET Peshawar"])
    except:
        error_kpk.append("UET Peshawar")
        uetp_uni=pd.DataFrame(columns=["UET Peshawar"])
    try:
        driver.get('https://www.eduvision.edu.pk/admissions/university-of-engineering-technology-mardan-campus--mardan-admissions-ms-mphil-18-years-level-3958')
        time.sleep(5)
        uetm=[]
        for r in range(1,6):
            try:
                value=driver.find_element_by_xpath("//*[@id='post_content']/article/div[1]/div/ul/a["+str(r)+"]/li").text   
                uetm.append(value)                 
            except NoSuchElementException:
                pass
        uetm_uni=pd.DataFrame(uetm,columns=["UET Mardan"]) 
    except:
        error_kpk.append("UET Mardan")
        uetm_uni=pd.DataFrame(columns=["UET Mardan"]) 
    try:
        driver.get('https://www.eduvision.edu.pk/university-of-haripur-uoh-haripur-ins-1377886413')
        har_uni=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]')
        button.click()
        for r in range(1,25):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                har_uni.append(value)                  
            except NoSuchElementException:
                pass
        har_uni=pd.DataFrame(har_uni,columns=["Haripur Uni"]) 
    except:
        error_kpk.append("Haripur Uni")
        har_uni=pd.DataFrame(columns=["Haripur Uni"]) 
    try:
        driver.get('https://uom.edu.pk/departments/')
        uom=[]
        time.sleep(5)
        for r in range(1,60):
            try:
                value= driver.find_element_by_xpath("//*[@id='row_degreeprogram_section']/div/div[2]/div[1]/table/tbody/tr[2]/td/ol/li["+str(r)+"]/a").text
                uom.append(value)                   
            except NoSuchElementException:
                pass
        for c in range(2,10,2):
            try:
                for r in range(1,60):
                    try:
                        value= driver.find_element_by_xpath("//*[@id='row_degreeprogram_section']/div/div[2]/div[2]/div/table/tbody/tr["+str(c)+"]/td/ol/li["+str(r)+"]/a").text
                        uom.append(value)
                    except NoSuchElementException:
                        pass
            except NoSuchElementException:
                    pass
        uom_uni=pd.DataFrame(uom,columns=["University of Malakand"])
    except:
        error_kpk.append("University of Malakand")
        uom_uni=pd.DataFrame(columns=["University of Malakand"])
    try:
        driver.get('http://www.uop.edu.pk/admissions/?q=Postgraduate&r=Postgraduate-Departments')
        pesh=[]
        time.sleep(5)
        for page in range(1,42):
            try:
                value=driver.find_element_by_xpath("//*[@id='team-container']/ol/li["+str(page)+"]/a/h5").text
                pesh.append(value)
            except NoSuchElementException:
                pass  
        pesh_uni=pd.DataFrame(pesh,columns=["Uni of Peshawar"])
    except:
        error_kpk.append("Uni of Peshawar")
        pesh_uni=pd.DataFrame(columns=["Uni of Peshawar"])
    try:
        driver.get('https://www.eduvision.edu.pk/university-of-science-technology-ust-bannu-ins-4233')
        ust=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]')
        button.click()
        for r in range(1,60):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                ust.append(value)                   
            except NoSuchElementException:
                pass
        ust_uni=pd.DataFrame(ust,columns=["University of Science & Technology"])
    except:
        error_kpk.append("University of Science & Technology")
        ust_uni=pd.DataFrame(columns=["University of Science & Technology"])
    try:
        driver.get('https://www.eduvision.edu.pk/university-of-swabi-uos-swabi-ins-1364647720')
        swabi=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]')
        button.click()
        for r in range(1,60):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                swabi.append(value)                   
            except NoSuchElementException:
                pass
        swabi_uni=pd.DataFrame(swabi,columns=["Uni of Swabi "])
    except:
        error_kpk.append("Uni of Swabi")
        swabi_uni=pd.DataFrame(columns=["Uni of Swabi "])
    try:
        driver.get('https://uswat.edu.pk/2021/03/13/ms-mphil-and-phd-admissions-status/')
        swat=[]
        time.sleep(5)
        for r in range(1,15):
            try:
                value=driver.find_element_by_xpath("//*[@id='post-6429']/div/div/div/div/div/section[2]/div/div/div/div/div/div/div/ul/b/li["+str(r)+"]/a/span[2]").text
                swat.append(value)                
            except NoSuchElementException:          
                pass
        swat_uni=pd.DataFrame(swat,columns=["University of Swat"])
    except:
        error_kpk.append("University of Swat")
        swat_uni=pd.DataFrame(columns=["University of Swat"])
    try:
        driver.get('https://www.eduvision.edu.pk/women-university-swabi-wus-swabi-ins-1442885100')
        wus=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]')
        button.click()
        for r in range(1,60):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                wus.append(value)                   
            except NoSuchElementException:
                pass
        wus_uni=pd.DataFrame(wus,columns=["Women Uni Swabi"])
    except:
        error_kpk.append("Women Uni Swabi")
        wus_uni=pd.DataFrame(columns=["Women Uni Swabi"])
    try:
        driver.get('https://www.eduvision.edu.pk/women-university-mardan-wum-mardan-ins-1475717226')
        wum=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]')
        button.click()
        for r in range(1,60):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                wum.append(value)                   
            except NoSuchElementException:
                pass
        wum_uni=pd.DataFrame(wum,columns=["Women Uni Mardan"])
    except:
        error_kpk.append("Women Uni Mardan")
        wum_uni=pd.DataFrame(columns=["Women Uni Mardan"])
    global pdList_kpk
    global kpk_df
    pdList_kpk=[aba_uni,abott_uni,awku_uni,bacha_uni,cecos_uni,
            city_uni,gand_uni,giki_uni,gom_uni,haz_uni,
            ims_uni,iqra_uni,kkk_uni,kmu_uni,kust_uni,
            north_uni,qur_uni,sar_uni,sbbwu_uni,isl_uni,
            uoap_uni,lak_uni,buner_uni,chitral_uni,
            uetp_uni,uetm_uni,har_uni,uom_uni,pesh_uni,ust_uni,swabi_uni,swat_uni,wus_uni,wum_uni]
    kpk_df=pd.concat(pdList_kpk, axis=1)
    print(kpk_df)
    eventkpk.set()
    event2kpk.set()
    event3kpk.set()
    event4kpk.set()
    event5kpk.set()
def punjab_ms():
    import requests
    import lxml.html as lh
    import pandas as pd
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    try:
        bzu=[]
        driver.get('https://www.bzu.edu.pk/v2_departments.php')
        arr=[]
        for b in driver.find_elements_by_xpath("/html/body/div[7]/div/div[2]/div[3]/div[3]/table/tbody/tr/td/table/tbody/tr/td/ul/li/a"):
            arr.append(b.get_attribute('href'))
        for a in arr:
            driver.get(a)
            course=driver.find_elements_by_xpath("/html/body/div[7]/div/div[2]/div[3]/div[3]/div[2]/ul/li[1]")
            for z in course:
                if (z.text.startswith('M')):
                    bzu.append(z.text)
        bzu_uni=pd.DataFrame(bzu,columns=["Bahauddin Zakariya University"])
    except:
        error_pun.append("Bahauddin Zakariya University")
        bzu_uni=pd.DataFrame(columns=["Bahauddin Zakariya University"])
    try:
        driver.get('https://www.bnu.edu.pk/bnu/Academics/Programs-of-Study')
        bnu=[]
        courses=driver.find_elements_by_xpath("/html/body/form/div[3]/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div/div/div/div/div/div/table/tbody/tr/td[1]")
        for z in courses:
            result3 = z.text.startswith('M')
            if   (result3):
                bnu.append(z.text)
        bnu_uni=pd.DataFrame(bnu,columns=[" Beaconhouse National University"])
    except:
        error_pun.append("Beaconhouse National University")
        bnu_uni=pd.DataFrame(columns=[" Beaconhouse National University"])
    try:
        driver.get('http://www.cuvas.edu.pk/Admissions/postGraduate/mPhil-Phd/index.htm')
        cuv=[]
        courses=driver.find_elements_by_xpath("/html/body/div[4]/div/div[3]/table/tbody/tr[4]/td/table/tbody/tr[3]/td/ul/li")
        for z in courses:
            result3 = z.text.startswith('M')
            if   (result3):
                cuv.append(z.text)
        cuvas_uni=pd.DataFrame(cuv,columns=["Cholistan University of Veterinary and Animal Sciences, Bahawalpur"])
    except:
        error_pun.append("Cholistan University of Veterinary and Animal Sciences, Bahawalpur")
        cuvas_uni=pd.DataFrame(columns=["Cholistan University of Veterinary and Animal Sciences, Bahawalpur"])
    try:
        driver.get('https://www.fjwu.edu.pk/higher-degree-program/')
        fjwu=[]
        course=driver.find_elements_by_xpath("/html/body/div[1]/div[5]/div[2]/div[2]/table/tbody/tr/td[3]/p")
        for z in course:
            fjwu.append("MS/M.Phil","",z.text)
        fjwu_uni=pd.DataFrame(fjwu,columns=[" Fatima Jinnah Women University"])
    except:
        error_pun.append("Fatima Jinnah Women University")
        fjwu_uni=pd.DataFrame(columns=[" Fatima Jinnah Women University"])
    try:
        driver.get('https://www.eduvision.edu.pk/forman-christian-college-fcc-lahore-ins-347')
        fc=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            fc.append(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            fc.append(a.text)
        fc_uni=pd.DataFrame(fc,columns=[" Forman Christian College"])
    except:
        error_pun.append(" Forman Christian College")
        fc_uni=pd.DataFrame(columns=[" Forman Christian College"])
    try:
        driver.get('https://www.gift.edu.pk/page/schools-and-programs')
        gift=[]
        name=driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div[2]/a")
        for a in name:
            if (a.text.startswith('M')):
                gift.append(a.text)
        gift_uni=pd.DataFrame(gift,columns=[" GIFT University"])
    except:
        error_pun.append(" GIFT University")
        gift_uni=pd.DataFrame(columns=[" GIFT University"])
    try:
        driver.get('https://www.gudgk.edu.pk/admission-criteria/')
        ghazi=[]
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div[3]/div/div/div/div[1]/article/table/tbody/tr/td[2]")
        for a in name:
            if (a.text.startswith('M')):
                ghazi.append(a.text)
        ghazi_uni=pd.DataFrame(ghazi,columns=[" Ghazi University"])
    except:
        error_pun.append(" Ghazi University")
        ghazi_uni=pd.DataFrame(columns=[" Ghazi University"])
    try:
        driver.get('https://www.eduvision.edu.pk/government-college-university-gcu-faisalabad-ins-279')
        gcf=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            print(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            gcf.append(a.text)
        gcf_uni=pd.DataFrame(gcf,columns=["Government College University"])
    except:
        error_pun.append("Government College University")
        gcf_uni=pd.DataFrame(columns=["Government College University"])
    try:
        driver.get('https://gcu.edu.pk/')
        gcl=[]
        arr=[]
        from selenium.webdriver.common.action_chains import ActionChains
        a = ActionChains(driver)
        m = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/header/div/div/div/div[4]/div/nav/ul/li[4]/a[1]")
        a.move_to_element(m).perform()
        for b in driver.find_elements_by_xpath("/html/body/div[2]/div/div[1]/header/div/div/div/div[4]/div/nav/ul/li[4]/div/ul/li/ul/li/a"):
            arr.append(b.get_attribute('href'))
        for d in arr:
            driver.get(d)
            name=driver.find_elements_by_xpath("/html/body/div/div/div[2]/div/section/div/div/div/div/div/div/div/div/div/div/div[1]/h4/a/span")
            for a in name:
                if (a.text.startswith('M')):
                    gcl.append(a.text)
        gcl_uni=pd.DataFrame(gcl,columns=["Government College University, Lahore"])
    except:
        error_pun.append("Government College University, Lahore")
        gcl_uni=pd.DataFrame(columns=["Government College University, Lahore"])
    try:
        driver.get('https://www.eduvision.edu.pk/government-college-women-university-gcwu-sialkot-ins-1411921503')
        gcwu=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            print(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            gcwu.append(a.text)
        gcwu_uni=pd.DataFrame(gcwu,columns=["Government College for Women University, Sialkot"])
    except:
        error_pun.append("Government College for Women University, Sialkot")
        gcwu_uni=pd.DataFrame(columns=["Government College for Women University, Sialkot"])
    try:
        driver.get('https://www.eduvision.edu.pk/the-government-sadiq-college-women-university-gscwu-bahawal-pur-ins-1313215922')
        gswu=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            print(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            gswu.append(a.text)
        gswu_uni=pd.DataFrame(gswu,columns=["Government College for Women University, Sialkot"])
    except:
        error_pun.append("Government College for Women University, Sialkot")
        gswu_uni=pd.DataFrame(columns=["Government College for Women University, Sialkot"])
    try:
        driver.get('https://www.hitecuni.edu.pk/')
        time.sleep(15)
        hitec=[]
        from selenium.webdriver.common.action_chains import ActionChains
        a = ActionChains(driver)
        m = driver.find_element_by_xpath("/html/body/form/div[3]/header/div[1]/div[2]/div/div/div[2]/nav/ul/li[3]/a")
        n = driver.find_elements_by_xpath("/html/body/form/div[3]/header/div[1]/div[2]/div/div/div[2]/nav/ul/li[3]/ul/li/a")
        a.move_to_element(m).perform()
        time.sleep(2)
        for b in n:
            a = ActionChains(driver)
            a.move_to_element(b).perform()
            q = driver.find_elements_by_xpath("/html/body/form/div[3]/header/div[1]/div[2]/div/div/div[2]/nav/ul/li[3]/ul/li/ul/li/a")
            time.sleep(2)
            for c in q:
                if (b.text):
                    if (c.text):
                        if  (b.text.startswith('PO')):
                            hitec.append(b.text,c.text)
        hitec_uni=pd.DataFrame(hitec,columns=["HITEC University"])
    except:
        error_pun.append("HITEC University")
        hitec_uni=pd.DataFrame(columns=["HITEC University"])
    try:
        driver.get('https://hajvery.edu.pk/#degrees')
        hj=[]
        name=driver.find_elements_by_xpath("/html/body/div/main/div/div[5]/div/div/div/div/div/div[2]/div/div/div/ul/li/a")
        for a in name:
            print(a.text)
        name=driver.find_elements_by_xpath("/html/body/div/main/div/div[5]/div/div/div/div/div/div[3]/div/div/div/ul/li/a")
        for a in name:
            if (a.text.startswith('M')):
                hj.append(a.text)
        hj_uni=pd.DataFrame(hj,columns=["Hajvery University, Lahore"])
    except:
        error_pun.append("Hajvery University, Lahore")
        hj_uni=pd.DataFrame(columns=["Hajvery University, Lahore"])
    try:
        driver.get('http://itu.edu.pk/admissions/#undergraduate')
        itu=[]
        section=len(driver.find_elements_by_xpath("/html/body/div[4]/div[2]/div[4]/div/div[1]/div/ul/li"))
        for r in range(1,section+1):
            subsection=len(driver.find_elements_by_xpath("/html/body/div[4]/div[2]/div[4]/div/div["+str(r)+"]/div/ul/li"))
            for c in range (1, subsection+1):
                course_name=driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[4]/div/div["+str(r)+"]/div/ul/li["+str(c)+"]").text
                result1 = course_name.startswith('M')
                if  (result1):
                    itu.append(course_name)     
        itu_uni=pd.DataFrame(itu,columns=["Information Technology University of the Punjab"]) 
    except:
        error_pun.append("Information Technology University of the Punjab")
        itu_uni=pd.DataFrame(columns=["Information Technology University of the Punjab"]) 
    try:
        driver.get('https://www.pakaims.edu.pk')
        ims=[]
        from selenium.webdriver.common.action_chains import ActionChains
        a = ActionChains(driver)
        m = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[3]/a")
        a.move_to_element(m).perform()
        n = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[3]/ul/li/a")
        for j in range(1,len(n)+1):
            b = ActionChains(driver)
            k = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[3]/ul/li["+str(j)+"]/a")
            b.move_to_element(k).perform()
            courses=driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[3]/ul/li["+str(j)+"]/ul/li/a")
            for z in courses:
                if (z.text.startswith('M') or z.text.startswith('E') ):
                    ims.append(z.text)
        ims_uni=pd.DataFrame(ims,columns=["Institute of Management Sciences"])  
    except:
        error_pun.append("Institute of Management Sciences")
        ims_uni=pd.DataFrame(columns=["Institute of Management Sciences"]) 
    try:
        driver.get('https://beta.isp.edu.pk/Admission/AdmissionProcedure')
        isp=[]
        course=driver.find_elements_by_xpath("/html/body/div[3]/div/section/table/tbody/tr/td[1]")
        for z in course:
            if (z.text.startswith('M')):
                isp.append(z.text)
        isp_uni=pd.DataFrame(isp,columns=["Institute of Southern Punjab"]) 
    except:
        error_pun.append("Institute of Southern Punjab")
        isp_uni=pd.DataFrame(columns=["Institute of Southern Punjab"]) 
    try:
        driver.get('https://www.eduvision.edu.pk/the-islamia-university-of-bahawalpur-iub-bahawal-pur-ins-16')
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        isl
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            print(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            isl.append(a.text)
        isl_uni=pd.DataFrame(isl,columns=["Islamia University"])
    except:
        error_pun.append("Islamia University")
        isl_uni=pd.DataFrame(columns=["Islamia University"])
    try:
        driver.get('https://kfueit.edu.pk/academic-programs?main=747&parent=ACADEMICS')
        kfu=[]
        time.sleep(3)
        value=driver.find_elements_by_xpath("/html/body/section[2]/div/div/main/div/div/div/div/ul/li")
        for a in value:
            result = a.text.startswith('M')
            if result:
                kfu.append(a.text)
        kfu_uni=pd.DataFrame(kfu,columns=["Khawaja Freed University of Engineering & Information Technology"])
    except:
        error_pun.append("Khawaja Freed University of Engineering & Information Technology")
        kfu_uni=pd.DataFrame(columns=["Khawaja Freed University of Engineering & Information Technology"])
    try:
        driver.get('https://kemu.edu.pk/programs')
        ke=[]
        driver.execute_script("window.scrollTo(0, 2500)") 
        course=driver.find_elements_by_xpath("/html/body/div/section[2]/div/section/div/div/div/div/div/ol/li")
        for z in course:
            if (z.text.startswith('M')):
                ke.append(z.text)
        ke_uni=pd.DataFrame(ke,columns=["King Edward Medical University"])
    except:
        error_pun.append("King Edward Medical University")
        ke_uni=pd.DataFrame(columns=["King Edward Medical University"])
    try:
        driver.get('http://www.kinnaird.edu.pk/postgraduate/')
        kc=[]
        course=driver.find_elements_by_xpath("/html/body/div[3]/div/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div/ul/li/a/div/span")
        for z in course:
            kc.append(z.text)
        kc_uni=pd.DataFrame(kc,columns=["Kinnaird College for Women"])
    except:
        error_pun.append("Kinnaird College for Women")
        kc_uni=pd.DataFrame(columns=["Kinnaird College for Women"])
    try:
        driver.get('https://www.eduvision.edu.pk/lahore-college-for-women-university-lcwu-lahore-ins-18')
        lcwu=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            lcwu.append(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            lcwu.append(a.text)
        lcwu_uni=pd.DataFrame(lcwu,columns=["Lahore College for Women University"])
    except:
        error_pun.append("Lahore College for Women University")
        lcwu_uni=pd.DataFrame(columns=["Lahore College for Women University"])
    try:
        driver.get('https://www.eduvision.edu.pk/lahore-garrison-university-lgu-lahore-ins-1345089286')
        lgu=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            lgu.append(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            lgu.append(a.text)
        lgu_uni=pd.DataFrame(lgu,columns=["Lahore Garrison University"])
    except:
        error_pun.append("Lahore Garrison University")
        lgu_uni=pd.DataFrame(columns=["Lahore Garrison University"])
    try:
        driver.get('http://www.leads.edu.pk/Graduate_Programs.php')
        llu=[]
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, 800)") 
        time.sleep(5)
        course=driver.find_elements_by_xpath("/html/body/div[8]/div/div/div/div/div/div/div/div[2]/div/div/a/span/p")
        for z in course:
            if not (z.text.startswith('D')):
                llu.append(z.text)
        llu_uni=pd.DataFrame(llu,columns=["Lahore Leads University"])
    except:
        error_pun.append("Lahore Leads University")
        llu_uni=pd.DataFrame(columns=["Lahore Leads University"])
    try:
        driver.get('http://lahoreschoolofeconomics.edu.pk/Academics/postgraduateprograms.aspx')
        lse=[]
        course=driver.find_elements_by_xpath("/html/body/form/div[3]/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[2]/p[7]/table/tbody/tr/td/a")
        for z in course:
            if(z.text.startswith('M')):
                lse.append(z.text)
        lse_uni=pd.DataFrame(lse,columns=["Lahore School of Economics"])
    except:
        error_pun.append("Lahore School of Economics")
        lse_uni=pd.DataFrame(columns=["Lahore School of Economics"])
    try:
        driver.get('https://lums.edu.pk/graduate')
        lums=[]
        course=driver.find_elements_by_xpath("/html/body/div[1]/div/div[5]/div/div[1]/div/div/section/div/div/div[2]/div/ul/li/div[2]/span/div[1]/a/div[2]")
        for z in course:
            if (z.text.startswith('M')):  
                lums.append(z.text)
        lums_uni=pd.DataFrame(lums,columns=["Lahore University of Management Sciences"])
    except:
        error_pun.append("Lahore University of Management Sciences")
        lums_uni=pd.DataFrame(columns=["Lahore University of Management Sciences"])
    try:
        driver.get('https://www.mul.edu.pk/english/admission/graduate-program/')
        minh=[]
        course=driver.find_elements_by_xpath("/html/body/div[2]/div/section[2]/div/div/div[1]/div/div/div/div/h4/a")
        for z in course:
            if (z.text.startswith('M')):
                minh.append(z.text)
        driver.get('https://www.mul.edu.pk/english/admission/post-graduate-program/')
        course=driver.find_elements_by_xpath("/html/body/div[2]/div/section[2]/div/div/div[1]/div/div/div/div/h4/a")
        for z in course:
            if (z.text.startswith('M')):
                minh.append(z.text)
        driver.get('https://www.mul.edu.pk/english/admission/doctoral-program/')
        course=driver.find_elements_by_xpath("/html/body/div[2]/div/section[2]/div/div/div[1]/div/div/div/div/h4/a")
        for z in course:
            if (z.text.startswith('M')):
                minh.append(z.text)
        min_uni=pd.DataFrame(minh,columns=["Minhaj University"])
    except:
        error_pun.append("Minhaj University")
        min_uni=pd.DataFrame(columns=["Minhaj University"])
    try:
        driver.get('https://www.mnsuam.edu.pk/index.php/admissions/programs-offered')
        mnsua=[]
        value=driver.find_elements_by_xpath("/html/body/div[2]/div[3]/div/div/div/article/div[2]/section/table/tbody/tr[3]/td[2]/ul/li")
        for a in value:
            mnsua.append("MS  ",a.text)
        mnsua_uni=pd.DataFrame(mnsua,columns=["Muhammad Nawaz Shareef University of Agriculture"])
    except:
        error_pun.append("Muhammad Nawaz Shareef University of Agriculture")
        mnsua_uni=pd.DataFrame(columns=["Muhammad Nawaz Shareef University of Agriculture"])
    try:
        driver.get('https://www.mnsuet.edu.pk/master-programs/')
        mnsuet=[]
        courses=driver.find_elements_by_xpath("/html/body/div[2]/div/main/div/div/div/section[4]/div/div/div/div/div/div/div/div/p/span/b")
        for z in courses:
            mnsuet.append(z.text)
        mnsuet_uni=pd.DataFrame(mnsuet,columns=["Muhammad Nawaz Sharif University of Engineering & Technology"])
    except:
        error_pun.append("Muhammad Nawaz Sharif University of Engineering & Technology")
        mnsuet_uni=pd.DataFrame(columns=["Muhammad Nawaz Sharif University of Engineering & Technology"])
    try:
        driver.get('http://www.nfciet.edu.pk/')
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/ul/li[4]/a/span").click()
        time.sleep(3)
        nfc=[]
        from selenium.webdriver.common.action_chains import ActionChains
        a = ActionChains(driver)
        m = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/ul/li[4]/div/div/div/div/ul/li[2]/a/span")
        a.move_to_element(m).perform()
        courses=driver.find_elements_by_xpath("/html/body/div/div[2]/div/div/div[2]/ul/li[4]/div/div/div/div/ul/li[2]/div/div/div/div/ul/li/a")
        for z in courses:
            result3 = z.text.startswith('M')
            if   (result3):
                    nfc.append(z.text)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/ul/li[4]/div/div/div/div/ul/li[4]/a/span").click()
        time.sleep(3)
        from selenium.webdriver.common.action_chains import ActionChains
        a = ActionChains(driver)
        m = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/ul/li[4]/div/div/div/div/ul/li[4]/a/span")
        a.move_to_element(m).perform()
        courses=driver.find_elements_by_xpath("/html/body/div/div[2]/div/div/div[2]/ul/li[4]/div/div/div/div/ul/li[4]/div/div/div/div/ul/li/a")
        for z in courses:
            result3 = z.text.startswith('M')
            if   (result3):
                    nfc.append(z.text)
        nfc_uni=pd.DataFrame(nfc,columns=["NFC Institute of Engineering & Technology"])
    except:
        error_pun.append("NFC Institute of Engineering & Technology")
        nfc_uni=pd.DataFrame(columns=["NFC Institute of Engineering & Technology"])
    try:
        driver.get('https://www.nca.edu.pk/programmes')
        nca=[]
        courses=driver.find_elements_by_xpath("/html/body/section[2]/div/div/div[3]/p[2]/a")
        for z in courses:
            if not (z.text.startswith('MPhil &')):
                nca.append(z.text)
        nca_uni=pd.DataFrame(nca,columns=["National College of Arts"])
    except:
        error_pun.append("National College of Arts")
        nca_uni=pd.DataFrame(columns=["National College of Arts"])
    try:
        ncbae=[]
        def fun():
            courses=driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/h5")
            for z in courses:
                result3 = z.text.startswith('M')
                if  (result3):
                    ncbae.append(z.text)
        driver.get('https://ncbae.edu.pk/school-of-business-administration-3/')
        fun()
        driver.get('https://ncbae.edu.pk/school-of-computer-science/')
        fun()
        driver.get('https://ncbae.edu.pk/school-of-social-science/')
        fun()
        ncbae_uni=pd.DataFrame(ncbae,columns=["National College of Business Administration & Economics"])
    except:
        error_pun.append("National College of Business Administration & Economics")
        ncbae_uni=pd.DataFrame(columns=["National College of Business Administration & Economics"])
    try:
        driver.get('https://ntu.edu.pk/')
        ntu=[]
        time.sleep(5)
        for r in range(1,76):
            try:
                value=driver.find_element_by_xpath("/html/body/section[2]/div/div/div[2]/div/div["+str(r)+"]/div/div/a").text
                ntu.append(value) 
            except NoSuchElementException:
                pass
        ntu_uni=pd.DataFrame(ntu,columns=["National Textile Uni"])
    except:
        error_pun.append("National Textile Uni")
        ntu_uni=pd.DataFrame(columns=["National Textile Uni"])
    try:
        driver.get('https://www.drnajeeblectures.com/nishtar-medical-college/')
        nis=[]
        time.sleep(5)
        for r in range(7,20):
            try:
                value=driver.find_element_by_xpath("//*[@id='tm-main']/div/div/main/article/ul[6]/li["+str(r)+"]").text
                nis.append(value) 
            except NoSuchElementException:
                pass
        nis_uni=pd.DataFrame(nis,columns=["Nishtar Medical"])
    except:
        error_pun.append("Nishtar Medical")
        nis_uni=pd.DataFrame(columns=["Nishtar Medical"])
    try:
        driver.get('https://www.eduvision.edu.pk/nur-international-university-niu-lahore-ins-1445753678')
        nur=[]
        time.sleep(5)
        button=driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]")
        button.click()
        time.sleep(1)
        for r in range(1,76):
            try:
                value=driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                nur.append(value) 
            except NoSuchElementException:
                pass
        nur_uni=pd.DataFrame(nur,columns=["Nur University"])
    except:
        error_pun.append("Nur University")
        nur_uni=pd.DataFrame(columns=["Nur University"])
    try:
        driver.get('http://www.pifd.edu.pk/post-graduate.html')
        pifd=[]
        time.sleep(5)
        value=driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/h2").text
        pifd.append(value) 
        pifd_uni=pd.DataFrame(pifd,columns=["Pakistan Institute of Fashion"])
    except:
        error_pun.append("Pakistan Institute of Fashion")
        pifd_uni=pd.DataFrame(columns=["Pakistan Institute of Fashion"])
    try:
        driver.get('https://www.eduvision.edu.pk/pir-mahar-ali-shah-arid-agriculture-university-uaa-rawalpindi-ins-34')
        pir=[]
        button=driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]")
        button.click()
        time.sleep(5)
        for r in range(1,76):
            try:
                value=driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                pir.append(value) 
            except NoSuchElementException:
                pass
        pir_uni=pd.DataFrame(pir,columns=["Pir Mehr Ali Shah University"])
    except:
        error_pun.append("Pir Mehr Ali Shah University")
        pir_uni=pd.DataFrame(columns=["Pir Mehr Ali Shah University"])
    try:
        driver.get('https://rmur.edu.pk/admission-4/')
        rmu=[]
        time.sleep(5)
        for r in range(14,23):
            try:
                value=driver.find_element_by_xpath("//*[@id='content']/article/div/div/div/div/section[1]/div/div/div/div/div/div/div/div/p["+str(r)+"]/span/span[2]").text
                rmu.append(value) 
            except NoSuchElementException:
                pass
        rmu_uni=pd.DataFrame(rmu,columns=["Rawalpindi Medical University"])
    except:
        error_pun.append("Rawalpindi Medical University")
        rmu_uni=pd.DataFrame(columns=["Rawalpindi Medical University"])
    try:
        driver.get('https://www.superior.edu.pk/graduate-programs/')
        time.sleep(5)
        su=[]
        for r in range(1,55):
            try:
                value=driver.find_element_by_xpath("//*[@id='kingster-page-wrapper']/div/div[1]/div/div/div[3]/div/div["+str(r)+"]/a/span").text
                su.append(value)                   
            except NoSuchElementException:
                pass
        su_uni=pd.DataFrame(su,columns=["Superior University"])
    except:
        error_pun.append("Superior University")
        su_uni=pd.DataFrame(columns=["Superior University"])
    try:
        driver.get('https://tuf.edu.pk/graduate-programs')
        time.sleep(5)
        tuf=[]
        for r in range(1,38):
            try:
                value=driver.find_element_by_xpath("//*[@id='wrapper']/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a/p").text
                tuf.append(value)
            except NoSuchElementException:
                pass
        tuf_uni=pd.DataFrame(tuf,columns=["University of Faisalabad"])
    except:
        error_pun.append("University of Faisalabad")
        tuf_uni=pd.DataFrame(columns=["University of Faisalabad"])
    try:
        driver.get('https://www.eduvision.edu.pk/the-women-university-wum-multan-ins-1407350525')
        wum=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]')
        button.click()
        for r in range(1,50):
            try:
                value=driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                wum.append(value)
            except NoSuchElementException:
                pass
        wum_uni=pd.DataFrame(wum,columns=["Women University"])
    except:
        error_pun.append("Women University")
        wum_uni=pd.DataFrame(columns=["Women University"])
    try:
        driver.get('https://www.eduvision.edu.pk/times-institute-tse-multan-ins-1409977739')
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]')
        button.click()
        times=[]
        for r in range(1,66):
            try:
                value=driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                times.append(value)                   
            except NoSuchElementException:
                pass
        times_uni=pd.DataFrame(times,columns=["Times Institute"])
    except:
        error_pun.append("Times Institute")
        times_uni=pd.DataFrame(columns=["Times Institute"])
    try:
        driver.get('https://www.eduvision.edu.pk/the-university-of-agriculture-uap-peshawar-ins-25')
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]')
        button.click()
        uoap=[]
        for r in range(1,66):
            try:
                value=driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                uoap.append(value)                   
            except NoSuchElementException:
                pass
        uoap_uni=pd.DataFrame(uoap,columns=["University of Agriculture KPK"])
    except:
        error_pun.append("University of Agriculture KPK")
        uoap_uni=pd.DataFrame(columns=["University of Agriculture KPK"])
    try:
        driver.get('https://www.ucp.edu.pk/postgraduate/')
        time.sleep(5)
        ucp=[]
        for r in range(2,30):
            try:
                value=driver.find_element_by_xpath("//*[@id='content']/article/div[1]/div[1]/div/div/div/div[2]/ul/li["+str(r)+"]/span[1]").text   
                ucp.append(value)
            except NoSuchElementException:
                pass
        for r in range(2,30):
            try:
                value=driver.find_element_by_xpath("//*[@id='content']/article/div[1]/div[1]/div/div/div/div[3]/div/div/div/div/ul/li["+str(r)+"]/span[1]/a").text   
                ucp.append(value)
            except NoSuchElementException:
                pass
        ucp_uni=pd.DataFrame(ucp,columns=["University of Central Punjab"])
    except:
        error_pun.append("University of Central Punjab")
        ucp_uni=pd.DataFrame(columns=["University of Central Punjab"])
    try:
        driver.get('https://www.eduvision.edu.pk/university-of-chakwal-uoc-chakwal-ins-1474974090')
        time.sleep(5)
        uoc=[]
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]')
        button.click()
        for r in range(1,25):
            try:
                value=driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text   
                uoc.append(value)
            except NoSuchElementException:
                pass
        uoc_uni=pd.DataFrame(uoc,columns=["University of Chakwal"])
    except:
        error_pun.append("University of Chakwal")
        uoc_uni=pd.DataFrame(columns=["University of Chakwal"])
    try:
        driver.get('https://ue.edu.pk/degreeprograms.php')
        time.sleep(5)
        ue=[]
        for c in range(2,4):
            try:
                for r in range(1,14):
                    try:
                        value=driver.find_element_by_xpath("//*[@id='ueitcell-about']/div/div/div[2]/ul["+str(c)+"]/li["+str(r)+"]").text   
                        ue.append(value)
                    except NoSuchElementException:
                        pass
            except NoSuchElementException:
                pass
        edu_uni=pd.DataFrame(ue,columns=["Education University"])
    except:
        error_pun.append("Education University")
        edu_uni=pd.DataFrame(columns=["Education University"])
    try:
        driver.get('https://www.uet.edu.pk/faculties/facultiesinfo/index.html?RID=postgraduate_academic_programs')
        time.sleep(5)
        uetl=[]
        for r in range(2,200,2):
            try:
                value=driver.find_element_by_xpath("//*[@id='page-content']/div[1]/div/div[2]/div[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr["+str(r)+"]/td[2]/a").text   
                uetl.append(value)                 
            except NoSuchElementException:
                pass
        uetl_uni=pd.DataFrame(uetl,columns=["UET, Lahore"])
    except:
        error_pun.append("UET, Lahore")
        uetl_uni=pd.DataFrame(columns=["UET, Lahore"])
    try:
        driver.get('https://web.uettaxila.edu.pk/PGprogram.aspx')
        uett=[]
        time.sleep(5)
        for r in range(1,66):
            try:
                value=driver.find_element_by_xpath("//*[@id='ContentPlaceHolder1_lblPageHTML']/div/div/div[2]/div/div/blockquote["+str(r)+"]/p[1]/strong").text
                uett.append(value)
            except NoSuchElementException:
                pass
        uett_uni=pd.DataFrame(uett,columns=["UET Taxilla"])
    except:
        error_pun.append("UET Taxilla")
        uett_uni=pd.DataFrame(columns=["UET Taxilla"])
    try:
        driver.get('https://www.eduvision.edu.pk/university-of-gujrat-uog-gujrat-ins-3223')
        ug=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]')
        button.click()
        for r in range(1,25):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                ug.append(value)                  
            except NoSuchElementException:
                pass
        ug_uni=pd.DataFrame(ug,columns=["University of Gujrat"])
    except:
        error_pun.append("University of Gujrat")
        ug_uni=pd.DataFrame(columns=["University of Gujrat"])
    try:
        driver.get('https://www.uhs.edu.pk/pg-PostgraduatePrograms.php')
        time.sleep(5)
        uhs=[]
        for r in range(3,26):
            try:
                value=driver.find_element_by_xpath("//*[@id='pg']/table[1]/tbody/tr["+str(r)+"]/td[2]/span").text   
                uhs.append(value)
            except NoSuchElementException:
                pass
        uhs_uni=pd.DataFrame(uhs,columns=["Uni of Health Sciences"])
    except:
        error_pun.append("Uni of Health Sciences")
        uhs_uni=pd.DataFrame(columns=["Uni of Health Sciences"])
    try:
        driver.get('https://uhe.edu.pk/programs/m-phil-programs/')
        time.sleep(5)
        uhe=[]
        for r in range(1,26):
            try:
                value=driver.find_element_by_xpath("//*[@id='post-435']/div/div[2]/div/div/div/div/div/ul/li["+str(r)+"]").text   
                uhe.append(value)
            except NoSuchElementException:
                pass
        uni_econ=pd.DataFrame(uhe,columns=["Uni of Home Economics"])
    except:
        error_pun.append("Uni of Home Economics")
        uni_econ=pd.DataFrame(columns=["Uni of Home Economics"])
    try:
        driver.get('https://www.eduvision.edu.pk/the-university-of-lahore-main-campus-ul-lahore-ins-711')
        uol=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]')
        button.click()
        for r in range(1,60):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                uol.append(value)                   
            except NoSuchElementException:
                pass
        uol_uni=pd.DataFrame(uol,columns=["Uni of Lahore"])
    except:
        error_pun.append("Uni of Lahore")
        uol_uni=pd.DataFrame(columns=["Uni of Lahore"])
    try:
        driver.get('https://www.eduvision.edu.pk/university-of-management-and-technology-umt-lahore-ins-825')
        umt=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]')
        button.click()
        for r in range(1,60):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                umt.append(value)                   
            except NoSuchElementException:
                pass
        umt_uni=pd.DataFrame(umt,columns=["University of Management & Technology"])
    except:
        error_pun.append("University of Management & Technology")
        umt_uni=pd.DataFrame(columns=["University of Management & Technology"])
    try:
        driver.get('https://umw.edu.pk/pages/main/academics/botany')
        action = ActionChains(driver);
        mian=[]
        time.sleep(5)
        parent_level_menu = driver.find_element_by_xpath("//*[@id='page']/nav/div[2]/div/div/div[2]/ul/li[4]")
        action = ActionChains(driver);
        action.move_to_element(parent_level_menu).perform()
        for r in range(1,15):
            try:
                 value=driver.find_element_by_xpath("//*[@id='page']/nav/div[2]/div/div/div[2]/ul/li[4]/ul/li["+str(r)+"]").text
                 mian.append(value)
            except NoSuchElementException:
                pass
        mian_uni=pd.DataFrame(mian,columns=[" Uni of Mianwali"])
    except:
        error_pun.append(" Uni of Mianwali")
        mian_uni=pd.DataFrame(columns=[" Uni of Mianwali"])
    try:
        driver.get('https://www.eduvision.edu.pk/university-of-narowal-uon-narowal-ins-1568895668')
        uon=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]')
        button.click()
        for r in range(1,25):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                uon.append(value)                  
            except NoSuchElementException:
                pass
        uon_uni=pd.DataFrame(uon,columns=["Uni of Narowal"])
    except:
        error_pun.append("Uni of Narowal")
        uon_uni=pd.DataFrame(columns=["Uni of Narowal"])
    try:
        driver.get('https://www.uo.edu.pk/programmes')
        uo=[]
        time.sleep(5)
        for page in range(1,42):
                try:
                    value=driver.find_element_by_xpath("/html/body/main/div/div/div["+str(page)+"]/div/div[contains(.,'M')]").text
                    uo.append(value)
                except NoSuchElementException:
                    pass  
        uoo=pd.DataFrame(uo,columns=["Uni of Okara"])
    except:
        error_pun.append("Uni of Okara")
        uoo=pd.DataFrame(columns=["Uni of Okara"])
    try:
        driver.get('https://www.uosahiwal.edu.pk/graduate.php')
        sahi=[]
        time.sleep(5)
        for page in range(1,20):
            try:
                value=driver.find_element_by_xpath("/html/body/div/div[4]/div/div[3]/div/ul/li["+str(page)+"]").text
                sahi.append(value)
            except NoSuchElementException:
                pass  
        sahi_uni=pd.DataFrame(sahi,columns=["University of Sahiwal"])
    except:
        error_pun.append("University of Sahiwal")
        sahi_uni=pd.DataFrame(columns=["University of Sahiwal"])
    try:
        driver.get('https://su.edu.pk/Faculty-of-Agriculture/degrees#bs')
        sar=[]
        time.sleep(5)
        i=1
        while i<2:
            scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
            i+=1
        time.sleep(1)
        for r in range(3,7):
            try:
                for c in range(2,20):
                    try:
                        value= driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div["+str(r)+"]/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div["+str(c)+"]/div[2]").text
                        sar.append(value)                 
                    except NoSuchElementException:           
                        pass
            except NoSuchElementException:           
                pass
        driver.get('https://su.edu.pk/Faculty-of-Social--Sciences/degrees#masters')
        time.sleep(5)
        for r in range(3,7):
            try:
                for c in range(2,20):
                    try:
                        value= driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div["+str(r)+"]/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div["+str(c)+"]/div[2]").text
                        sar.append(value)                 
                    except NoSuchElementException:           
                        pass
            except NoSuchElementException:           
                pass
        driver.get('https://su.edu.pk/Faculty-of-Pharmacy/degrees#ms')
        time.sleep(5)
        for r in range(3,7):
            try:
                for c in range(2,20):
                    try:
                        value= driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div["+str(r)+"]/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div["+str(c)+"]/div[2]").text
                        sar.append(value)                 
                    except NoSuchElementException:           
                        pass
            except NoSuchElementException:           
                pass
        driver.get('https://su.edu.pk/Faculty-of-Arts-&-Humanities/degrees#masters')
        time.sleep(5)
        for r in range(3,7):
            try:
                for c in range(2,20):
                    try:
                        value= driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div["+str(r)+"]/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div["+str(c)+"]/div[2]").text
                        sar.append(value)                 
                    except NoSuchElementException:           
                        pass
            except NoSuchElementException:           
                pass
        driver.get('https://su.edu.pk/Faculty-of-Sciences/degrees#masters')
        time.sleep(5)
        for r in range(3,7):
            try:
                for c in range(2,20):
                    try:
                        value= driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div["+str(r)+"]/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div["+str(c)+"]/div[2]").text
                        sar.append(value)                 
                    except NoSuchElementException:           
                        pass
            except NoSuchElementException:           
                pass
        sar_uni=pd.DataFrame(sar,columns=["University of Sargodha"])
    except:
        error_pun.append("University of Sargodha")
        sar_uni=pd.DataFrame(columns=["University of Sargodha"])
    try:
        driver.get('https://www.uskt.edu.pk/Home/OfferedPrograms')
        sial=[]
        time.sleep(5)
        for r in range(1,7):
            try:
                for c in range(3,9,2):
                    try:
                        for page in range(1,10):
                            try:
                                value=driver.find_element_by_xpath("//*[@id='form1']/div[4]/div/table["+str(r)+"]/tbody/tr["+str(c)+"]/td/table/tbody/tr/td/h6["+str(page)+"]").text
                                sial.append(value)                 
                            except NoSuchElementException:            
                                pass
                    except NoSuchElementException:  
                        pass      
            except NoSuchElementException:  
                pass
        for page in range(1,10):
            try:
                value=driver.find_element_by_xpath("/html/body/form/div[4]/div/table[7]/tbody/tr["+str(page)+"]/td/table/tbody/tr/td/h6/a").text
                sial.append(value)                 
            except NoSuchElementException:            
                pass
        sial_uni=pd.DataFrame(sial,columns=["University of Sialkot"])
    except:
        error_pun.append("University of Sialkot")
        sial_uni=pd.DataFrame(columns=["University of Sialkot"])
    try:
        driver.get('https://usa.edu.pk/graduate-programs')
        usa=[]
        time.sleep(5)
        for page in range(1,20):
            try:
                value=driver.find_element_by_xpath("/html/body/section/div/div/div/div["+str(page)+"]/div/div[2]/h6").text
                usa.append(value)
            except NoSuchElementException:
                pass  
        usa_uni=pd.DataFrame(usa,columns=["University of South Asia"])
    except:
        error_pun.append("University of South Asia")
        usa_uni=pd.DataFrame(columns=["University of South Asia"])
    try:
        driver.get('http://www.uvas.edu.pk/Admissions/postGraduate/mPhil-Phd/index.htm')
        uvas=[]
        time.sleep(5)
        for c in range(1,5,2):
            try:
                for r in range(2,40):
                    try:
                        value=driver.find_element_by_xpath("//*[@id='dp']/tbody/tr[7]/td/table["+str(c)+"]/tbody/tr["+str(r)+"]/td[2]/p").text
                        uvas.append(value)
                    except NoSuchElementException:
                        pass
            except NoSuchElementException:
                        pass
        uvas_uni=pd.DataFrame(uvas,columns=["University of Veterinary & Animal Sciences"])
    except:
        error_pun.append("University of Veterinary & Animal Sciences")
        uvas_uni=pd.DataFrame(columns=["University of Veterinary & Animal Sciences"])
    try:
        driver.get('https://uoj.edu.pk/content/fee-structure/index.html')
        time.sleep(5)
        uj=[]
        for r in range(1,26):
            try:
                value=driver.find_element_by_xpath("//*[@id='wrapper']/div/section[2]/div/div["+str(r)+"]/p").text   
                uj.append(value)
            except NoSuchElementException:
                pass
        uni_jhang=pd.DataFrame(uj,columns=["Uni of Jhang"])
    except:
        error_pun.append("Uni of Jhang")
        uni_jhang=pd.DataFrame(columns=["Uni of Jhang"])
    try:
        driver.get('http://www.uow.edu.pk/admissions/financialaidgrad.aspx')
        uow=[]
        time.sleep(5)
        for r in range(4,30):
            try:
                value=driver.find_element_by_xpath("//*[@id='centercol']/div/ul/li[3]/table/tbody/tr["+str(r)+"]/td[1]").text
                uow.append(value)
            except NoSuchElementException:
                pass  
        uow_uni=pd.DataFrame(uow,columns=["Uni of Wah"])
    except:
        error_pun.append("Uni of Wah")
        uow_uni=pd.DataFrame(columns=["Uni of Wah"])
    try:
        driver.get('http://pu.edu.pk/program/index/masters')
        punj=[]
        time.sleep(5)
        for r in range(1,7):
            for c in range(1,9):
                for h in range(1,10):
                    try:
                        value=driver.find_element_by_xpath("//*[@id='news-blocks']/section/div/div[2]/div/table/tbody/tr["+str(r)+"]/td/table["+str(c)+"]/tbody/tr["+str(h)+"]/td[2]/a/g").text
                        punj.append(value)
                    except NoSuchElementException:
                        pass
        punj_uni=pd.DataFrame(punj,columns=["Uni of Punjab"])
    except:
        error_pun.append("Uni of Punjab")
        punj_uni=pd.DataFrame(columns=["Uni of Punjab"])
    try:
        driver.get('https://www.eduvision.edu.pk/admissions/virtual-university-of-pakistan-lahore-admissions-master-ma-msc-level-844')
        vu=[]
        time.sleep(5)
        action = ActionChains(driver);
        for r in range(39,100):
            try:
                value=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/article/div[1]/div/ul/a["+str(r)+"]/li").text
                vu.append(value) 
            except NoSuchElementException:
                pass
        vu_uni=pd.DataFrame(vu,columns=["Virtual University"])
    except:
        error_pun.append("Virtual University")
        vu_uni=pd.DataFrame(columns=["Virtual University"])
    global pdList_pun
    global pun_df
#     pdList_pun = [ali_uni,bz_uni,bnu_uni,cuvas_uni,fjwu_uni,gswu_uni,fc_uni,gift_uni,
#               ghazi_uni,gcf_uni,gcl_uni,gcwu_uni,gcws_uni,gsc_uni,hitec_uni,hj_uni,
#               itu_uni,ims_uni,isp_uni,isl_uni,kfu_uni,ke_uni,
#               kc_uni,lcwu_uni,lgu_uni,llu_uni,lse_uni,lums_uni,mnsua_uni,mnsuet_uni
#               ,nfc_uni,nca_uni,ncbae_uni,ntu_uni,nis_uni,
#               nur_uni,pifd_uni,pir_uni,rmu_uni,su_uni,tuf_uni,times_uni,uoap_uni
#               ,wum_uni,ucp_uni,uoc_uni,ug_uni,uon_uni,sahi_uni,
#               edu_uni,uetl_uni,uett_uni,uhs_uni,uni_econ,
#               uni_jhang,uol_uni,umt_uni,mian_uni,uoo,uos,sar_uni,sial_uni,usa_uni,uvas_uni,uow_uni,punj_uni,vu_uni]
    pdList_pun=[uow_uni,punj_uni,vu_uni,uni_jhang]
    pun_df=pd.concat(pdList_pun, axis=1)
    print(pun_df)
    eventpun.set()
    event2pun.set()
    event3pun.set()
    event4pun.set()
    event5pun.set()
def sindh_ms():    
    import requests
    import lxml.html as lh
    import pandas as pd
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    try:
        driver.get('https://www.aku.edu/admissions/Pages/graduate.aspx')
        aga=[]
        name=driver.find_elements_by_xpath("/html/body/form/div[9]/div[3]/div/div/div[1]/footer/div/div/div[2]/div/div/div/div/div[1]/div")
        o=name[0].text.split("\n")
        for v in o:
            if (v.startswith('M')):
                aga.append(v)
        aga_uni=pd.DataFrame(aga,columns=["Aga Khan University"])
    except:
        error_sin.append("Aga Khan University")
        aga_uni=pd.DataFrame(columns=["Aga Khan University"])
    try:
        driver.get('https://www.baqai.edu.pk/Results.php')
        time.sleep(3)
        baq=[]
        from selenium.webdriver.common.action_chains import ActionChains
        a = ActionChains(driver)
        m = driver.find_element_by_xpath("/html/body/div[3]/div[1]/header/div/div/header/div[2]/div/nav/ul/li[3]/a")
        a.move_to_element(m).perform()
        courses=driver.find_elements_by_xpath("/html/body/div[3]/div[1]/header/div/div/header/div[2]/div/nav/ul/li[3]/div/div/div[2]/ul[1]/li/a")
        for z in courses:
            if (z.text.startswith('M')):
                baq.append(z.text)
        courses=driver.find_elements_by_xpath("/html/body/div[3]/div[1]/header/div/div/header/div[2]/div/nav/ul/li[3]/div/div/div[3]/ul[2]/li/a")
        for z in courses:
            if (z.text.startswith('M')):
                baq.append(z.text)
        courses=driver.find_elements_by_xpath("/html/body/div[3]/div[1]/header/div/div/header/div[2]/div/nav/ul/li[3]/div/div/div[4]/ul/li/a")
        for z in courses:
            if (z.text.startswith('M')):
                baq.append(z.text)
        baq_uni=pd.DataFrame(baq,columns=["Baqai Medical University"])
    except:
        error_sin.append("Baqai Medical University")
        baq_uni=pd.DataFrame(columns=["Baqai Medical University"])
    try:
        driver.get('https://www.shu.edu.pk/Home/eligibility_criteria')
        bar=[]
        coursees=driver.find_elements_by_xpath("/html/body/div/div[2]/div/div[2]/table/tbody/tr/td[1]")
        for z in coursees:
            if(z.text.startswith('M')):
                bar.append(z.text)
        bar_uni=pd.DataFrame(bar,columns=["Barret Hodgson University"])
    except:
        error_sin.append("Barret Hodgson University")
        bar_uni=pd.DataFrame(columns=["Barret Hodgson University"])
    try:
        driver.get('https://bbsul.edu.pk/admission_e.php')
        bbsul=[]
        course=driver.find_elements_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[1]/ul/li")
        for z in course:
            if(z.text.startswith('M')):
                bbsul(z.text)
        bbsul_uni=pd.DataFrame(bbsul,columns=["Benazir Bhutto Shaheed University Lyari"])
    except:
        error_sin.append("Benazir Bhutto Shaheed University Lyari")
        bbsul_uni=pd.DataFrame(columns=["Benazir Bhutto Shaheed University Lyari"])
    try:
        driver.get('https://www.eduvision.edu.pk/commeces-institute-of-business-emerging-sciences-commecs-karachi-ins-1421314762')
        com=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            com.append(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            com.append(a.text)
        com_uni=pd.DataFrame(com,columns=[" Commecs Institute of Business & Emerging Sciences"])
    except:
        error_sin.append(" Commecs Institute of Business & Emerging Sciences")
        com_uni=pd.DataFrame(columns=[" Commecs Institute of Business & Emerging Sciences"])
    try:
        driver.get('https://www.eduvision.edu.pk/dha-suffa-universitymain-campus-dsu-karachi-ins-1322850088')
        dha=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            dha.append(a.text)
        dha_uni=pd.DataFrame(dha,columns=[" DHA Suffa University"])
    except:
        error_sin.append(" DHA Suffa University")
        dha_uni=pd.DataFrame(columns=[" DHA Suffa University"])
    try:
        driver.get('https://www.duhs.edu.pk/new/postgraduate/')
        dow=[]
        driver.execute_script("window.scrollTo(0, 500)") 
        course=driver.find_elements_by_xpath("/html/body/div[3]/div/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div/h3")
        for z in course:
            if(z.text.startswith('M')):
                dow.append(z.text)
        course=driver.find_elements_by_xpath("/html/body/div[3]/div/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div/h3")
        for z in course:
            if(z.text.startswith('M')):
                dow.append(z.text)
        dow_uni=pd.DataFrame(dow,columns=["DOW University of Health Sciences"])
    except:
        error_sin.append("DOW University of Health Sciences")
        dow_uni=pd.DataFrame(columns=["DOW University of Health Sciences"])
    try:
        driver.get('https://www.eduvision.edu.pk/dadabhoy-institute-of-higher-education-dihe-karachi-ins-874')
        dad=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            dad.append(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            dad.append(a.text)
        dad_uni=pd.DataFrame(dad,columns=["Dadabhoy Institute of Higher Education"])
    except:
        error_sin.append("Dadabhoy Institute of Higher Education")
        dad_uni=pd.DataFrame(columns=["Dadabhoy Institute of Higher Education"])
    try:
        driver.get('https://www.eduvision.edu.pk/dawood-university-of-engineering-and-technology-duet-karachi-ins-619')
        daw=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name: 
            daw.append(a.text)
        daw_uni=pd.DataFrame(daw,columns=["Dawood University of Engineering & Technology"])
    except:
        error_sin.append("Dawood University of Engineering & Technology")
        daw_uni=pd.DataFrame(columns=["Dawood University of Engineering & Technology"])
    try:
        driver.get('https://www.greenwich.edu.pk/Home/GraduateCourses')
        green=[]
        courses=driver.find_elements_by_xpath("/html/body/section/div/div/div/div/div/h4/a")
        for z in courses:
            green.append(z.text)
        driver.get('https://www.greenwich.edu.pk/Home/MPhilCourses')
        courses=driver.find_elements_by_xpath("/html/body/section/div/div/div/div/div/h4")
        for z in courses:
            green.append(z.text)
        green_uni=pd.DataFrame(green,columns=["Greenwich University"])
    except:
        error_sin.append("Greenwich University")
        green_uni=pd.DataFrame(columns=["Greenwich University"])
    try:
        driver.get('https://ilmauniversity.edu.pk/pgap')
        ilm=[]
        course=driver.find_elements_by_xpath("/html/body/div[1]/div[2]/section/div/div/div/div/article/div/div/div/table/tbody/tr/td/p")
        for z in course:
            if(z.text.startswith('M')):
                ilm.append(z.text)
        ilm_uni=pd.DataFrame(ilm,columns=["ILMA University"])
    except:
        error_sin.append("ILMA University")
        ilm_uni=pd.DataFrame(columns=["ILMA University"])
    try:
        driver.get('http://www.indusvalley.edu.pk/web/graduate/')
        ind=[]
        unilist=driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/nav/ul[1]/li[2]/ul/li[2]/ul/li/a")
        for a in unilist:
            result4 = a.text.startswith('M')
            if   (result4):
                if(a.text):
                    ind.append(a.text)
        ind_uni=pd.DataFrame(ind,columns=["Indus Valley School of Art & Architecture"]) 
    except:
        error_sin.append("Indus Valley School of Art & Architecture")
        ind_uni=pd.DataFrame(columns=["Indus Valley School of Art & Architecture"]) 
    try:
        driver.get('http://www.indus.edu.pk/graduate%20programs.html')
        indus=[]
        rows=driver.find_elements_by_xpath("/html/body/div[5]/div/div[1]/article/div/div[2]/table/tbody/tr/td[1]/a")
        for a in rows:
            indus.append(a.text)
        indus_uni=pd.DataFrame(indus,columns=["Indus University"]) 
    except:
        error_sin.append("Indus University")
        indus_uni=pd.DataFrame(columns=["Indus University"]) 
    try:
        driver.get('https://www.iba.edu.pk/graduate.php')
        iba=[]
        rows=len(driver.find_elements_by_xpath("/html/body/div[2]/div/div[1]/div/ul[2]/li/a/span"))
        for t in range (1,rows+1):
            vah=driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/ul[2]/li["+str(t)+"]/a/span").text
            iba.append(vah)
        iba_uni=pd.DataFrame(iba,columns=["Institute of Business Administration"])
    except:
        error_sin.append("Institute of Business Administration")
        iba_uni=pd.DataFrame(columns=["Institute of Business Administration"])
    try:
        driver.get('https://www.iobm.edu.pk/academic-programs-search/')
        courses=driver.find_elements_by_xpath("/html/body/div[3]/div/div[4]/div[2]/div/div[1]/div/div/div/h3")
        for z in courses:
            if(z.text.startswith('M')):
                ibm.append(z.text)
        courses=driver.find_elements_by_xpath("/html/body/div[3]/div/div[4]/div[2]/div/div[1]/div/div/div/h3")
        for z in courses:
            if(z.text.startswith('M')):
                ibm.append(z.text)
        driver.get('https://www.iobm.edu.pk/academic-programs-search/page/2/')
        courses=driver.find_elements_by_xpath("/html/body/div[3]/div/div[4]/div[2]/div/div[1]/div/div/div/h3")
        for z in courses:
            if(z.text.startswith('M')):
                ibm.append(z.text)
        courses=driver.find_elements_by_xpath("/html/body/div[3]/div/div[4]/div[2]/div/div[1]/div/div/div/h3")
        for z in courses:
            if(z.text.startswith('M')):
                ibm.append(z.text)
        driver.get('https://www.iobm.edu.pk/academic-programs-search/page/3/')
        courses=driver.find_elements_by_xpath("/html/body/div[3]/div/div[4]/div[2]/div/div[1]/div/div/div/h3")
        for z in courses:
            if(z.text.startswith('M')):
                ibm.append(z.text)
        courses=driver.find_elements_by_xpath("/html/body/div[3]/div/div[4]/div[2]/div/div[1]/div/div/div/h3")
        for z in courses:
            if(z.text.startswith('M')):
                ibm.append(z.text)
        ibm_uni=pd.DataFrame(ibm,columns=["Institute of Business Administration"])
    except:
        error_sin.append("Institute of Business Administration")
        ibm_uni=pd.DataFrame(columns=["Institute of Business Administration"])
    try:
        driver.get('https://isra.edu.pk/study-programss/')
        isra=[]
        programs=len(driver.find_elements_by_xpath("/html/body/div/div[1]/div/div/section/div/section/article/section/div/div[2]/div/div/table[1]/tbody/tr[1]/td[1]"))
        try:
            for t in range (1,programs+1):
                vah=driver.find_element_by_xpath("/html/body/div/div[1]/div/div/section/div/section/article/section/div/div[1]/span["+str(t)+"]/strong")
                vah.click()
                time.sleep(5)
                noofdiv=len(driver.find_elements_by_xpath("/html/body/div/div[1]/div/div/section/div/section/article/section/div/div[2]/div["+str(t)+"]/div/table[1]/tbody/tr[1]/td[1]"))
                for a in range(1,noofdiv+1):
                    nooftable=len(driver.find_elements_by_xpath("/html/body/div/div[1]/div/div/section/div/section/article/section/div/div[2]/div["+str(t)+"]/div["+str(a)+"]/table/tbody/tr[1]/td[1]"))
                    for b in range (1,nooftable+1):
                        norow=len(driver.find_elements_by_xpath("/html/body/div/div[1]/div/div/section/div/section/article/section/div/div[2]/div["+str(t)+"]/div["+str(a)+"]/table["+str(b)+"]/tbody/tr/td[1]"))
                        for c in range (1,norow+1):
                            for d in range(1,3):
                                value=driver.find_element_by_xpath("/html/body/div/div[1]/div/div/section/div/section/article/section/div/div[2]/div["+str(t)+"]/div["+str(a)+"]/table["+str(b)+"]/tbody/tr["+str(c)+"]/td["+str(d)+"]").text                        
                                isra.append(value)
        except NoSuchElementException: 
            pass
        isra_uni=pd.DataFrame(isra,columns=["Isra University"])
    except:
        error_sin.append("Isra University")
        isra_uni=pd.DataFrame(columns=["Isra University"])
    try:
        driver.get('http://www.jsmu.edu.pk/admission-programs-offered.html')
        jsmu=[]
        program=len(driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/div/div[2]/ul/li/ul/li/div/i"))
        for t in range (1,program+1):
            vah=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/div/div[2]/ul/li["+str(t)+"]/ul/li/div/i")
            vah.click()
            time.sleep(5)
            vah=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/div/div[2]/ul/li["+str(t)+"]/ul/li/ul/li[1]/a")
            vah.click()
            time.sleep(5)
            try:
                z=len(driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[1]/h4/a"))
                for h in range (1,z+1):
                    value=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div["+str(h)+"]/div[1]/h4/a").text
                    if (value.startswith('M')):
                        jsmu.append(value)
            except:
                print ("no attribute 'a'")
                driver.back()
                continue
            driver.back() 
        jsmu_uni=pd.DataFrame(jsmu,columns=["Jinnah Sindh Medical University"]) 
    except:
        error_sin.append("Jinnah Sindh Medical University")
        jsmu_uni=pd.DataFrame(columns=["Jinnah Sindh Medical University"]) 
    try:
        driver.get('https://www.eduvision.edu.pk/jinnah-university-for-women-juw-karachi-ins-57')
        juw=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            juw.append(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            juw.append(a.text)
        juw_uni=pd.DataFrame(juw,columns=["Jinnah University for Women"]) 
    except:
        error_sin.append("Jinnah University for Women")
        juw_uni=pd.DataFrame(columns=["Jinnah University for Women"]) 
    try:
        driver.get('http://kasbit.edu.pk/')
        kasb=[]
        programs=driver.find_element_by_xpath("/html/body/header/div[2]/div/div/div/nav/div/div[2]/ul/li[3]/a")
        undergrad=driver.find_element_by_xpath("/html/body/header/div[2]/div/div/div/nav/div/div[2]/ul/li[3]/ul/li[3]/a")
        hover=ActionChains(driver).move_to_element(programs)
        hover.perform()
        hover=ActionChains(driver).move_to_element(undergrad)
        hover.perform()
        name=driver.find_elements_by_xpath("/html/body/header/div[2]/div/div/div/nav/div/div[2]/ul/li[3]/ul/li[3]/ul/li/a")
        for a in name:
            kasb.append(a.text)
        kasb_uni=pd.DataFrame(kasb,columns=["KASB Institute of Technology"]) 
    except:
        error_sin.append("KASB Institute of Technology")
        kasb_uni=pd.DataFrame(columns=["KASB Institute of Technology"]) 
    try:
        driver.get('https://www.eduvision.edu.pk/karachi-institute-of-economics-technology-kiet-karachi-ins-58')
        kiet=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            kiet.append(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            kiet.append(a.text)
        kiet_uni=pd.DataFrame(kiet,columns=["Karachi Institute of Economics & Technology"]) 
    except:
        error_sin.append("Karachi Institute of Economics & Technology")
        kiet_uni=pd.DataFrame(columns=["Karachi Institute of Economics & Technology"]) 
    try:
        driver.get('http://www.ksbl.edu.pk/')
        ksbl=[]
        value=driver.find_elements_by_xpath("/html/body/header/div[3]/div[2]/div/div/a/h4")
        for a in value:
            ksbl.append(a.text)
        ksbl_uni=pd.DataFrame(ksbl,columns=["Karachi School for Business & Leadership"]) 
    except:
        error_sin.append("Karachi School for Business & Leadership")
        ksbl_uni=pd.DataFrame(columns=["Karachi School for Business & Leadership"])
    try:
        driver.get('https://www.eduvision.edu.pk/liaquat-university-of-medical-and-health-sciences-lumhs-jamshoro-ins-19')
        lumh=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            lumh.append(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            lumh.append(a.text)
        lumh_uni=pd.DataFrame(lumh,columns=["Liaquat University of Medical & Health Sciences"]) 
    except:
        error_sin.append("Liaquat University of Medical & Health Sciences")
        lumh_uni=pd.DataFrame(columns=["Liaquat University of Medical & Health Sciences"]) 
    try:
        driver.get('https://www.eduvision.edu.pk/mehran-university-of-engineering-technology-muet-jamshoro-ins-20')
        muet=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            muet.append(a.text)
        muet_uni=pd.DataFrame(muet,columns=["Mehran University of Engineering & Technology"]) 
    except:
        error_sin.append("Mehran University of Engineering & Technology")
        muet_uni=pd.DataFrame(columns=["Mehran University of Engineering & Technology"]) 
    try:
        driver.get('https://www.eduvision.edu.pk/muhammad-ali-jinnah-university-maju-karachi-ins-63')
        maju=[]
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            maju(a.text)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]").click()
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            maju(a.text)
        maju_uni=pd.DataFrame(maju,columns=["Mohammad Ali Jinnah University"]) 
    except:
        error_sin.append("Mohammad Ali Jinnah University")
        maju_uni=pd.DataFrame(columns=["Mohammad Ali Jinnah University"]) 
    try:
        driver.get('https://www.eduvision.edu.pk/ned-university-of-engineering-technology-neduet-karachi-ins-631')
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]").click()
        ned=[]
        name=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/a[1]")
        for a in name:
            ned.append(a.text)
        ned_uni=pd.DataFrame(ned,columns=["NED University of Engineering & Technology"])
    except:
        error_sin.append("NED University of Engineering & Technology")
        ned_uni=pd.DataFrame(columns=["NED University of Engineering & Technology"])
    try:
        driver.get('https://www.eduvision.edu.pk/newports-institute-of-communications-and-economics-newports-karachi-ins-783')
        new=[]
        time.sleep(5)
        button=driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]")
        button.click()
        time.sleep(1)
        for r in range(1,76):
            try:
                value=driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                new.append(value) 
            except NoSuchElementException:
                pass
        new_uni=pd.DataFrame(new,columns=["Newport Institute of Communications & Economics"])
    except:
        error_sin.append("Newport Institute of Communications & Economics")
        new_uni=pd.DataFrame(columns=["Newport Institute of Communications & Economics"])
    try:
        driver.get('https://pumhs.edu.pk/postgraduate.html')
        pumhs=[]
        time.sleep(5)
        for c in range(5,15):
            try:
                for r in range(1,20):
                    try:
                        value= driver.find_element_by_xpath("/html/body/div/div["+str(c)+"]/div/div/table/tbody/tr["+str(r)+"]/td[1]/div/div/font[1]").text
                        pumhs.append(value)                  
                    except NoSuchElementException:
                        pass
            except NoSuchElementException:
                pass
        pumhs_uni=pd.DataFrame(pumhs,columns=["Peoples University of Medical & Health Sciences for Women"])
    except:
        error_sin.append("Peoples University of Medical & Health Sciences for Women")
        pumhs_uni=pd.DataFrame(columns=["Peoples University of Medical & Health Sciences for Women"])
    try:
        driver.get('http://www.preston.edu.pk/courses.php')
        pre=[]
        time.sleep(5)
        action = ActionChains(driver);
        for c in range(1,8):
            try:
                parent_level_menu = driver.find_element_by_xpath("//*[@id='nav']/ul/li[2]/a")
                action.move_to_element(parent_level_menu).perform()
                parent_level_menu = driver.find_element_by_xpath("//*[@id='nav']/ul/li[2]/ul/v/v["+str(c)+"]/li/a")
                action.move_to_element(parent_level_menu).perform() 
                for r in range(1,30):
                    try:
                        value=driver.find_element_by_xpath("//*[@id='nav']/ul/li[2]/ul/v/v["+str(c)+"]/li/ul/n["+str(r)+"]/li/a").text
                        pre.append(value) 
                    except NoSuchElementException: 
                        pass
            except NoSuchElementException:
                pass
        parent_level_menu = driver.find_element_by_xpath("//*[@id='nav']/ul/li[2]/ul/v/li/a")
        action.move_to_element(parent_level_menu).perform() 
        value=driver.find_element_by_xpath("//*[@id='nav']/ul/li[2]/ul/v/li/ul/li/a").text
        pre.append(value) 
        pre_uni=pd.DataFrame(pre,columns=["Preston Uni Karachi"])
    except:
        error_sin.append("Preston Uni Karachi")
        pre_uni=pd.DataFrame(columns=["Preston Uni Karachi"])
    try:
        driver.get('https://quest.edu.pk/programmes/postgraduate.php')
        quest=[]
        time.sleep(5)
        for r in range(1,76):
            try:
                value=driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td/div/table/tbody/tr[1]/td[2]/table[1]/tbody/tr[2]/td/div/ul/li["+str(r)+"]").text
                quest.append(value) 
            except NoSuchElementException:
                pass
        for r in range(1,76):
            try:
                value=driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td/div/table/tbody/tr[1]/td[2]/ul/li["+str(r)+"]").text
                quest.append(value) 
            except NoSuchElementException:
                pass
        quest_uni=pd.DataFrame(quest,columns=["Quaid-e-Awam University of Engineering, Sciences & Technology"])
    except:
        error_sin.append("Quaid-e-Awam University of Engineering, Sciences & Technology")
        quest_uni=pd.DataFrame(columns=["Quaid-e-Awam University of Engineering, Sciences & Technology"])
    try:
        driver.get('https://www.eduvision.edu.pk/shah-abdul-latif-university-salu-khair-pur-ins-32')
        time.sleep(5)
        action = ActionChains(driver);
        button=driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]")
        button.click()
        sal=[]
        time.sleep(1)
        for r in range(1,30):
            try:
                value=driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                sal.append(value) 
            except NoSuchElementException:
                pass
        sal_uni=pd.DataFrame(sal,columns=["Shah Abdul Latif"])
    except:
        error_sin.append("Shah Abdul Latif")
        sal_uni=pd.DataFrame(columns=["Shah Abdul Latif"])
    try:
        driver.get('https://www.eduvision.edu.pk/shaheed-benazir-bhutto-city-university-sbbcu-karachi-ins-1469672414')
        ssbcu=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]')
        button.click()
        for r in range(1,12):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                ssbcu.append(value)
            except NoSuchElementException:
                pass
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]')
        button.click()
        for r in range(1,12):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                ssbcu.append(value)
            except NoSuchElementException:
                pass
        ssbcu_uni=pd.DataFrame(ssbcu,columns=["Shaheed Benazir Bhutto City University"])
    except:
        error_sin.append("Shaheed Benazir Bhutto City University")
        ssbcu_uni=pd.DataFrame(columns=["Shaheed Benazir Bhutto City University"])
    try:
        driver.get('https://www.ilmkidunya.com/colleges/shaheed-benazir-bhutto-dewan-university-karachi-courses.aspx')
        time.sleep(5)
        action = ActionChains(driver);
        sbbdu=[]
        for r in range(1,30):
            try:
                value=driver.find_element_by_xpath("//*[@id='form1']/div[2]/div[1]/div[3]/div/div/div/div/div[3]/div[1]/div/div[4]/div[4]/div/table/tbody/tr["+str(r)+"]/td[1]").text
                sbbdu.append(value) 
            except NoSuchElementException:
                pass
        sbbdu_uni=pd.DataFrame(sbbdu,columns=["Shaheed Benazir Bhutto Dewan University"])
    except:
        error_sin.append("Shaheed Benazir Bhutto Dewan University")
        sbbdu_uni=pd.DataFrame(columns=["Shaheed Benazir Bhutto Dewan University"])
    try:
        driver.get('https://www.sbbusba.edu.pk/sbbu-main/graduate-programs.html')
        ssbusb=[]
        time.sleep(5)
        for r in range(2,7):
            try:
                value=driver.find_element_by_xpath("//*[@id='Section1']/div[2]/div/h5["+str(r)+"]").text
                ssbusb.append(value)
            except NoSuchElementException:
                pass
        ssbusb_uni=pd.DataFrame(ssbusb,columns=["Shaheed Benazir Bhutto University, Shaheed Benazirabad"])
    except:
        error_sin.append("Shaheed Benazir Bhutto University, Shaheed Benazirabad")
        ssbusb_uni=pd.DataFrame(columns=["Shaheed Benazir Bhutto University, Shaheed Benazirabad"])
    try:
        driver.get('https://www.smbbmu.edu.pk/beta/admissions/post-graduate#admission-policy')
        smbbmu=[]
        time.sleep(5)
        for q in range(1,3):
            for c in range(1,20):
                try:
                    for r in range(1,20):
                        try:
                            value= driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div/div["+str(q)+"]/ul["+str(c)+"]/li["+str(r)+"]").text
                            smbbmu.append(value)                  
                        except NoSuchElementException:
                            pass
                except NoSuchElementException:
                    pass
        smbbmu_uni=pd.DataFrame(smbbmu,columns=["Shaheed Mohtarma Benazir Bhutto Medical University"])
    except:
        error_sin.append("Shaheed Mohtarma Benazir Bhutto Medical University")
        smbbmu_uni=pd.DataFrame(columns=["Shaheed Mohtarma Benazir Bhutto Medical University"])
    try:
        driver.get('https://szabist.edu.pk/programs/')
        szabist=[]
        time.sleep(5)
        for r in range(1,20):
            try:
                value= driver.find_element_by_xpath("//*[@id='kingster-page-wrapper']/div[1]/div/div/div[5]/div/div["+str(r)+"]/div[2]/h4").text
                szabist.append(value)                 
            except NoSuchElementException:
                pass
        for r in range(2,20):
            try:
                value= driver.find_element_by_xpath("//*[@id='kingster-page-wrapper']/div[1]/div/div/div[8]/div/div["+str(r)+"]/div[2]/h4").text
                szabist.append(value)                 
            except NoSuchElementException:
                pass
        szabist_uni=pd.DataFrame(szabist,columns=["Shaheed Zulfikar Ali Bhutto Institute of Science & Technology"])
    except:
        error_sin.append("Shaheed Zulfikar Ali Bhutto Institute of Science & Technology")
        szabist_uni=pd.DataFrame(columns=["Shaheed Zulfikar Ali Bhutto Institute of Science & Technology"])
    try:
        driver.get('https://www.szabul.edu.pk/fee.php#')
        szal=[]
        time.sleep(5)
        for r in range(1,66):
            try:
                value=driver.find_element_by_xpath("//*[@id='div_983a_3']/div[2]/div/div[1]/div/div/div[1]/table/tbody/tr["+str(r)+"]/td/a").text
                szal.append(value)
            except NoSuchElementException:
                pass
        szal_uni=pd.DataFrame(szal,columns=["Shaheed Zulfiqar Ali Bhutto University of Law"])
    except:
        error_sin.append("Shaheed Zulfiqar Ali Bhutto University of Law")
        szal_uni=pd.DataFrame(columns=["Shaheed Zulfiqar Ali Bhutto University of Law"])
    try:
        driver.get('https://www.eduvision.edu.pk/sindh-agriculture-university-sau-tando-jam-ins-33')
        tanj=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]')
        button.click()
        for r in range(1,12):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                tanj.append(value)
            except NoSuchElementException:
                pass
        tanj_uni=pd.DataFrame(tanj,columns=["Sindh Agriculture Tanjodam"])
    except:
        error_sin.append("Sindh Agriculture Tanjodam")
        tanj_uni=pd.DataFrame(columns=["Sindh Agriculture Tanjodam"])
    try:
        driver.get('https://www.ssuet.edu.pk/')
        ssuet=[]
        time.sleep(5)
        action = ActionChains(driver);
        parent_level_menu = driver.find_element_by_xpath("//*[@id='jet-menu-item-4140']/a/div")
        action.move_to_element(parent_level_menu).perform()
        time.sleep(5)
        for r in range(2,44):
            try:
                value=driver.find_element_by_xpath("//*[@id='jet-menu-item-4140']/div/div/div/div/section/div[2]/div/div[1]/div/div/div[2]/div/ul/li["+str(r)+"]/a/span[2]").text
                ssuet.append(value) 
            except NoSuchElementException:
                pass
        for c in range(1,44):
            try:
                value=driver.find_element_by_xpath("//*[@id='jet-menu-item-4140']/div/div/div/div/section/div[2]/div/div[2]/div/div/div[2]/div/ul/li["+str(c)+"]/a/span[2]").text
                ssuet.append(value) 
            except NoSuchElementException:
                pass
        value=driver.find_element_by_xpath("//*[@id='jet-menu-item-4140']/div/div/div/div/section/div[2]/div/div[2]/div/div/div[4]/div/ul/li/a/span[2]").text
        ssuet.append(value)   
        ssuet_uni=pd.DataFrame(ssuet,columns=["Sir Syed Uni of E & T"])
    except:
        error_sin.append("Sir Syed Uni of E & T")
        ssuet_uni=pd.DataFrame(columns=["Sir Syed Uni of E & T"])
    try:
        driver.get('https://www.smiu.edu.pk/admissions/graduate-programs')
        smiu=[]
        time.sleep(5)
        for c in range(1,13):
            for r in range(1,66):
                try:
                    value=driver.find_element_by_xpath("/html/body/div[3]/section[2]/div/div/div[1]/article/div/div["+str(c)+"]/div[2]/ul/li["+str(r)+"]/a").text
                    smiu.append(value)                 
                except NoSuchElementException:
                    pass
        driver.get('https://www.smiu.edu.pk/admissions/Postgraduate-Programs')
        time.sleep(5)
        value=driver.find_element_by_xpath("/html/body/div[3]/section[2]/div/div/div[1]/article/div/div[1]/h6").text
        smiu.append(value)                 
        value1=driver.find_element_by_xpath("/html/body/div[3]/section[2]/div/div/div[1]/article/div/div[2]/h6").text
        smiu.append(value)
        value2=driver.find_element_by_xpath("/html/body/div[3]/section[2]/div/div/div[1]/article/div/div[2]/div[3]/h6").text
        smiu.append(value)   
        smiu_uni=pd.DataFrame(smiu,columns=["Sindh Madresatul Islam University"])
    except:
        error_sin.append("Sindh Madresatul Islam University")
        smiu_uni=pd.DataFrame(columns=["Sindh Madresatul Islam University"])
    try:
        driver.get('https://www.iba-suk.edu.pk/admissions/graduate-programs')
        siba=[]
        time.sleep(5)
        for r in range(1,66):
            try:
                value=driver.find_element_by_xpath("//*[@id='course-list']/div/table/tbody/tr["+str(r)+"]/th[1]/a").text
                siba.append(value) 
            except NoSuchElementException:
                pass
        driver.get('https://www.iba-suk.edu.pk/admissions/post-graduate-programs')
        time.sleep(5)
        for r in range(1,66):
            try:
                value=driver.find_element_by_xpath("//*[@id='course-list']/div/table/tbody/tr["+str(r)+"]/td[1]").text
                siba.append(value) 
            except NoSuchElementException:
                pass
        siba_uni=pd.DataFrame(siba,columns=["Sukkur Institute of Business Administration"])
    except:
        error_sin.append("Sukkur Institute of Business Administration")
        siba_uni=pd.DataFrame(columns=["Sukkur Institute of Business Administration"])
    try:
        driver.get('https://www.eduvision.edu.pk/university-of-karachi-uok-karachi-ins-40')
        kar=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[2]')
        button.click()
        for r in range(1,60):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                kar.append(value)                   
            except NoSuchElementException:
                pass
        kar_uni=pd.DataFrame(kar,columns=["University of Karachi"])
    except:
        error_sin.append("University of Karachi")
        kar_uni=pd.DataFrame(columns=["University of Karachi"])
    try:
        driver.get('https://www.eduvision.edu.pk/university-of-sindh-uos-jamshoro-ins-44')
        sindh=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]')
        button.click()
        for r in range(1,60):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                sindh.append(value)                   
            except NoSuchElementException:
                pass
        sindh_uni=pd.DataFrame(sindh,columns=["University of Sindh"])
    except:
        error_sin.append("University of Sindh")
        sindh_uni=pd.DataFrame(columns=["University of Sindh"])
    try:
        driver.get('https://www.eduvision.edu.pk/zia-ud-din-medical-university-zmu-karachi-ins-71')
        zia=[]
        time.sleep(5)
        button=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[3]/div/div[2]/div[3]/div/label[3]')
        button.click()
        for r in range(1,60):
            try:
                value= driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[3]/div/div[2]/div[3]/div/div[3]/table/tbody/tr["+str(r)+"]/td[1]/a[1]").text
                zia.append(value)                   
            except NoSuchElementException:
                pass
        zia_uni=pd.DataFrame(zia,columns=["Ziauddin Universty"])
    except:
        error_sin.append("Ziauddin Universty")
        zia_uni=pd.DataFrame(columns=["Ziauddin Universty"])
    global pdList_sin
    global sin_df
#     pdList_sin=[aga_uni,baq_uni,bar_uni,bbsul_uni,com_uni,dha_uni,
#             dow_uni,dad_uni,daw_uni,green_uni,ilm_uni,ind_uni,
#             indus_uni,iba_uni,ibm_uni,isra_uni,jsmu_uni,juw_uni,
#             kasb_uni,kiet_uni,ksbl_uni,lumh_uni,muet_uni,maju_uni,
#             ned_uni,new_uni,pumhs_uni,pre_uni,quest_uni,sal_uni,
#             ssbcu_uni,sbbdu_uni,ssbusb_uni,smbbmu_uni,
#             szabist_uni,szal_uni,tanj_uni,ssuet_uni,smiu_uni,siba_uni,kar_uni,sindh_uni,zia_uni]
    pdList_sin=[kar_uni,sindh_uni,zia_uni]
    sin_df=pd.concat(pdList_sin, axis=1)
    print(sin_df)
    eventsin.set()
    event2sin.set()
    event3sin.set()
    event4sin.set()
    event5sin.set()
from PIL import Image, ImageTk
def show_frame(frame):
    frame.tkraise()
window=tkinter.Tk()
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)
frame_sel_pro=tkinter.Frame(window)
frame1=tkinter.Frame(window)
frame2=tkinter.Frame(window)
frame3=tkinter.Frame(window)
frame4=tkinter.Frame(window)
frame5=tkinter.Frame(window)
frame2bal=tkinter.Frame(window)
frame3bal=tkinter.Frame(window)
frame4bal=tkinter.Frame(window)
frame5bal=tkinter.Frame(window)
frame2isb=tkinter.Frame(window)
frame3isb=tkinter.Frame(window)
frame4isb=tkinter.Frame(window)
frame5isb=tkinter.Frame(window)
frame2kpk=tkinter.Frame(window)
frame3kpk=tkinter.Frame(window)
frame4kpk=tkinter.Frame(window)
frame5kpk=tkinter.Frame(window)
frame2pun=tkinter.Frame(window)
frame3pun=tkinter.Frame(window)
frame4pun=tkinter.Frame(window)
frame5pun=tkinter.Frame(window)
frame2sin=tkinter.Frame(window)
frame3sin=tkinter.Frame(window)
frame4sin=tkinter.Frame(window)
frame5sin=tkinter.Frame(window)
for frame in(frame1,frame2,frame3,frame4,frame5,frame_sel_pro,frame2bal,frame3bal,frame4bal,frame5bal,
             frame2isb,frame3isb,frame4isb,frame5isb,frame2kpk,frame3kpk,frame4kpk,frame5kpk,frame2pun,frame3pun,frame4pun,frame5pun,frame2sin,frame3sin,frame4sin,frame5sin):
    frame.grid(row=0,column=0,sticky="nsew")
#========================================= first page code
bg = Image.open(r'D:\sabz\minarssss.png')
bg = bg.resize((140, 320), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(bg)
bg_label = tkinter.Label(frame1,image=bg)
bg_label.image=bg
bgg=bg_label.grid(row=0,column=0)
#logo = Image.open(r'D:\sabz\fk.png')
#logo = logo.resize((45, 45), Image.ANTIALIAS)
#logo = ImageTk.PhotoImage(logo)
#logo_label = tkinter.Label(frame1,image=logo)
#logo_label.image=logo
#logo_label.place(in_=bgg,x=75,y=17)
instructions=tkinter.Label(frame1,text="Welcome to Parh Pakistan's Web Scrapper 1.0",font=("Arial Bold",12),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=160,y=19)
note=tkinter.Label(frame1,text="This setup will guide you through the process of starting\nthe scrapper.",font=("Arial",10),justify="left")
note.grid(row=1,column=1)
note.place(x=160,y=59)
note2=tkinter.Label(frame1,text="It is recommended that you close all other applications\nbefore starting the scrapper. This will make it possible to\nupdate relevant system files without having to reboot\nyour system.",font=("Arial",10),justify="left")
note2.grid(row=2,column=1)
note2.place(x=160,y=109)
note3=tkinter.Label(frame1,text="Click Next to continue.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=160,y=199)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370')
scrap=tkinter.Button(frame1,text="Next",command=lambda:show_frame(frame_sel_pro),fg="white",bg="#202c34",font="Raleway 10",padx=20,pady=-10)
scrap.grid(row=4,column=1)
scrap.place(x=300,y=327)
cancel=tkinter.Button(frame1,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 10",padx=12,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)
#============================================= select province
line=Canvas(frame_sel_pro,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame_sel_pro,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
instructions=tkinter.Label(frame_sel_pro,text="Select one of the Provinces.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=8)
note=tkinter.Label(frame_sel_pro,text="This is will scrap the universities for the selected province.",font=("Arial",9),justify="left")
note.grid(row=1,column=1)
note.place(x=10,y=32)
kashmir=PhotoImage(file=r'D:\sabz\kash2.png')
baloch=PhotoImage(file=r'D:\sabz\bal.png')
kpk=PhotoImage(file=r'D:\sabz\kpk.png')
lahore=PhotoImage(file=r'D:\sabz\pun.png')
sindh=PhotoImage(file=r'D:\sabz\sindh.png')
isb=PhotoImage(file=r'D:\sabz\isb.png')
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370') 
scrap=tkinter.Button(frame_sel_pro,image=kashmir,command=lambda:show_frame(frame5),border=0,)
scrap.grid(row=3,column=1)
scrap.place(x=20,y=90)
scrap1=tkinter.Button(frame_sel_pro,image=baloch,command=lambda:show_frame(frame5bal),border=0,)
scrap1.grid(row=3,column=1)
scrap1.place(x=20,y=170)
scrap2=tkinter.Button(frame_sel_pro,image=kpk,command=lambda:show_frame(frame5kpk),border=0,)
scrap2.grid(row=3,column=1)
scrap2.place(x=20,y=250)
scrap3=tkinter.Button(frame_sel_pro,image=lahore,command=lambda:show_frame(frame5pun),border=0,)
scrap3.grid(row=3,column=1)
scrap3.place(x=300,y=90)
scrap4=tkinter.Button(frame_sel_pro,image=sindh,command=lambda:show_frame(frame5sin),border=0,)
scrap4.grid(row=3,column=1)
scrap4.place(x=300,y=170)
scrap5=tkinter.Button(frame_sel_pro,image=isb,command=lambda:show_frame(frame5isb),border=0,)
scrap5.grid(row=3,column=1)
scrap5.place(x=300,y=250)
cancel=tkinter.Button(frame_sel_pro,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=9,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=430,y=327)
#==========================================  save page
def save():
    data = [('All types(.)', '.')]
    global x
    x = asksaveasfile(filetypes = data, defaultextension = data)
    listnew.insert(0,x.name)
def write():
    event4.wait()
    global writer
    writer = pd.ExcelWriter(x.name,engine='xlsxwriter')
def df():
    event5.wait()
    ajk_df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
write_thread=threading.Thread(target=write)
write_thread.start()
df_thread=threading.Thread(target=df)
df_thread.start()
line=Canvas(frame5,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame5,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
instructions=tkinter.Label(frame5,text="Select insallation folder.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=8)
note=tkinter.Label(frame5,text="This is the folder where the scrapped data will be saved.",font=("Arial",9),justify="left")
note.grid(row=1,column=1)
note.place(x=10,y=32)
listnew=tkinter.Listbox(frame5,width=53,height=1 ,bd=1)
listnew.grid(row=1,column=0)
listnew.place(x=53,y=155)
listnew.insert(0,"")
save=tkinter.Button(frame5,text="Browse",command=save,fg="white",bg="#202c34",font="Raleway 10",padx=9,width=5)
save.grid(row=4,column=2)
save.place(x=400,y=150)
note3=tkinter.Label(frame5,text="To save in a different folder, click Browse.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=53,y=90)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370') 
scrap=tkinter.Button(frame5,text="Next",command=lambda:show_frame(frame2),fg="white",bg="#202c34",font="Raleway 11",padx=20,pady=-10)
scrap.grid(row=4,column=1)
scrap.place(x=300,y=327)
cancel=tkinter.Button(frame5,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=9,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)
#========================================= second page code
from tkinter import messagebox
def net_ok():
    try:
        if urllib.request.urlopen('http://google.com'):
            response=tkinter.messagebox.askyesno(title="Parh Pakistan Scrapper v1.0 setup", message="Internet Connection Check Successful\nDo you want to proceed with scrapping?")
            if response == 1:
                show_frame(frame3)
                t1sin=threading.Thread(target=ajk_gb_ms)
                t1sin.start()
                t2sin=threading.Thread(target=prog_start)
                t2sin.start()
    except:
        responseno=tkinter.messagebox.showerror(title="Parh Pakistan Scrapper v1.0 setup", message="Internet Connection Check Failed\nPlease setup your internet connection?")
        if responseno == "ok":
            show_frame(frame2)
def prog_start():
    bar=ttk.Progressbar(frame3,orient=HORIZONTAL,length=400,mode="indeterminate")
    bar.grid(row=5,column=1)
    bar.place(x=85,y=180)
    bar.start(20)
    event.wait()
    bar.stop()
    response1=tkinter.messagebox.showinfo(title="Parh Pakistan Scrapper v1.0 setup", message="Scrapping finished successfully!")            
    if response1 == "ok":
        show_frame(frame4)
bg = Image.open(r'D:\sabz\minarssss.png')
bg = bg.resize((140, 320), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(bg)
bg_label = tkinter.Label(frame2,image=bg)
bg_label.image=bg
bgg=bg_label.grid(row=0,column=0)
#logo = Image.open(r'D:\sabz\Sabz.png')
#logo = logo.resize((45, 45), Image.ANTIALIAS)
#logo = ImageTk.PhotoImage(logo)
#logo_label = tkinter.Label(frame2,image=logo)
#logo_label.image=logo
#logo_label.place(in_=bgg,x=75,y=17)
instructions=tkinter.Label(frame2,text="Check Internet Connectivity",font=("Arial Bold",12),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=160,y=19)
note=tkinter.Label(frame2,text="A strong internet connection is necessary for the scrapper\nto work.",font=("Arial",10),justify="left")
note.grid(row=1,column=1)
note.place(x=160,y=59)
note2=tkinter.Label(frame2,text="Note: Please allow the software to access the internet\nfrom your machine.",font=("Arial",10),justify="left")
note2.grid(row=1,column=1)
note2.place(x=160,y=99)
note3=tkinter.Label(frame2,text="Click Confirm to check internet connectivity.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=160,y=199)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370')
scrap=tkinter.Button(frame2,text="Confirm",command=net_ok,fg="white",bg="#202c34",font="Raleway 11 ",padx=12,pady=-10)
scrap.grid(row=4,column=1)
scrap.place(x=300,y=327)
cancel=tkinter.Button(frame2,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=12,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)
#===================================== third page code
line=Canvas(frame3,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame3,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
img = Image.open(r'D:\sabz\lol.png')
img = img.resize((43, 44), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
img_label = tkinter.Label(frame3,image=img)
img_label.image=img
img_label.place(x=15,y=80)
instructions=tkinter.Label(frame3,text="Parh Pakistan's Scrapper in progress.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=8)
note=tkinter.Label(frame3,text="Azad Jammu Kashmir and Gilgit Baltistan's Universities are being scrapped",font=("Arial",9),justify="left")
note.grid(row=1,column=1)
note.place(x=10,y=32)
note3=tkinter.Label(frame3,text="Please wait while the Scrapper Wizard scraps the information.\nThis may take several minutes.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=85,y=90)
note4=tkinter.Label(frame3,text="Status:\nScrapping information from websites.",font=("Arial",10),justify="left")
note4.grid(row=4,column=1)
note4.place(x=85,y=140)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370') 
cancel=tkinter.Button(frame3,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=9,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)
#========================================= fourth page code
line=Canvas(frame4,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame4,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
instructions=tkinter.Label(frame4,text="Azad Jammu Kashmir and Gilgit Baltistan's summary of results.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=25)
note3=tkinter.Label(frame4,text="The summary of results includes the list of universities not scrapped owing\nto any problem in accessing the university's official website.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=50,y=80)
#rame_scroll=tkinter.Frame(window)
#rame_scroll.grid(row=0,column=0,sticky="NSEW")
#croll=Scrollbar(frame_scroll,orient=VERTICAL)
#roll.config(command=list.yview)
#croll.grid(side=RIGHT,fill=Y)
list_ajk=tkinter.Listbox(frame4,width=73,bd=1)
list_ajk.grid(row=1,column=0)
list_ajk.place(x=50,y=125)
def info():
    event3.wait()
    total=len(pdList_ajk)
    unscrap=len(error_ajk)
    scrapped_u=total-unscrap
    list_ajk.insert(0,"Total number of universities = " + str(total))
    list_ajk.insert(1,"Number of universities scrapped = " + str(scrapped_u))
    list_ajk.insert(2,"Number of universities not scrapped = " + str(unscrap))
    list_ajk.insert(3,"")
    list_ajk.insert(4,"List of universities not scrapped:")
def err():
    event2.wait()
    for name in error_ajk:
        list_ajk.insert(END,name)
t3=threading.Thread(target=info)
t3.start()
t2=threading.Thread(target=err)
t2.start()
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370')
def open1():
    import os
    path = x.name
    path = os.path.realpath(path)
    os.startfile(path)
cancel=tkinter.Button(frame4,text="Preview Results",command=open1,fg="white",bg="#202c34",font="Raleway 11",padx=12,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=380,y=327)
exit=tkinter.Button(frame4,text="Exit",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=12,pady=-10)
exit.grid(row=4,column=2)
exit.place(x=300,y=327)
#========================================== BALOCHISTAN
#========================================== BALOCHISTAN
#============================================= BALOCHISTAN
#==========================================  save page


def save_bal():
    data_bal = [('All types(.)', '.')]
    global x_bal
    x_bal = asksaveasfile(filetypes = data_bal, defaultextension = data_bal)
    list2.insert(0,x_bal.name)
def write_bal():
    event4bal.wait()
    global writer_bal
    writer_bal = pd.ExcelWriter(x_bal.name, engine='xlsxwriter')
def df_bal():
    event5bal.wait()
    bal_df.to_excel(writer_bal, sheet_name='Sheet1')
    writer_bal.save()
write_bal_thread=threading.Thread(target=write_bal)
write_bal_thread.start()
df_bal_thread=threading.Thread(target=df_bal)
df_bal_thread.start()
line=Canvas(frame5bal,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame5bal,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
instructions=tkinter.Label(frame5bal,text="Select insallation folder.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=8)
note=tkinter.Label(frame5bal,text="This is the folder where the scrapped data will be saved.",font=("Arial",9),justify="left")
note.grid(row=1,column=1)
note.place(x=10,y=32)
list2=tkinter.Listbox(frame5bal,width=53,height=1 ,bd=1)
list2.grid(row=1,column=0)
list2.place(x=53,y=155)
list2.insert(0,"")
save=tkinter.Button(frame5bal,text="Browse",command=save_bal,fg="white",bg="#202c34",font="Raleway 10",padx=9,width=5)
save.grid(row=4,column=2)
save.place(x=400,y=150)
note3=tkinter.Label(frame5bal,text="To save in a different folder, click Browse.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=53,y=90)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370') 
scrap=tkinter.Button(frame5bal,text="Next",command=lambda:show_frame(frame2bal),fg="white",bg="#202c34",font="Raleway 11",padx=20,pady=-10)
scrap.grid(row=4,column=1)
scrap.place(x=300,y=327)
cancel=tkinter.Button(frame5bal,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=9,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)


#========================================= second page code
from tkinter import messagebox
def net_ok_bal():
    try:
        if urllib.request.urlopen('http://google.com'):
            response=tkinter.messagebox.askyesno(title="Parh Pakistan Scrapper v1.0 setup", message="Internet Connection Check Successful\nDo you want to proceed with scrapping?")
            if response == 1:
                show_frame(frame3bal)
                t1sin=threading.Thread(target=bal_ms)
                t1sin.start()
                t2sin=threading.Thread(target=prog_start_bal)
                t2sin.start()
    except:
        responseno=tkinter.messagebox.showerror(title="Parh Pakistan Scrapper v1.0 setup", message="Internet Connection Check Failed\nPlease setup your internet connection?")
        if responseno == "ok":
            show_frame(frame2bal)
def prog_start_bal():
    bar=ttk.Progressbar(frame3bal,orient=HORIZONTAL,length=400,mode="indeterminate")
    bar.grid(row=5,column=1)
    bar.place(x=85,y=180)
    bar.start(20)
    eventbal.wait()
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    bar.stop()
    response1=tkinter.messagebox.showinfo(title="Parh Pakistan Scrapper v1.0 setup", message="Scrapping finished successfully!")            
    if response1 == "ok":
        show_frame(frame4bal)
bg = Image.open(r'D:\sabz\minarssss.png')
bg = bg.resize((140, 320), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(bg)
bg_label = tkinter.Label(frame2bal,image=bg)
bg_label.image=bg
bgg=bg_label.grid(row=0,column=0)
#logo = Image.open(r'D:\sabz\Sabz.png')
#logo = logo.resize((45, 45), Image.ANTIALIAS)
#logo = ImageTk.PhotoImage(logo)
#logo_label = tkinter.Label(frame2,image=logo)
#logo_label.image=logo
#logo_label.place(in_=bgg,x=75,y=17)
instructions=tkinter.Label(frame2bal,text="Check Internet Connectivity",font=("Arial Bold",12),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=160,y=19)
note=tkinter.Label(frame2bal,text="A strong internet connection is necessary for the scrapper\nto work.",font=("Arial",10),justify="left")
note.grid(row=1,column=1)
note.place(x=160,y=59)
note2=tkinter.Label(frame2bal,text="Note: Please allow the software to access the internet\nfrom your machine.",font=("Arial",10),justify="left")
note2.grid(row=1,column=1)
note2.place(x=160,y=99)
note3=tkinter.Label(frame2,text="Click Confirm to check internet connectivity.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=160,y=199)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370')
scrap=tkinter.Button(frame2bal,text="Confirm",command=net_ok_bal,fg="white",bg="#202c34",font="Raleway 11 ",padx=12,pady=-10)
scrap.grid(row=4,column=1)
scrap.place(x=300,y=327)
cancel=tkinter.Button(frame2bal,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=12,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)
#===================================== third page code
line=Canvas(frame3bal,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame3bal,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
img = Image.open(r'D:\sabz\lol.png')
img = img.resize((43, 44), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
img_label = tkinter.Label(frame3bal,image=img)
img_label.image=img
img_label.place(x=15,y=80)
instructions=tkinter.Label(frame3bal,text="Parh Pakistan's Scrapper in progress.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=8)
note=tkinter.Label(frame3bal,text="Azad Jammu Kashmir and Gilgit Baltistan's Universities are being scrapped",font=("Arial",9),justify="left")
note.grid(row=1,column=1)
note.place(x=10,y=32)
note3=tkinter.Label(frame3bal,text="Please wait while the Scrapper Wizard scraps the information.\nThis may take several minutes.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=85,y=90)
note4=tkinter.Label(frame3bal,text="Status:\nScrapping information from websites.",font=("Arial",10),justify="left")
note4.grid(row=4,column=1)
note4.place(x=85,y=140)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370') 
cancel=tkinter.Button(frame3bal,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=9,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)
#========================================= fourth page code
line=Canvas(frame4bal,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame4bal,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
instructions=tkinter.Label(frame4bal,text="Balochistan's summary of results.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=25)
note3=tkinter.Label(frame4bal,text="The summary of results includes the list of universities not scrapped owing\nto any problem in accessing the university's official website.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=50,y=80)
#rame_scroll=tkinter.Frame(window)
#rame_scroll.grid(row=0,column=0,sticky="NSEW")
#croll=Scrollbar(frame_scroll,orient=VERTICAL)
#roll.config(command=list.yview)
#croll.grid(side=RIGHT,fill=Y)
list1=tkinter.Listbox(frame4bal,width=73,bd=1)
list1.grid(row=1,column=0)
list1.place(x=50,y=125)
def info_bal():
    event3bal.wait()
    total_bal=len(pdList_bal)
    unscrap_bal=len(error_bal)
    scrapped_bal=total_bal-unscrap_bal
    list1.insert(0,"Total number of universities = " + str(total_bal))
    list1.insert(1,"Number of universities scrapped = " + str(scrapped_bal))
    list1.insert(2,"Number of universities not scrapped = " + str(unscrap_bal))
    list1.insert(3,"")
    list1.insert(4,"List of universities not scrapped:")
def err_bal():
    event2bal.wait()
    for x_bal in error_bal:
        list1.insert(END,x_bal)
t3bal=threading.Thread(target=info_bal)
t3bal.start()
t4bal=threading.Thread(target=err_bal)
t4bal.start()
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370')
def open1_bal():
    import os
    path = x_bal.name
    path = os.path.realpath(path)
    os.startfile(path)
cancel=tkinter.Button(frame4bal,text="Preview Results",command=open1_bal,fg="white",bg="#202c34",font="Raleway 11",padx=12,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=380,y=327)
exit=tkinter.Button(frame4bal,text="Exit",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=12,pady=-10)
exit.grid(row=4,column=2)
exit.place(x=300,y=327)
#========================================== ISLAMABAD
#========================================== ISLAMABAD
#============================================= ISLAMABAD
#==========================================  save page


def save_isb():
    data_isb = [('All types(.)', '.')]
    global x_isb
    x_isb = asksaveasfile(filetypes = data_isb, defaultextension = data_isb)
    list_isb.insert(0,x_isb.name)
def write_isb():
    event4isb.wait()
    global writer_isb
    writer_isb = pd.ExcelWriter(x_isb.name, engine='xlsxwriter')
def df_isb():
    event5isb.wait()
    isb_df.to_excel(writer_isb, sheet_name='Sheet1')
    writer_isb.save()
write_isb_thread=threading.Thread(target=write_isb)
write_isb_thread.start()
df_isb_thread=threading.Thread(target=df_isb)
df_isb_thread.start()
line=Canvas(frame5isb,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame5isb,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
instructions=tkinter.Label(frame5isb,text="Select insallation folder.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=8)
note=tkinter.Label(frame5isb,text="This is the folder where the scrapped data will be saved.",font=("Arial",9),justify="left")
note.grid(row=1,column=1)
note.place(x=10,y=32)
list_isb=tkinter.Listbox(frame5isb,width=53,height=1 ,bd=1)
list_isb.grid(row=1,column=0)
list_isb.place(x=53,y=155)
list_isb.insert(0,"")
save=tkinter.Button(frame5isb,text="Browse",command=save_isb,fg="white",bg="#202c34",font="Raleway 10",padx=9,width=5)
save.grid(row=4,column=2)
save.place(x=400,y=150)
note3=tkinter.Label(frame5isb,text="To save in a different folder, click Browse.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=53,y=90)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370') 
scrap=tkinter.Button(frame5isb,text="Next",command=lambda:show_frame(frame2isb),fg="white",bg="#202c34",font="Raleway 11",padx=20,pady=-10)
scrap.grid(row=4,column=1)
scrap.place(x=300,y=327)
cancel=tkinter.Button(frame5isb,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=9,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)

#========================================= second page code
from tkinter import messagebox
def net_ok_isb():
    try:
        if urllib.request.urlopen('http://google.com'):
            response=tkinter.messagebox.askyesno(title="Parh Pakistan Scrapper v1.0 setup", message="Internet Connection Check Successful\nDo you want to proceed with scrapping?")
            if response == 1:
                show_frame(frame3isb)
                t1sin=threading.Thread(target=isb_ms)
                t1sin.start()
                t2sin=threading.Thread(target=prog_start_isb)
                t2sin.start()
    except:
        responseno=tkinter.messagebox.showerror(title="Parh Pakistan Scrapper v1.0 setup", message="Internet Connection Check Failed\nPlease setup your internet connection?")
        if responseno == "ok":
            show_frame(frame2isb)
def prog_start_isb():
    bar=ttk.Progressbar(frame3isb,orient=HORIZONTAL,length=400,mode="indeterminate")
    bar.grid(row=5,column=1)
    bar.place(x=85,y=180)
    bar.start(20)
    eventisb.wait()
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    bar.stop()
    response1=tkinter.messagebox.showinfo(title="Parh Pakistan Scrapper v1.0 setup", message="Scrapping finished successfully!")            
    if response1 == "ok":
        show_frame(frame4isb)
bg = Image.open(r'D:\sabz\minarssss.png')
bg = bg.resize((140, 320), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(bg)
bg_label = tkinter.Label(frame2isb,image=bg)
bg_label.image=bg
bgg=bg_label.grid(row=0,column=0)
#logo = Image.open(r'D:\sabz\Sabz.png')
#logo = logo.resize((45, 45), Image.ANTIALIAS)
#logo = ImageTk.PhotoImage(logo)
#logo_label = tkinter.Label(frame2,image=logo)
#logo_label.image=logo
#logo_label.place(in_=bgg,x=75,y=17)
instructions=tkinter.Label(frame2isb,text="Check Internet Connectivity",font=("Arial Bold",12),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=160,y=19)
note=tkinter.Label(frame2isb,text="A strong internet connection is necessary for the scrapper\nto work.",font=("Arial",10),justify="left")
note.grid(row=1,column=1)
note.place(x=160,y=59)
note2=tkinter.Label(frame2isb,text="Note: Please allow the software to access the internet\nfrom your machine.",font=("Arial",10),justify="left")
note2.grid(row=1,column=1)
note2.place(x=160,y=99)
note3=tkinter.Label(frame2isb,text="Click Confirm to check internet connectivity.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=160,y=199)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370')
scrap=tkinter.Button(frame2isb,text="Confirm",command=net_ok_isb,fg="white",bg="#202c34",font="Raleway 11 ",padx=12,pady=-10)
scrap.grid(row=4,column=1)
scrap.place(x=300,y=327)
cancel=tkinter.Button(frame2isb,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=12,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)
#===================================== third page code
line=Canvas(frame3isb,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame3isb,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
img = Image.open(r'D:\sabz\lol.png')
img = img.resize((43, 44), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
img_label = tkinter.Label(frame3isb,image=img)
img_label.image=img
img_label.place(x=15,y=80)
instructions=tkinter.Label(frame3isb,text="Parh Pakistan's Scrapper in progress.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=8)
note=tkinter.Label(frame3isb,text="Islamabad's Universities are being scrapped",font=("Arial",9),justify="left")
note.grid(row=1,column=1)
note.place(x=10,y=32)
note3=tkinter.Label(frame3isb,text="Please wait while the Scrapper Wizard scraps the information.\nThis may take several minutes.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=85,y=90)
note4=tkinter.Label(frame3isb,text="Status:\nScrapping information from websites.",font=("Arial",10),justify="left")
note4.grid(row=4,column=1)
note4.place(x=85,y=140)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370') 
cancel=tkinter.Button(frame3isb,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=9,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)
#========================================= fourth page code
line=Canvas(frame4isb,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame4isb,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
instructions=tkinter.Label(frame4isb,text="Islamabad's summary of results.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=25)
note3=tkinter.Label(frame4isb,text="The summary of results includes the list of universities not scrapped owing\nto any problem in accessing the university's official website.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=50,y=80)
#rame_scroll=tkinter.Frame(window)
#rame_scroll.grid(row=0,column=0,sticky="NSEW")
#croll=Scrollbar(frame_scroll,orient=VERTICAL)
#roll.config(command=list.yview)
#croll.grid(side=RIGHT,fill=Y)
list1isb=tkinter.Listbox(frame4isb,width=73,bd=1)
list1isb.grid(row=1,column=0)
list1isb.place(x=50,y=125)
def info_isb():
    event3isb.wait()
    total_isb=len(pdList_isb)
    unscrap_isb=len(error_isb)
    scrapped_isb=total_isb-unscrap_isb
    list1isb.insert(0,"Total number of universities = " + str(total_isb))
    list1isb.insert(1,"Number of universities scrapped = " + str(scrapped_isb))
    list1isb.insert(2,"Number of universities not scrapped = " + str(unscrap_isb))
    list1isb.insert(3,"")
    list1isb.insert(4,"List of universities not scrapped:")
def err_isb():
    event2isb.wait()
    for x_isb in error_isb:
        list1isb.insert(END,x_isb)
t3isb=threading.Thread(target=info_isb)
t3isb.start()
t4isb=threading.Thread(target=err_isb)
t4isb.start()
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370')
def open1_isb():
    import os
    path = x_isb.name
    path = os.path.realpath(path)
    os.startfile(path)
cancel=tkinter.Button(frame4isb,text="Preview Results",command=open1_isb,fg="white",bg="#202c34",font="Raleway 11",padx=12,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=380,y=327)
exit=tkinter.Button(frame4isb,text="Exit",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=12,pady=-10)
exit.grid(row=4,column=2)
exit.place(x=300,y=327)
#========================================== KPK
#========================================== KPK
#============================================= KPK
#==========================================  save page


def save_kpk():
    data_kpk = [('All types(.)', '.')]
    global x_kpk
    x_kpk = asksaveasfile(filetypes = data_kpk, defaultextension = data_kpk)
    list_kpk.insert(0,x_kpk.name)
def write_kpk():
    event4kpk.wait()
    global writer_kpk
    writer_kpk = pd.ExcelWriter(x_kpk.name, engine='xlsxwriter')
def df_kpk():
    event5kpk.wait()
    kpk_df.to_excel(writer_kpk, sheet_name='Sheet1')
    writer_kpk.save()
write_kpk_thread=threading.Thread(target=write_kpk)
write_kpk_thread.start()
df_kpk_thread=threading.Thread(target=df_kpk)
df_kpk_thread.start()
line=Canvas(frame5kpk,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame5kpk,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
instructions=tkinter.Label(frame5kpk,text="Select insallation folder.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=8)
note=tkinter.Label(frame5kpk,text="This is the folder where the scrapped data will be saved.",font=("Arial",9),justify="left")
note.grid(row=1,column=1)
note.place(x=10,y=32)
list_kpk=tkinter.Listbox(frame5kpk,width=53,height=1 ,bd=1)
list_kpk.grid(row=1,column=0)
list_kpk.place(x=53,y=155)
list_kpk.insert(0,"")
save=tkinter.Button(frame5kpk,text="Browse",command=save_kpk,fg="white",bg="#202c34",font="Raleway 10",padx=9,width=5)
save.grid(row=4,column=2)
save.place(x=400,y=150)
note3=tkinter.Label(frame5kpk,text="To save in a different folder, click Browse.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=53,y=90)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370') 
scrap=tkinter.Button(frame5kpk,text="Next",command=lambda:show_frame(frame2kpk),fg="white",bg="#202c34",font="Raleway 11",padx=20,pady=-10)
scrap.grid(row=4,column=1)
scrap.place(x=300,y=327)
cancel=tkinter.Button(frame5kpk,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=9,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)

#========================================= second page code
from tkinter import messagebox
def net_ok_kpk():
    try:
        if urllib.request.urlopen('http://google.com'):
            response=tkinter.messagebox.askyesno(title="Parh Pakistan Scrapper v1.0 setup", message="Internet Connection Check Successful\nDo you want to proceed with scrapping?")
            if response == 1:
                show_frame(frame3kpk)
                t1sin=threading.Thread(target=kpk_ms)
                t1sin.start()
                t2sin=threading.Thread(target=prog_start_kpk)
                t2sin.start()
    except:
        responseno=tkinter.messagebox.showerror(title="Parh Pakistan Scrapper v1.0 setup", message="Internet Connection Check Failed\nPlease setup your internet connection?")
        if responseno == "ok":
            show_frame(frame2kpk)
def prog_start_kpk():
    bar=ttk.Progressbar(frame3kpk,orient=HORIZONTAL,length=400,mode="indeterminate")
    bar.grid(row=5,column=1)
    bar.place(x=85,y=180)
    bar.start(20)
    eventkpk.wait()
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    bar.stop()
    response1=tkinter.messagebox.showinfo(title="Parh Pakistan Scrapper v1.0 setup", message="Scrapping finished successfully!")            
    if response1 == "ok":
        show_frame(frame4kpk)
bg = Image.open(r'D:\sabz\minarssss.png')
bg = bg.resize((140, 320), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(bg)
bg_label = tkinter.Label(frame2kpk,image=bg)
bg_label.image=bg
bgg=bg_label.grid(row=0,column=0)
#logo = Image.open(r'D:\sabz\Sabz.png')
#logo = logo.resize((45, 45), Image.ANTIALIAS)
#logo = ImageTk.PhotoImage(logo)
#logo_label = tkinter.Label(frame2,image=logo)
#logo_label.image=logo
#logo_label.place(in_=bgg,x=75,y=17)
instructions=tkinter.Label(frame2kpk,text="Check Internet Connectivity",font=("Arial Bold",12),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=160,y=19)
note=tkinter.Label(frame2kpk,text="A strong internet connection is necessary for the scrapper\nto work.",font=("Arial",10),justify="left")
note.grid(row=1,column=1)
note.place(x=160,y=59)
note2=tkinter.Label(frame2kpk,text="Note: Please allow the software to access the internet\nfrom your machine.",font=("Arial",10),justify="left")
note2.grid(row=1,column=1)
note2.place(x=160,y=99)
note3=tkinter.Label(frame2kpk,text="Click Confirm to check internet connectivity.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=160,y=199)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370')
scrap=tkinter.Button(frame2kpk,text="Confirm",command=net_ok_kpk,fg="white",bg="#202c34",font="Raleway 11 ",padx=12,pady=-10)
scrap.grid(row=4,column=1)
scrap.place(x=300,y=327)
cancel=tkinter.Button(frame2kpk,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=12,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)
#===================================== third page code
line=Canvas(frame3kpk,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame3kpk,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
img = Image.open(r'D:\sabz\lol.png')
img = img.resize((43, 44), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
img_label = tkinter.Label(frame3kpk,image=img)
img_label.image=img
img_label.place(x=15,y=80)
instructions=tkinter.Label(frame3kpk,text="Parh Pakistan's Scrapper in progress.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=8)
note=tkinter.Label(frame3kpk,text="Khyber Pakthukhwa's Universities are being scrapped",font=("Arial",9),justify="left")
note.grid(row=1,column=1)
note.place(x=10,y=32)
note3=tkinter.Label(frame3kpk,text="Please wait while the Scrapper Wizard scraps the information.\nThis may take several minutes.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=85,y=90)
note4=tkinter.Label(frame3kpk,text="Status:\nScrapping information from websites.",font=("Arial",10),justify="left")
note4.grid(row=4,column=1)
note4.place(x=85,y=140)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370') 
cancel=tkinter.Button(frame3kpk,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=9,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)
#========================================= fourth page code
line=Canvas(frame4kpk,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame4kpk,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
instructions=tkinter.Label(frame4kpk,text="Khyber Pakthukwa's summary of results.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=25)
note3=tkinter.Label(frame4kpk,text="The summary of results includes the list of universities not scrapped owing\nto any problem in accessing the university's official website.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=50,y=80)
#rame_scroll=tkinter.Frame(window)
#rame_scroll.grid(row=0,column=0,sticky="NSEW")
#croll=Scrollbar(frame_scroll,orient=VERTICAL)
#roll.config(command=list.yview)
#croll.grid(side=RIGHT,fill=Y)
list1kpk=tkinter.Listbox(frame4kpk,width=73,bd=1)
list1kpk.grid(row=1,column=0)
list1kpk.place(x=50,y=125)
def info_kpk():
    event3kpk.wait()
    total_kpk=len(pdList_kpk)
    unscrap_kpk=len(error_kpk)
    scrapped_kpk=total_kpk-unscrap_kpk
    list1kpk.insert(0,"Total number of universities = " + str(total_kpk))
    list1kpk.insert(1,"Number of universities scrapped = " + str(scrapped_kpk))
    list1kpk.insert(2,"Number of universities not scrapped = " + str(unscrap_kpk))
    list1kpk.insert(3,"")
    list1kpk.insert(4,"List of universities not scrapped:")
def err_kpk():
    event2kpk.wait()
    for x_kpk in error_kpk:
        list1kpk.insert(END,x_kpk)
t3kpk=threading.Thread(target=info_kpk)
t3kpk.start()
t4kpk=threading.Thread(target=err_kpk)
t4kpk.start()
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370')
def open1_kpk():
    import os
    path = x_kpk.name
    path = os.path.realpath(path)
    os.startfile(path)
cancel=tkinter.Button(frame4kpk,text="Preview Results",command=open1_kpk,fg="white",bg="#202c34",font="Raleway 11",padx=12,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=380,y=327)
exit=tkinter.Button(frame4kpk,text="Exit",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=12,pady=-10)
exit.grid(row=4,column=2)
exit.place(x=300,y=327)
#========================================== PUNJAB
#========================================== PUNJAB
#============================================= PUNJAB
#==========================================  save page


def save_pun():
    data_pun = [('All types(.)', '.')]
    global x_pun
    x_pun = asksaveasfile(filetypes = data_pun, defaultextension = data_pun)
    list_pun.insert(0,x_pun.name)
def write_pun():
    event4pun.wait()
    global writer_pun
    writer_pun = pd.ExcelWriter(x_pun.name, engine='xlsxwriter')
def df_pun():
    event5pun.wait()
    pun_df.to_excel(writer_pun, sheet_name='Sheet1')
    writer_pun.save()
write_pun_thread=threading.Thread(target=write_pun)
write_pun_thread.start()
df_pun_thread=threading.Thread(target=df_pun)
df_pun_thread.start()
line=Canvas(frame5pun,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame5pun,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
instructions=tkinter.Label(frame5pun,text="Select insallation folder.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=8)
note=tkinter.Label(frame5pun,text="This is the folder where the scrapped data will be saved.",font=("Arial",9),justify="left")
note.grid(row=1,column=1)
note.place(x=10,y=32)
list_pun=tkinter.Listbox(frame5pun,width=53,height=1 ,bd=1)
list_pun.grid(row=1,column=0)
list_pun.place(x=53,y=155)
list_pun.insert(0,"")
save=tkinter.Button(frame5pun,text="Browse",command=save_pun,fg="white",bg="#202c34",font="Raleway 10",padx=9,width=5)
save.grid(row=4,column=2)
save.place(x=400,y=150)
note3=tkinter.Label(frame5pun,text="To save in a different folder, click Browse.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=53,y=90)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370') 
scrap=tkinter.Button(frame5pun,text="Next",command=lambda:show_frame(frame2pun),fg="white",bg="#202c34",font="Raleway 11",padx=20,pady=-10)
scrap.grid(row=4,column=1)
scrap.place(x=300,y=327)
cancel=tkinter.Button(frame5pun,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=9,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)

#========================================= second page code
from tkinter import messagebox
def net_ok_pun():
    try:
        if urllib.request.urlopen('http://google.com'):
            response=tkinter.messagebox.askyesno(title="Parh Pakistan Scrapper v1.0 setup", message="Internet Connection Check Successful\nDo you want to proceed with scrapping?")
            if response == 1:
                show_frame(frame3pun)
                t1sin=threading.Thread(target=punjab_ms)
                t1sin.start()
                t2sin=threading.Thread(target=prog_start_pun)
                t2sin.start()
    except:
        responseno=tkinter.messagebox.showerror(title="Parh Pakistan Scrapper v1.0 setup", message="Internet Connection Check Failed\nPlease setup your internet connection?")
        if responseno == "ok":
            show_frame(frame2pun)
def prog_start_pun():
    bar=ttk.Progressbar(frame3pun,orient=HORIZONTAL,length=400,mode="indeterminate")
    bar.grid(row=5,column=1)
    bar.place(x=85,y=180)
    bar.start(20)
    eventpun.wait()
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    bar.stop()
    response1=tkinter.messagebox.showinfo(title="Parh Pakistan Scrapper v1.0 setup", message="Scrapping finished successfully!")            
    if response1 == "ok":
        show_frame(frame4pun)
bg = Image.open(r'D:\sabz\minarssss.png')
bg = bg.resize((140, 320), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(bg)
bg_label = tkinter.Label(frame2pun,image=bg)
bg_label.image=bg
bgg=bg_label.grid(row=0,column=0)
#logo = Image.open(r'D:\sabz\Sabz.png')
#logo = logo.resize((45, 45), Image.ANTIALIAS)
#logo = ImageTk.PhotoImage(logo)
#logo_label = tkinter.Label(frame2,image=logo)
#logo_label.image=logo
#logo_label.place(in_=bgg,x=75,y=17)
instructions=tkinter.Label(frame2pun,text="Check Internet Connectivity",font=("Arial Bold",12),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=160,y=19)
note=tkinter.Label(frame2pun,text="A strong internet connection is necessary for the scrapper\nto work.",font=("Arial",10),justify="left")
note.grid(row=1,column=1)
note.place(x=160,y=59)
note2=tkinter.Label(frame2pun,text="Note: Please allow the software to access the internet\nfrom your machine.",font=("Arial",10),justify="left")
note2.grid(row=1,column=1)
note2.place(x=160,y=99)
note3=tkinter.Label(frame2pun,text="Click Confirm to check internet connectivity.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=160,y=199)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370')
scrap=tkinter.Button(frame2pun,text="Confirm",command=net_ok_pun,fg="white",bg="#202c34",font="Raleway 11 ",padx=12,pady=-10)
scrap.grid(row=4,column=1)
scrap.place(x=300,y=327)
cancel=tkinter.Button(frame2pun,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=12,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)
#===================================== third page code
line=Canvas(frame3pun,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame3pun,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
img = Image.open(r'D:\sabz\lol.png')
img = img.resize((43, 44), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
img_label = tkinter.Label(frame3pun,image=img)
img_label.image=img
img_label.place(x=15,y=80)
instructions=tkinter.Label(frame3pun,text="Parh Pakistan's Scrapper in progress.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=8)
note=tkinter.Label(frame3pun,text="Khyber Pakthukhwa's Universities are being scrapped",font=("Arial",9),justify="left")
note.grid(row=1,column=1)
note.place(x=10,y=32)
note3=tkinter.Label(frame3pun,text="Please wait while the Scrapper Wizard scraps the information.\nThis may take several minutes.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=85,y=90)
note4=tkinter.Label(frame3pun,text="Status:\nScrapping information from websites.",font=("Arial",10),justify="left")
note4.grid(row=4,column=1)
note4.place(x=85,y=140)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370') 
cancel=tkinter.Button(frame3pun,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=9,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)
#========================================= fourth page code
line=Canvas(frame4pun,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame4pun,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
instructions=tkinter.Label(frame4pun,text="Khyber Pakthukwa's summary of results.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=25)
note3=tkinter.Label(frame4pun,text="The summary of results includes the list of universities not scrapped owing\nto any problem in accessing the university's official website.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=50,y=80)
#rame_scroll=tkinter.Frame(window)
#rame_scroll.grid(row=0,column=0,sticky="NSEW")
#croll=Scrollbar(frame_scroll,orient=VERTICAL)
#roll.config(command=list.yview)
#croll.grid(side=RIGHT,fill=Y)
list1pun=tkinter.Listbox(frame4pun,width=73,bd=1)
list1pun.grid(row=1,column=0)
list1pun.place(x=50,y=125)
def info_pun():
    event3pun.wait()
    total_pun=len(pdList_pun)
    unscrap_pun=len(error_pun)
    scrapped_pun=total_pun-unscrap_pun
    list1pun.insert(0,"Total number of universities = " + str(total_pun))
    list1pun.insert(1,"Number of universities scrapped = " + str(scrapped_pun))
    list1pun.insert(2,"Number of universities not scrapped = " + str(unscrap_pun))
    list1pun.insert(3,"")
    list1pun.insert(4,"List of universities not scrapped:")
def err_pun():
    event2pun.wait()
    for x_pun in error_pun:
        list1pun.insert(END,x_pun)
t3pun=threading.Thread(target=info_pun)
t3pun.start()
t4pun=threading.Thread(target=err_pun)
t4pun.start()
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370')
def open1_pun():
    import os
    path = x_pun.name
    path = os.path.realpath(path)
    os.startfile(path)
cancel=tkinter.Button(frame4pun,text="Preview Results",command=open1_pun,fg="white",bg="#202c34",font="Raleway 11",padx=12,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=380,y=327)
exit=tkinter.Button(frame4pun,text="Exit",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=12,pady=-10)
exit.grid(row=4,column=2)
exit.place(x=300,y=327)
#========================================== SINDH
#========================================== SINDH
#============================================= SINDH
#==========================================  save page


def save_sin():
    data_sin = [('All types(.)', '.')]
    global x_sin
    x_sin = asksaveasfile(filetypes = data_sin, defaultextension = data_sin)
    list_sin.insert(0,x_sin.name)
def write_sin():
    event4sin.wait()
    global writer_sin
    writer_sin = pd.ExcelWriter(x_sin.name, engine='xlsxwriter')
def df_sin():
    event5sin.wait()
    sin_df.to_excel(writer_sin, sheet_name='Sheet1')
    writer_sin.save()
write_sin_thread=threading.Thread(target=write_sin)
write_sin_thread.start()
df_sin_thread=threading.Thread(target=df_sin)
df_sin_thread.start()
line=Canvas(frame5sin,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame5sin,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
instructions=tkinter.Label(frame5sin,text="Select insallation folder.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=8)
note=tkinter.Label(frame5sin,text="This is the folder where the scrapped data will be saved.",font=("Arial",9),justify="left")
note.grid(row=1,column=1)
note.place(x=10,y=32)
list_sin=tkinter.Listbox(frame5sin,width=53,height=1 ,bd=1)
list_sin.grid(row=1,column=0)
list_sin.place(x=53,y=155)
list_sin.insert(0,"")
save=tkinter.Button(frame5sin,text="Browse",command=save_sin,fg="white",bg="#202c34",font="Raleway 10",padx=9,width=5)
save.grid(row=4,column=2)
save.place(x=400,y=150)
note3=tkinter.Label(frame5sin,text="To save in a different folder, click Browse.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=53,y=90)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370') 
scrap=tkinter.Button(frame5sin,text="Next",command=lambda:show_frame(frame2sin),fg="white",bg="#202c34",font="Raleway 11",padx=20,pady=-10)
scrap.grid(row=4,column=1)
scrap.place(x=300,y=327)
cancel=tkinter.Button(frame5sin,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=9,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)

#========================================= second page code
from tkinter import messagebox
def net_ok_sin():
    try:
        if urllib.request.urlopen('http://google.com'):
            response=tkinter.messagebox.askyesno(title="Parh Pakistan Scrapper v1.0 setup", message="Internet Connection Check Successful\nDo you want to proceed with scrapping?")
            if response == 1:
                show_frame(frame3sin)
                t1sin=threading.Thread(target=sindh_ms)
                t1sin.start()
                t2sin=threading.Thread(target=prog_start_sin)
                t2sin.start()
    except:
        responseno=tkinter.messagebox.showerror(title="Parh Pakistan Scrapper v1.0 setup", message="Internet Connection Check Failed\nPlease setup your internet connection?")
        if responseno == "ok":
            show_frame(frame2sin)
def prog_start_sin():
    bar=ttk.Progressbar(frame3sin,orient=HORIZONTAL,length=400,mode="indeterminate")
    bar.grid(row=5,column=1)
    bar.place(x=85,y=180)
    bar.start(20)
    eventsin.wait()
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    bar.stop()
    response1=tkinter.messagebox.showinfo(title="Parh Pakistan Scrapper v1.0 setup", message="Scrapping finished successfully!")            
    if response1 == "ok":
        show_frame(frame4sin)
bg = Image.open(r'D:\sabz\minarssss.png')
bg = bg.resize((140, 320), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(bg)
bg_label = tkinter.Label(frame2sin,image=bg)
bg_label.image=bg
bgg=bg_label.grid(row=0,column=0)
#logo = Image.open(r'D:\sabz\Sabz.png')
#logo = logo.resize((45, 45), Image.ANTIALIAS)
#logo = ImageTk.PhotoImage(logo)
#logo_label = tkinter.Label(frame2,image=logo)
#logo_label.image=logo
#logo_label.place(in_=bgg,x=75,y=17)
instructions=tkinter.Label(frame2sin,text="Check Internet Connectivity",font=("Arial Bold",12),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=160,y=19)
note=tkinter.Label(frame2sin,text="A strong internet connection is necessary for the scrapper\nto work.",font=("Arial",10),justify="left")
note.grid(row=1,column=1)
note.place(x=160,y=59)
note2=tkinter.Label(frame2sin,text="Note: Please allow the software to access the internet\nfrom your machine.",font=("Arial",10),justify="left")
note2.grid(row=1,column=1)
note2.place(x=160,y=99)
note3=tkinter.Label(frame2sin,text="Click Confirm to check internet connectivity.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=160,y=199)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370')
scrap=tkinter.Button(frame2sin,text="Confirm",command=net_ok_sin,fg="white",bg="#202c34",font="Raleway 11 ",padx=12,pady=-10)
scrap.grid(row=4,column=1)
scrap.place(x=300,y=327)
cancel=tkinter.Button(frame2sin,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=12,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)
#===================================== third page code
line=Canvas(frame3sin,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame3sin,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
img = Image.open(r'D:\sabz\lol.png')
img = img.resize((43, 44), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
img_label = tkinter.Label(frame3sin,image=img)
img_label.image=img
img_label.place(x=15,y=80)
instructions=tkinter.Label(frame3sin,text="Parh Pakistan's Scrapper in progress.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=8)
note=tkinter.Label(frame3sin,text="Khyber Pakthukhwa's Universities are being scrapped",font=("Arial",9),justify="left")
note.grid(row=1,column=1)
note.place(x=10,y=32)
note3=tkinter.Label(frame3sin,text="Please wait while the Scrapper Wizard scraps the information.\nThis may take several minutes.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=85,y=90)
note4=tkinter.Label(frame3sin,text="Status:\nScrapping information from websites.",font=("Arial",10),justify="left")
note4.grid(row=4,column=1)
note4.place(x=85,y=140)
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370') 
cancel=tkinter.Button(frame3sin,text="Cancel",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=9,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=400,y=327)
#========================================= fourth page code
line=Canvas(frame4sin,width=550,height=370)
line.grid(row=0,column=0,sticky="NSEW")
line.create_line(0,63,700,63)
logo = Image.open(r'D:\sabz\Sabz.png')
logo = logo.resize((45, 45), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(frame4sin,image=logo)
logo_label.image=logo
logo_label.place(x=485,y=9)
instructions=tkinter.Label(frame4sin,text="Khyber Pakthukwa's summary of results.",font=("Arial Bold",11),justify="left")
instructions.grid(row=0,column=1)
instructions.place(x=10,y=25)
note3=tkinter.Label(frame4sin,text="The summary of results includes the list of universities not scrapped owing\nto any problem in accessing the university's official website.",font=("Arial",10),justify="left")
note3.grid(row=3,column=1)
note3.place(x=50,y=80)
#rame_scroll=tkinter.Frame(window)
#rame_scroll.grid(row=0,column=0,sticky="NSEW")
#croll=Scrollbar(frame_scroll,orient=VERTICAL)
#roll.config(command=list.yview)
#croll.grid(side=RIGHT,fill=Y)
list1sin=tkinter.Listbox(frame4sin,width=73,bd=1)
list1sin.grid(row=1,column=0)
list1sin.place(x=50,y=125)
def info_sin():
    event3sin.wait()
    total_sin=len(pdList_sin)
    unscrap_sin=len(error_sin)
    scrapped_sin=total_sin-unscrap_sin
    list1sin.insert(0,"Total number of universities = " + str(total_sin))
    list1sin.insert(1,"Number of universities scrapped = " + str(scrapped_sin))
    list1sin.insert(2,"Number of universities not scrapped = " + str(unscrap_sin))
    list1sin.insert(3,"")
    list1sin.insert(4,"List of universities not scrapped:")
def err_sin():
    event2sin.wait()
    for x_sin in error_sin:
        list1sin.insert(END,x_sin)
t3sin=threading.Thread(target=info_sin)
t3sin.start()
t4sin=threading.Thread(target=err_sin)
t4sin.start()
window.title("Sabz-Qalam Scrapper")
window.geometry('550x370')
def open1_sin():
    import os
    path = x_sin.name
    path = os.path.realpath(path)
    os.startfile(path)
cancel=tkinter.Button(frame4sin,text="Preview Results",command=open1_sin,fg="white",bg="#202c34",font="Raleway 11",padx=12,pady=-10)
cancel.grid(row=4,column=2)
cancel.place(x=380,y=327)
exit=tkinter.Button(frame4sin,text="Exit",command=window.destroy,fg="white",bg="#202c34",font="Raleway 11",padx=12,pady=-10)
exit.grid(row=4,column=2)
exit.place(x=300,y=327)
show_frame(frame1)
window.mainloop()   


# In[ ]:





# In[ ]:




