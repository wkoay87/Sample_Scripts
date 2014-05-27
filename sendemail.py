def send_mail(send_from, send_to,send_cc, subject, text, files=[],server="localhost"):    
    assert type(send_to)==list
    
    assert type(files)==list

    print 'ERROR HERRRRRE'
    msg = MIMEMultipart('alternative')
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    
    if send_cc is None:
        send_tocc = send_to
    else:
        assert type(send_cc)==list
        msg['Cc'] = COMMASPACE.join(send_cc)
        send_tocc = send_to + send_cc
        
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)
    
    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_tocc, msg.as_string())
    smtp.close()
