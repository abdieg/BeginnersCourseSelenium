class Locators():

    authentication_401_message = "//body/center/h1"

    topbar_conduit_title = "//a[contains(@class,'navbar')][text()='conduit']"
    topbar_home_button = "//ul/li/a[contains(text(),'Home')]"
    topbar_sign_in_button = "//ul/li/a[contains(text(),'Sign in')]"
    topbar_sign_up_button = "//ul/li/a[contains(text(),'Sign up')]"
    topbar_new_article_button = "//ul/li/a[contains(text(),'New Article')]"
    section_your_feed = "//li/a[contains(text(),'Your Feed')]"
    section_global_feed = "//li/a[contains(text(),'Global Feed')]"

    signin_email = "//input[@placeholder='Email']"
    signin_password = "//input[@placeholder='Password']"
    signin_button = "//button[@type='submit'][contains(text(),'Sign in')]"

    new_article_title = "//input[@formcontrolname='title']"
    new_article_about = "//input[@formcontrolname='description']"
    new_article_markdown = "//textarea[@formcontrolname='body']"
    new_article_tags = "//input[@placeholder='Enter tags']"
    new_article_publish_button = "//button[contains(text(),'Publish Article')]"

    article_title = "//div[@class='article-page']/div[@class='banner']/div[@class='container']/h1"
    article_content = "//div[contains(@class, 'article-content')]//p"

    global_feed_article_preview_title = "//app-article-list//a[@class='preview-link']//h1"
    global_feed_article_preview_about = "//app-article-list//a[@class='preview-link']//p"