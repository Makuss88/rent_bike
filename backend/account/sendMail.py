def sendMail(mailTo):

    user = 'sqltestsender@gmail.com'
    password = 'console123!@#'

    mailFrom = 'Poczta automatyczna od serweru!'
    mailSubject = 'Rent a bike!'
    mailBody = '''Witaj na moim portalu z wypozyczalnia rowerow!
    '''

    message = '''From: {}
    Subject: {}

    {}
    '''.format(mailFrom, mailSubject, mailBody)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        print('GOOD')
    except:
        print('BAD')