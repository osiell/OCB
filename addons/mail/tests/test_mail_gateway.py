# -*- coding: utf-8 -*-

from email.utils import formataddr

from .common import TestMail
from openerp.tools import mute_logger
import socket

MAIL_TEMPLATE = """Return-Path: <whatever-2a840@postmaster.twitter.com>
To: {to}
cc: {cc}
Received: by mail1.openerp.com (Postfix, from userid 10002)
    id 5DF9ABFB2A; Fri, 10 Aug 2012 16:16:39 +0200 (CEST)
From: {email_from}
Subject: {subject}
MIME-Version: 1.0
Content-Type: multipart/alternative;
    boundary="----=_Part_4200734_24778174.1344608186754"
Date: Fri, 10 Aug 2012 14:16:26 +0000
Message-ID: {msg_id}
{extra}
------=_Part_4200734_24778174.1344608186754
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: quoted-printable

Please call me as soon as possible this afternoon!

--
Sylvie
------=_Part_4200734_24778174.1344608186754
Content-Type: text/html; charset=utf-8
Content-Transfer-Encoding: quoted-printable

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>=20
  <meta http-equiv=3D"Content-Type" content=3D"text/html; charset=3Dutf-8" />
 </head>=20
 <body style=3D"margin: 0; padding: 0; background: #ffffff;-webkit-text-size-adjust: 100%;">=20

  <p>Please call me as soon as possible this afternoon!</p>

  <p>--<br/>
     Sylvie
  <p>
 </body>
</html>
------=_Part_4200734_24778174.1344608186754--
"""

MAIL_TEMPLATE_PLAINTEXT = """Return-Path: <whatever-2a840@postmaster.twitter.com>
To: {to}
Received: by mail1.openerp.com (Postfix, from userid 10002)
    id 5DF9ABFB2A; Fri, 10 Aug 2012 16:16:39 +0200 (CEST)
From: Sylvie Lelitre <test.sylvie.lelitre@agrolait.com>
Subject: {subject}
MIME-Version: 1.0
Content-Type: text/plain
Date: Fri, 10 Aug 2012 14:16:26 +0000
Message-ID: {msg_id}
{extra}

Please call me as soon as possible this afternoon!

--
Sylvie
"""

MAIL_MULTIPART_MIXED = """Return-Path: <ignasse.carambar@gmail.com>
X-Original-To: raoul@grosbedon.fr
Delivered-To: raoul@grosbedon.fr
Received: by mail1.grosbedon.com (Postfix, from userid 10002)
    id E8166BFACA; Fri, 23 Aug 2013 13:18:01 +0200 (CEST)
X-Spam-Checker-Version: SpamAssassin 3.3.1 (2010-03-16) on mail1.grosbedon.com
X-Spam-Level:
X-Spam-Status: No, score=-2.6 required=5.0 tests=BAYES_00,FREEMAIL_FROM,
    HTML_MESSAGE,RCVD_IN_DNSWL_LOW autolearn=unavailable version=3.3.1
Received: from mail-ie0-f173.google.com (mail-ie0-f173.google.com [209.85.223.173])
    by mail1.grosbedon.com (Postfix) with ESMTPS id 9BBD7BFAAA
    for <raoul@openerp.fr>; Fri, 23 Aug 2013 13:17:55 +0200 (CEST)
Received: by mail-ie0-f173.google.com with SMTP id qd12so575130ieb.4
        for <raoul@grosbedon.fr>; Fri, 23 Aug 2013 04:17:54 -0700 (PDT)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20120113;
        h=mime-version:date:message-id:subject:from:to:content-type;
        bh=dMNHV52EC7GAa7+9a9tqwT9joy9z+1950J/3A6/M/hU=;
        b=DGuv0VjegdSrEe36ADC8XZ9Inrb3Iu+3/52Bm+caltddXFH9yewTr0JkCRQaJgMwG9
         qXTQgP8qu/VFEbCh6scu5ZgU1hknzlNCYr3LT+Ih7dAZVUEHUJdwjzUU1LFV95G2RaCd
         /Lwff6CibuUvrA+0CBO7IRKW0Sn5j0mukYu8dbaKsm6ou6HqS8Nuj85fcXJfHSHp6Y9u
         dmE8jBh3fHCHF/nAvU+8aBNSIzl1FGfiBYb2jCoapIuVFitKR4q5cuoodpkH9XqqtOdH
         DG+YjEyi8L7uvdOfN16eMr7hfUkQei1yQgvGu9/5kXoHg9+Gx6VsZIycn4zoaXTV3Nhn
         nu4g==
MIME-Version: 1.0
X-Received: by 10.50.124.65 with SMTP id mg1mr1144467igb.43.1377256674216;
 Fri, 23 Aug 2013 04:17:54 -0700 (PDT)
Received: by 10.43.99.71 with HTTP; Fri, 23 Aug 2013 04:17:54 -0700 (PDT)
Date: Fri, 23 Aug 2013 13:17:54 +0200
Message-ID: <CAP76m_V4BY2F7DWHzwfjteyhW8L2LJswVshtmtVym+LUJ=rASQ@mail.gmail.com>
Subject: Test mail multipart/mixed
From: =?ISO-8859-1?Q?Raoul Grosbedon=E9e?= <ignasse.carambar@gmail.com>
To: Followers of ASUSTeK-Joseph-Walters <raoul@grosbedon.fr>
Content-Type: multipart/mixed; boundary=089e01536c4ed4d17204e49b8e96

--089e01536c4ed4d17204e49b8e96
Content-Type: multipart/alternative; boundary=089e01536c4ed4d16d04e49b8e94

--089e01536c4ed4d16d04e49b8e94
Content-Type: text/plain; charset=ISO-8859-1

Should create a multipart/mixed: from gmail, *bold*, with attachment.

--
Marcel Boitempoils.

--089e01536c4ed4d16d04e49b8e94
Content-Type: text/html; charset=ISO-8859-1

<div dir="ltr">Should create a multipart/mixed: from gmail, <b>bold</b>, with attachment.<br clear="all"><div><br></div>-- <br>Marcel Boitempoils.</div>

--089e01536c4ed4d16d04e49b8e94--
--089e01536c4ed4d17204e49b8e96
Content-Type: text/plain; charset=US-ASCII; name="test.txt"
Content-Disposition: attachment; filename="test.txt"
Content-Transfer-Encoding: base64
X-Attachment-Id: f_hkpb27k00

dGVzdAo=
--089e01536c4ed4d17204e49b8e96--"""

MAIL_MULTIPART_MIXED_TWO = """X-Original-To: raoul@grosbedon.fr
Delivered-To: raoul@grosbedon.fr
Received: by mail1.grosbedon.com (Postfix, from userid 10002)
    id E8166BFACA; Fri, 23 Aug 2013 13:18:01 +0200 (CEST)
From: "Bruce Wayne" <bruce@wayneenterprises.com>
Content-Type: multipart/alternative;
 boundary="Apple-Mail=_9331E12B-8BD2-4EC7-B53E-01F3FBEC9227"
Message-Id: <6BB1FAB2-2104-438E-9447-07AE2C8C4A92@sexample.com>
Mime-Version: 1.0 (Mac OS X Mail 7.3 \(1878.6\))

--Apple-Mail=_9331E12B-8BD2-4EC7-B53E-01F3FBEC9227
Content-Transfer-Encoding: 7bit
Content-Type: text/plain;
    charset=us-ascii

First and second part

--Apple-Mail=_9331E12B-8BD2-4EC7-B53E-01F3FBEC9227
Content-Type: multipart/mixed;
 boundary="Apple-Mail=_CA6C687E-6AA0-411E-B0FE-F0ABB4CFED1F"

--Apple-Mail=_CA6C687E-6AA0-411E-B0FE-F0ABB4CFED1F
Content-Transfer-Encoding: 7bit
Content-Type: text/html;
    charset=us-ascii

<html><head></head><body>First part</body></html>

--Apple-Mail=_CA6C687E-6AA0-411E-B0FE-F0ABB4CFED1F
Content-Disposition: inline;
    filename=thetruth.pdf
Content-Type: application/pdf;
    name="thetruth.pdf"
Content-Transfer-Encoding: base64

SSBhbSB0aGUgQmF0TWFuCg==

--Apple-Mail=_CA6C687E-6AA0-411E-B0FE-F0ABB4CFED1F
Content-Transfer-Encoding: 7bit
Content-Type: text/html;
    charset=us-ascii

<html><head></head><body>Second part</body></html>
--Apple-Mail=_CA6C687E-6AA0-411E-B0FE-F0ABB4CFED1F--

--Apple-Mail=_9331E12B-8BD2-4EC7-B53E-01F3FBEC9227--
"""

MAIL_SINGLE_BINARY = """X-Original-To: raoul@grosbedon.fr
Delivered-To: raoul@grosbedon.fr
Received: by mail1.grosbedon.com (Postfix, from userid 10002)
    id E8166BFACA; Fri, 23 Aug 2013 13:18:01 +0200 (CEST)
From: "Bruce Wayne" <bruce@wayneenterprises.com>
Content-Type: application/pdf;
Content-Disposition: filename=thetruth.pdf
Content-Transfer-Encoding: base64
Message-Id: <6BB1FAB2-2104-438E-9447-07AE2C8C4A92@sexample.com>
Mime-Version: 1.0 (Mac OS X Mail 7.3 \(1878.6\))

SSBhbSB0aGUgQmF0TWFuCg=="""


MAIL_XHTML = """Return-Path: <xxxx@xxxx.com>
Received: from xxxx.internal (xxxx.xxxx.internal [1.1.1.1])
	 by xxxx (xxxx 1.1.1-111-g972eecc-slipenbois) with LMTPA;
	 Fri, 13 Apr 2018 22:11:52 -0400
X-Cyrus-Session-Id: sloti35d1t38-1111111-11111111111-5-11111111111111111111
X-Sieve: CMU Sieve 1.0
X-Spam-known-sender: no ("Email failed DMARC policy for domain"); in-addressbook
X-Spam-score: 0.0
X-Spam-hits: ALL_TRUSTED -1, BAYES_00 -1.9, FREEMAIL_FROM 0.001,
  HTML_FONT_LOW_CONTRAST 0.001, HTML_MESSAGE 0.001, SPF_SOFTFAIL 0.665,
  LANGUAGES en, BAYES_USED global, SA_VERSION 1.1.0
X-Spam-source: IP='1.1.1.1', Host='unk', Country='unk', FromHeader='com',
  MailFrom='com'
X-Spam-charsets: plain='utf-8', html='utf-8'
X-IgnoreVacation: yes ("Email failed DMARC policy for domain")
X-Resolved-to: catchall@xxxx.xxxx
X-Delivered-to: catchall@xxxx.xxxx
X-Mail-from: xxxx@xxxx.com
Received: from mx4 ([1.1.1.1])
  by xxxx.internal (LMTPProxy); Fri, 13 Apr 2018 22:11:52 -0400
Received: from xxxx.xxxx.com (localhost [127.0.0.1])
	by xxxx.xxxx.internal (Postfix) with ESMTP id E1111C1111;
	Fri, 13 Apr 2018 22:11:51 -0400 (EDT)
Received: from xxxx.xxxx.internal (localhost [127.0.0.1])
    by xxxx.xxxx.com (Authentication Milter) with ESMTP
    id BBDD1111D1A;
    Fri, 13 Apr 2018 22:11:51 -0400
ARC-Authentication-Results: i=1; xxxx.xxxx.com; arc=none (no signatures found);
    dkim=pass (2048-bit rsa key sha256) header.d=xxxx.com header.i=@xxxx.com header.b=P1aaAAaa x-bits=2048 x-keytype=rsa x-algorithm=sha256 x-selector=fm2;
    dmarc=fail (p=none,d=none) header.from=xxxx.com;
    iprev=pass policy.iprev=1.1.1.1 (out1-smtp.xxxx.com);
    spf=softfail smtp.mailfrom=xxxx@xxxx.com smtp.helo=out1-smtp.xxxx.com;
    x-aligned-from=pass (Address match);
    x-cm=none score=0;
    x-ptr=pass x-ptr-helo=out1-smtp.xxxx.com x-ptr-lookup=out1-smtp.xxxx.com;
    x-return-mx=pass smtp.domain=xxxx.com smtp.result=pass smtp_is_org_domain=yes header.domain=xxxx.com header.result=pass header_is_org_domain=yes;
    x-tls=pass version=TLSv1.2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128;
    x-vs=clean score=0 state=0
Authentication-Results: xxxx.xxxx.com;
    arc=none (no signatures found);
    dkim=pass (2048-bit rsa key sha256) header.d=xxxx.com header.i=@xxxx.com header.b=P1awJPiy x-bits=2048 x-keytype=rsa x-algorithm=sha256 x-selector=fm2;
    dmarc=fail (p=none,d=none) header.from=xxxx.com;
    iprev=pass policy.iprev=66.111.4.25 (out1-smtp.xxxx.com);
    spf=softfail smtp.mailfrom=xxxx@xxxx.com smtp.helo=out1-smtp.xxxx.com;
    x-aligned-from=pass (Address match);
    x-cm=none score=0;
    x-ptr=pass x-ptr-helo=out1-smtp.xxxx.com x-ptr-lookup=out1-smtp.xxxx.com;
    x-return-mx=pass smtp.domain=xxxx.com smtp.result=pass smtp_is_org_domain=yes header.domain=xxxx.com header.result=pass header_is_org_domain=yes;
    x-tls=pass version=TLSv1.2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128;
    x-vs=clean score=0 state=0
X-ME-VSCategory: clean
X-ME-CMScore: 0
X-ME-CMCategory: none
Received-SPF: softfail
    (gmail.com ... _spf.xxxx.com: Sender is not authorized by default to use 'xxxx@xxxx.com' in 'mfrom' identity, however domain is not currently prepared for false failures (mechanism '~all' matched))
    receiver=xxxx.xxxx.com;
    identity=mailfrom;
    envelope-from="xxxx@xxxx.com";
    helo=out1-smtp.xxxx.com;
    client-ip=1.1.1.1
Received: from xxxx.xxxx.internal (gateway1.xxxx.internal [1.1.1.1])
	(using TLSv1.2 with cipher ECDHE-RSA-AES128-GCM-SHA256 (128/128 bits))
	(No client certificate requested)
	by xxxx.xxxx.internal (Postfix) with ESMTPS;
	Fri, 13 Apr 2018 22:11:51 -0400 (EDT)
Received: from compute3.internal (xxxx.xxxx.internal [10.202.2.43])
	by xxxx.xxxx.internal (Postfix) with ESMTP id 8BD5B21BBD;
	Fri, 13 Apr 2018 22:11:51 -0400 (EDT)
Received: from xxxx ([10.202.2.163])
  by xxxx.internal (MEProxy); Fri, 13 Apr 2018 22:11:51 -0400
X-ME-Sender: <xms:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa>
Received: from [1.1.1.1] (unknown [1.1.1.1])
	by mail.xxxx.com (Postfix) with ESMTPA id BF5E1111D
	for <catchall@xxxx.xxxx>; Fri, 13 Apr 2018 22:11:50 -0400 (EDT)
From: "xxxx xxxx" <xxxx@xxxx.com>
To: "xxxx" <catchall@xxxx.xxxx>
Subject: Re: xxxx (Ref PO1)
Date: Sat, 14 Apr 2018 02:11:42 +0000
Message-Id: <em67f5c44a-xxxx-xxxx-xxxx-69f56d618a94@wswin7hg4n4l1ce>
In-Reply-To: <829228111124527.1111111602.256611118262939-openerp-129-xxxx.xxxx@ip-1-1-1-1>
References: <867911111953277.1523671337.187951111160400-openerp-129-xxxx.xxxx@ip-1-1-1-1>
 <867911111953277.1523671337.256611118262939-openerp-129-xxxx.xxxx@ip-1-1-1-1>
Reply-To: "xxxx xxxx" <xxxx@xxxx.com>
User-Agent: eM_Client/7.0.26687.0
Mime-Version: 1.0
Content-Type: multipart/alternative;
 boundary="------=_MB48E455BD-1111-42EC-1111-886CDF48905E"

--------=_MB48E455BD-1111-42EC-1111-886CDF48905E
Content-Type: text/plain; format=flowed; charset=utf-8
Content-Transfer-Encoding: quoted-printable

xxxx


------ Original Message ------
From: "xxxx" <xxxx@xxxx.com>
To: "xxxx" <xxxx@xxxx.com>
Sent: 4/13/2018 7:06:43 PM
Subject: xxxx

>xxxx

--------=_MB48E455BD-1111-42EC-1111-886CDF48905E
Content-Type: text/html; charset=utf-8
Content-Transfer-Encoding: quoted-printable

<?xml version=3D"1.0" encoding=3D"utf-16"?><html><head><style type=3D"text/=
css"><!--blockquote.cite
{margin-left: 5px; margin-right: 0px; padding-left: 10px; padding-right:=
 0px; border-left-width: 1px; border-left-style: solid; border-left-color:=
 rgb(204, 204, 204);}
blockquote.cite2
{margin-left: 5px; margin-right: 0px; padding-left: 10px; padding-right:=
 0px; border-left-width: 1px; border-left-style: solid; border-left-color:=
 rgb(204, 204, 204); margin-top: 3px; padding-top: 0px;}
a img
{border: 0px;}
body
{font-family: Tahoma; font-size: 12pt;}
--></style></head><body><div>this is a reply to PO200109 from emClient</div=
><div id=3D"signature_old"><div style=3D"font-family: Tahoma; font-size:=
 12 pt;">-- <br /><span><span class=3D"__postbox-detected-content __postbox=
-detected-address" style=3D"TEXT-DECORATION: underline; COLOR: rgb(115,133,=
172); PADDING-BOTTOM: 0pt; PADDING-TOP: 0pt; PADDING-LEFT: 0pt; DISPLAY:=
 inline; PADDING-RIGHT: 0pt" __postbox-detected-content=3D"__postbox-detect=
ed-address"></span>xxxx<br />xxxx<br /><b=
r />xxxx</span></=
div></div><div><br /></div><div><br /></div><div><br /></div>
<div>------ Original Message ------</div>
<div>From: "xxxx" &lt;<a href=3D"mailto:xxxx@xxxx.com">xxxx=
@xxxx.com</a>&gt;</div>
<div>To: "xxxx" &lt;<a href=3D"mailto:xxxx@xxxx.com">a=
xxxx@xxxx.com</a>&gt;</div>
<div>Sent: 4/13/2018 7:06:43 PM</div>
<div>Subject: xxxx</div><div><br /></div=
>
<div id=3D"x00b4101ba6e64ce"><blockquote cite=3D"829228972724527.1523671602=
.256660938262939-openerp-129-xxxx.xxxx@ip-1-1-1-1" type=3D"cite"=
 class=3D"cite2">
<table border=3D"0" width=3D"100%" cellpadding=3D"0" bgcolor=3D"#ededed"=
 style=3D"padding: 20px; background-color: #ededed" summary=3D"o_mail_notif=
ication">
                    <tbody>

                      <!-- HEADER -->
                      <tr>
                        <td align=3D"center" style=3D"min-width: 590px;">
                          <table width=3D"590" border=3D"0" cellpadding=3D=
"0" bgcolor=3D"#875A7B" style=3D"min-width: 590px; background-color: rgb(13=
5,90,123); padding: 20px;">
                            <tbody><tr>
                              <td valign=3D"middle">
                                  <span style=3D"font-size:20px; color:whit=
e; font-weight: bold;">
                                      mangez des saucisses
                                  </span>
                              </td>
                              <td valign=3D"middle" align=3D"right">
                                  <img src=3D"http://erp.xxxx.xxxx/logo.png=
" style=3D"padding: 0px; margin: 0px; height: auto; width: 80px;" alt=3D=
"xxxx" />
                              </td>
                            </tr>
                          </tbody></table>
                        </td>
                      </tr>

                      <!-- CONTENT -->
                      <tr>
                        <td align=3D"center" style=3D"min-width: 590px;">
                          <table width=3D"590" border=3D"0" cellpadding=3D=
"0" bgcolor=3D"#ffffff" style=3D"min-width: 590px; background-color: rgb(25=
5, 255, 255); padding: 20px;">
                            <tbody>
                              <tr><td valign=3D"top" style=3D"font-family:A=
rial,Helvetica,sans-serif; color: #555; font-size: 14px;">
                                <p style=3D"margin: 0px 0px 9px 0px; font-s=
ize: 13px; font-family: &quot;Lucida Grande&quot;, Helvetica, Verdana, Aria=
l, sans-serif">xxxx.=20
,</p>
<p style=3D"margin: 0px 0px 9px 0px; font-size: 13px; font-family: &quot;Lu=
cida Grande&quot;, Helvetica, Verdana, Arial, sans-serif">
xxxx.
</p>

<p style=3D"margin: 0px 0px 9px 0px; font-size: 13px; font-family: &quot;Lu=
cida Grande&quot;, Helvetica, Verdana, Arial, sans-serif">You can reply =
to this email if you have any questions.</p>
<p style=3D"margin: 0px 0px 9px 0px; font-size: 13px; font-family: &quot;Lu=
cida Grande&quot;, Helvetica, Verdana, Arial, sans-serif">Thank you,</p>
                              </td>
                            </tr></tbody>
                          </table>
                        </td>
                      </tr>

                      <!-- FOOTER -->
                      <tr>
                        <td align=3D"center" style=3D"min-width: 590px;">
                          <table width=3D"590" border=3D"0" cellpadding=3D=
"0" bgcolor=3D"#875A7B" style=3D"min-width: 590px; background-color: rgb(13=
5,90,123); padding: 20px;">
                            <tbody><tr>
                              <td valign=3D"middle" align=3D"left" style=
=3D"color: #fff; padding-top: 10px; padding-bottom: 10px; font-size: 12px;"=
>
                                xxxx<br />
                                +1-801-980-4240
                              </td>
                              <td valign=3D"middle" align=3D"right" style=
=3D"color: #fff; padding-top: 10px; padding-bottom: 10px; font-size: 12px;"=
>
                                <a href=3D"http://erp.xxxx.xxxx/info@xxxx-a=
aa.com" style=3D"text-decoration:none; color: white;">info@aust-mfg.com</a>=
<br />
                                    <a href=3D"http://www.xxxx=
.com" style=3D"text-decoration:none; color: white;">
                                        http://www.xxxx.com
                                    </a>
                              </td>
                            </tr>
                          </tbody></table>
                        </td>
                      </tr>
                      <tr>
                        <td align=3D"center">
                            Powered by <a href=3D"https://www.odoo.com">Odo=
o</a>.
                        </td>
                      </tr>
                    </tbody>
                </table>
               =20
                <pre style=3D"white-space: pre-wrap">xxxx.
</pre>
</blockquote></div>
</body></html>
--------=_MB48E455BD-2850-42EC-B1CA-886CDF48905E--"""


class TestMailgateway(TestMail):

    def setUp(self):
        super(TestMailgateway, self).setUp()
        # groups@.. will cause the creation of new mail.channels
        self.mail_channel_model = self.env['ir.model'].search([('model', '=', 'mail.channel')], limit=1)
        self.alias = self.env['mail.alias'].create({
            'alias_name': 'groups',
            'alias_user_id': False,
            'alias_model_id': self.mail_channel_model.id,
            'alias_contact': 'everyone'})

        # Set a first message on public group to test update and hierarchy
        self.fake_email = self.env['mail.message'].create({
            'model': 'mail.channel',
            'res_id': self.group_public.id,
            'subject': 'Public Discussion',
            'message_type': 'email',
            'author_id': self.partner_1.id,
            'message_id': '<123456-openerp-%s-mail.channel@%s>' % (self.group_public.id, socket.gethostname()),
        })

    @mute_logger('openerp.addons.mail.models.mail_thread')
    def test_message_parse(self):
        """ Test parsing of various scenarios of incoming emails """
        res = self.env['mail.thread'].message_parse(MAIL_TEMPLATE_PLAINTEXT)
        self.assertIn('Please call me as soon as possible this afternoon!',
                      res.get('body', ''),
                      'message_parse: missing text in text/plain body after parsing')

        res = self.env['mail.thread'].message_parse(MAIL_TEMPLATE)
        self.assertIn('<p>Please call me as soon as possible this afternoon!</p>',
                      res.get('body', ''),
                      'message_parse: missing html in multipart/alternative body after parsing')

        res = self.env['mail.thread'].message_parse(MAIL_MULTIPART_MIXED)
        self.assertNotIn('Should create a multipart/mixed: from gmail, *bold*, with attachment',
                         res.get('body', ''),
                         'message_parse: text version should not be in body after parsing multipart/mixed')
        self.assertIn('<div dir="ltr">Should create a multipart/mixed: from gmail, <b>bold</b>, with attachment.<br clear="all"><div><br></div>',
                      res.get('body', ''),
                      'message_parse: html version should be in body after parsing multipart/mixed')

        res = self.env['mail.thread'].message_parse(MAIL_MULTIPART_MIXED_TWO)
        self.assertNotIn('First and second part',
                         res.get('body', ''),
                         'message_parse: text version should not be in body after parsing multipart/mixed')
        self.assertIn('First part',
                      res.get('body', ''),
                      'message_parse: first part of the html version should be in body after parsing multipart/mixed')
        self.assertIn('Second part',
                      res.get('body', ''),
                      'message_parse: second part of the html version should be in body after parsing multipart/mixed')

        res = self.env['mail.thread'].message_parse(MAIL_SINGLE_BINARY)
        self.assertEqual(res['body'], '')
        self.assertEqual(res['attachments'][0][0], 'thetruth.pdf')

    @mute_logger('odoo.addons.mail.models.mail_thread')
    def test_message_parse_xhtml(self):
        """ Test that the parsing of mail with embedded emails as eml(msg) which generates empty attachments, can be processed.
        """
        self.env['mail.thread'].message_process('mail.channel', MAIL_XHTML)

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models')
    def test_message_process_alias_basic(self):
        """ Incoming email on an alias creating a new record + message_new + message details """
        new_groups = self.format_and_process(MAIL_TEMPLATE, subject='My Frogs', to='groups@example.com, other@gmail.com')

        # Test: one group created by mailgateway administrator
        self.assertEqual(len(new_groups), 1, 'message_process: a new mail.channel should have been created')
        res = new_groups.get_metadata()[0].get('create_uid') or [None]
        self.assertEqual(res[0], self.env.uid,
                         'message_process: group should have been created by uid as alias_user_id is False on the alias')

        # Test: one message that is the incoming email
        self.assertEqual(len(new_groups.message_ids), 1,
                         'message_process: newly created group should have the incoming email in message_ids')
        msg = new_groups.message_ids[0]
        self.assertEqual(msg.subject, 'My Frogs',
                         'message_process: newly created group should have the incoming email as first message')
        self.assertIn('Please call me as soon as possible this afternoon!', msg.body,
                      'message_process: newly created group should have the incoming email as first message')
        self.assertEqual(msg.message_type, 'email',
                         'message_process: newly created group should have an email as first message')
        self.assertEqual(msg.subtype_id, self.env.ref('mail.mt_comment'),
                         'message_process: newly created group should not have a log first message but an email')

        # Test: sent emails: no-one
        self.assertEqual(len(self._mails), 0,
                         'message_process: should create emails without any follower added')

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models')
    def test_message_process_alias_user_id(self):
        """ Test alias ownership """
        self.alias.write({'alias_user_id': self.user_employee.id})
        new_groups = self.format_and_process(MAIL_TEMPLATE, to='groups@example.com, other@gmail.com')

        # Test: one group created by mailgateway administrator
        self.assertEqual(len(new_groups), 1, 'message_process: a new mail.channel should have been created')
        res = new_groups.get_metadata()[0].get('create_uid') or [None]
        self.assertEqual(res[0], self.user_employee.id,
                         'message_process: group should have been created by alias_user_id')

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models')
    def test_message_process_email_email_from(self):
        """ Incoming email: not recognized author: email_from, no author_id, no followers """
        new_groups = self.format_and_process(MAIL_TEMPLATE, to='groups@example.com, other@gmail.com')

        self.assertFalse(new_groups.message_ids[0].author_id,
                         'message_process: unrecognized email -> no author_id')
        self.assertIn('test.sylvie.lelitre@agrolait.com', new_groups.message_ids[0].email_from,
                      'message_process: unrecognized email -> email_from')

        self.assertEqual(len(new_groups.message_partner_ids), 0,
                         'message_process: newly create group should not have any follower')

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models')
    def test_message_process_email_author(self):
        """ Incoming email: recognized author: email_from, author_id, added as follower """
        new_groups = self.format_and_process(MAIL_TEMPLATE, email_from='Valid Lelitre <valid.lelitre@agrolait.com>', to='groups@example.com, valid.other@gmail.com')

        self.assertEqual(new_groups.message_ids[0].author_id, self.partner_1,
                         'message_process: recognized email -> author_id')
        self.assertIn('Valid Lelitre <valid.lelitre@agrolait.com>', new_groups.message_ids[0].email_from,
                      'message_process: recognized email -> email_from')

        # TODO : the author of a message post on mail.channel should not be added as follower
        # FAIL ON recognized email -> added as follower')
        # self.assertEqual(new_groups.message_partner_ids, self.partner_1,
        #                  'message_process: recognized email -> added as follower')

        self.assertEqual(len(self._mails), 0,
                         'message_process: no bounce or notificatoin email should be sent with follower = author')

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models', 'openerp.addons.mail.models.mail_mail')
    def test_message_process_alias_partners_bounce(self):
        """ Incoming email from an unknown partner on a Partners only alias -> bounce """
        self.alias.write({'alias_contact': 'partners'})

        # Test: no group created, email bounced
        new_groups = self.format_and_process(MAIL_TEMPLATE, subject='New Frogs', to='groups@example.com, other@gmail.com')
        self.assertTrue(len(new_groups) == 0)
        self.assertEqual(len(self._mails), 1,
                         'message_process: incoming email on Partners alias should send a bounce email')
        self.assertIn('New Frogs', self._mails[0].get('subject'),
                      'message_process: bounce email on Partners alias should contain the original subject')
        self.assertIn('whatever-2a840@postmaster.twitter.com', self._mails[0].get('email_to'),
                      'message_process: bounce email on Partners alias should go to Return-Path address')

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models', 'openerp.addons.mail.models.mail_mail')
    def test_message_process_alias_followers_bounce(self):
        """ Incoming email from unknown partner / not follower partner on a Followers only alias -> bounce """
        self.alias.write({
            'alias_contact': 'followers',
            'alias_parent_model_id': self.mail_channel_model.id,
            'alias_parent_thread_id': self.group_pigs.id})

        # Test: unknown on followers alias -> bounce
        new_groups = self.format_and_process(MAIL_TEMPLATE, to='groups@example.com, other@gmail.com')
        self.assertEqual(len(new_groups), 0, 'message_process: should have bounced')
        self.assertEqual(len(self._mails), 1,
                         'message_process: incoming email on Followers alias should send a bounce email')

        # Test: partner on followers alias -> bounce
        self._init_mock_build_email()
        new_groups = self.format_and_process(MAIL_TEMPLATE, email_from='Valid Lelitre <valid.lelitre@agrolait.com>', to='groups@example.com, other@gmail.com')
        self.assertTrue(len(new_groups) == 0, 'message_process: should have bounced')
        self.assertEqual(len(self._mails), 1,
                         'message_process: incoming email on Followers alias should send a bounce email')

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models')
    def test_message_process_alias_partner(self):
        """ Incoming email from a known partner on a Partners alias -> ok (+ test on alias.user_id) """
        self.alias.write({'alias_contact': 'partners'})
        new_groups = self.format_and_process(MAIL_TEMPLATE, email_from='Valid Lelitre <valid.lelitre@agrolait.com>', to='groups@example.com, valid.other@gmail.com')

        # Test: one group created by alias user
        self.assertEqual(len(new_groups), 1, 'message_process: a new mail.channel should have been created')

        # Test: one message that is the incoming email
        self.assertEqual(len(new_groups.message_ids), 1,
                         'message_process: newly created group should have the incoming email in message_ids')

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models')
    def test_message_process_alias_followers(self):
        """ Incoming email from a parent document follower on a Followers only alias -> ok """
        self.alias.write({
            'alias_contact': 'followers',
            'alias_parent_model_id': self.mail_channel_model.id,
            'alias_parent_thread_id': self.group_pigs.id})
        self.group_pigs.message_subscribe(partner_ids=[self.partner_1.id])
        new_groups = self.format_and_process(MAIL_TEMPLATE, email_from='Valid Lelitre <valid.lelitre@agrolait.com>', to='groups@example.com, other6@gmail.com')

        # Test: one group created by Raoul (or Sylvie maybe, if we implement it)
        self.assertEqual(len(new_groups), 1, 'message_process: a new mail.channel should have been created')

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models', 'openerp.addons.mail.models.mail_mail')
    def test_message_process_alias_update(self):
        """ Incoming email update discussion + notification email """
        self.alias.write({'alias_force_thread_id': self.group_public.id})

        self.group_public.message_subscribe(partner_ids=[self.partner_1.id])
        new_groups = self.format_and_process(
            MAIL_TEMPLATE, email_from='valid.other@gmail.com',
            msg_id='<1198923581.41972151344608186799.JavaMail.diff1@agrolait.com>',
            to='groups@example.com>', subject='Re: cats')

        # Test: no new group + new message
        self.assertEqual(len(new_groups), 0,
                         'message_process: reply on Frogs should not have created a new group with new subject')
        self.assertEqual(len(self.group_public.message_ids), 2, 'message_process: group should contain one new message')
        # Test: sent emails: 1 (Sylvie copy of the incoming email)
        self.assertEqual(len(self._mails), 1,
                         'message_process: one email should have been generated')
        self.assertIn('valid.lelitre@agrolait.com', self._mails[0].get('email_to')[0],
                      'message_process: email should be sent to Sylvie')

        # TODO : the author of a message post on mail.channel should not be added as follower
        # FAIL ON 'message_process: after reply, group should have 2 followers') ` AssertionError: res.partner(104,) != res.partner(104, 105) : message_process: after reply, group should have 2 followers

        # Test: author (and not recipient) added as follower
        # self.assertEqual(self.group_public.message_partner_ids, self.partner_1 | self.partner_2,
        #                  'message_process: after reply, group should have 2 followers')
        # self.assertEqual(self.group_public.message_channel_ids, self.env['mail.channel'],
        #                  'message_process: after reply, group should have 2 followers (0 channels)')

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models')
    def test_message_process_in_reply_to(self):
        """ Incoming email using in-rely-to should go into the right destination event with a wrong destination """
        self.format_and_process(
            MAIL_TEMPLATE, email_from='valid.other@gmail.com',
            msg_id='<1198923581.41972151344608186800.JavaMail.diff1@agrolait.com>',
            to='erroneous@example.com>', subject='Re: news',
            extra='In-Reply-To:\r\n\t%s\n' % self.fake_email.message_id)

        self.assertEqual(len(self.group_public.message_ids), 2, 'message_process: group should contain one new message')
        self.assertEqual(len(self.fake_email.child_ids), 1, 'message_process: new message should be children of the existing one')

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models')
    def test_message_process_references(self):
        """ Incoming email using in-rely-to should go into the right destination event with a wrong destination """
        self.format_and_process(
            MAIL_TEMPLATE, to='erroneous@example.com',
            extra='References: <2233@a.com>\r\n\t<3edss_dsa@b.com> %s' % self.fake_email.message_id,
            msg_id='<1198923581.41972151344608186800.JavaMail.4@agrolait.com>')

        self.assertEqual(len(self.group_public.message_ids), 2, 'message_process: group should contain one new message')
        self.assertEqual(len(self.fake_email.child_ids), 1, 'message_process: new message should be children of the existing one')

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models')
    def test_message_process_model_res_id(self):
        """ Incoming email with ref holding model / res_id but that does not match any message in the thread: must raise since OpenERP saas-3 """
        self.assertRaises(ValueError,
                          self.format_and_process,
                          MAIL_TEMPLATE, email_from='valid.lelitre@agrolait.com',
                          to='noone@example.com', subject='spam',
                          extra='In-Reply-To: <12321321-openerp-%d-mail.channel@%s>' % (self.group_public.id, socket.gethostname()),
                          msg_id='<1198923581.41972151344608186802.JavaMail.diff1@agrolait.com>')

        # when 6.1 messages are present, compat mode is available
        self.fake_email.write({'message_id': False})
        # Do: compat mode accepts partial-matching emails
        frog_groups = self.format_and_process(
            MAIL_TEMPLATE, email_from='other5@gmail.com',
            msg_id='<1.2.JavaMail.new@agrolait.com>',
            to='noone@example.com>', subject='spam',
            extra='In-Reply-To: <12321321-openerp-%d-mail.channel@%s>' % (self.group_public.id, socket.gethostname()))

        # 3''. 6.1 compat mode should not work if hostname does not match!
        self.assertRaises(ValueError,
                          self.format_and_process,
                          MAIL_TEMPLATE, email_from='other5@gmail.com',
                          msg_id='<1.3.JavaMail.new@agrolait.com>',
                          to='noone@example.com>', subject='spam',
                          extra='In-Reply-To: <12321321-openerp-%d-mail.channel@neighbor.com>' % frog_groups.id)

        # 4. Subject contains [<ID>] + model passed to message+process -> only attached to group, but not to mail (not in msg1.child_ids)
        self.format_and_process(
            MAIL_TEMPLATE,
            to='erroneous@example.com', email_from='other6@gmail.com',
            extra='', subject='Re: [%s] 1' % self.group_public.id, model='mail.channel',
            msg_id='<1198923581.41972151344608186803.JavaMail.5@agrolait.com>')

        # Test created messages
        self.assertEqual(len(self.group_public.message_ids), 3, 'message_process: group should contain 6 messages')
        self.assertEqual(len(self.group_public.message_ids[0].child_ids), 0, 'message_process: msg1 should not have children')

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models')
    def test_message_process_duplicate(self):
        """ Duplicate emails (same message_id) are not processed """
        self.alias.write({'alias_force_thread_id': self.group_public.id,})

        # Post a base message
        frog_groups = self.format_and_process(
            MAIL_TEMPLATE, email_from='valid.other@gmail.com', subject='Re: super cats',
            msg_id='<1198923581.41972151344608186799.JavaMail.diff1@agrolait.com>')

        # Do: due to some issue, same email goes back into the mailgateway
        frog_groups = self.format_and_process(
            MAIL_TEMPLATE, email_from='other4@gmail.com', subject='Re: news',
            msg_id='<1198923581.41972151344608186799.JavaMail.diff1@agrolait.com>',
            extra='In-Reply-To: <1198923581.41972151344608186799.JavaMail.diff1@agrolait.com>\n')

        # Test: no group 'Re: news' created, still only 1 Frogs group
        self.assertEqual(len(frog_groups), 0,
                         'message_process: reply on Frogs should not have created a new group with new subject')

        # Test: no new message
        self.assertEqual(len(self.group_public.message_ids), 2, 'message_process: message with already existing message_id should not have been duplicated')
        # Test: message_id is still unique
        no_of_msg = self.env['mail.message'].search_count([('message_id', 'ilike', '<1198923581.41972151344608186799.JavaMail.diff1@agrolait.com>')])
        self.assertEqual(no_of_msg, 1,
                         'message_process: message with already existing message_id should not have been duplicated')

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models')
    def test_message_process_partner_find(self):
        """ Finding the partner based on email, based on partner / user / follower """
        from_1 = self.env['res.partner'].create({'name': 'A', 'email': 'from.test@example.com'})

        self.format_and_process(MAIL_TEMPLATE, to='public@example.com', msg_id='<1>', email_from='Brice Denisse <from.test@example.com>')
        self.assertEqual(self.group_public.message_ids[0].author_id, from_1, 'message_process: email_from -> author_id wrong')
        self.group_public.message_unsubscribe([from_1.id])

        from_2 = self.env['res.users'].with_context({'no_reset_password': True}).create({'name': 'B', 'login': 'B', 'email': 'from.test@example.com'})

        self.format_and_process(MAIL_TEMPLATE, to='public@example.com', msg_id='<2>', email_from='Brice Denisse <from.test@example.com>')
        self.assertEqual(self.group_public.message_ids[0].author_id, from_2.partner_id, 'message_process: email_from -> author_id wrong')
        self.group_public.message_unsubscribe([from_2.partner_id.id])

        from_3 = self.env['res.partner'].create({'name': 'C', 'email': 'from.test@example.com'})
        self.group_public.message_subscribe([from_3.id])

        self.format_and_process(MAIL_TEMPLATE, to='public@example.com', msg_id='<3>', email_from='Brice Denisse <from.test@example.com>')
        self.assertEqual(self.group_public.message_ids[0].author_id, from_3, 'message_process: email_from -> author_id wrong')

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models')
    def test_message_process_crash_wrong_model(self):
        """ Incoming email with model that does not accepts incoming emails must raise """
        self.assertRaises(ValueError,
                          self.format_and_process,
                          MAIL_TEMPLATE,
                          to='noone@example.com', subject='spam', extra='', model='res.country',
                          msg_id='<1198923581.41972151344608186760.JavaMail.new4@agrolait.com>')

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models')
    def test_message_process_crash_no_data(self):
        """ Incoming email without model and without alias must raise """
        self.assertRaises(ValueError,
                          self.format_and_process,
                          MAIL_TEMPLATE,
                          to='noone@example.com', subject='spam', extra='',
                          msg_id='<1198923581.41972151344608186760.JavaMail.new5@agrolait.com>')

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models')
    def test_message_process_fallback(self):
        """ Incoming email with model that accepting incoming emails as fallback """
        frog_groups = self.format_and_process(
            MAIL_TEMPLATE, to='noone@example.com', subject='Spammy', extra='', model='mail.channel',
            msg_id='<1198923581.41972151344608186760.JavaMail.new6@agrolait.com>')
        self.assertEqual(len(frog_groups), 1,
                         'message_process: erroneous email but with a fallback model should have created a new mail.channel')

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models')
    def test_message_process_plain_text(self):
        """ Incoming email in plaintext should be stored as html """
        frog_groups = self.format_and_process(
            MAIL_TEMPLATE_PLAINTEXT, to='groups@example.com', subject='Frogs Return', extra='',
            msg_id='<deadcafe.1337@smtp.agrolait.com>')
        self.assertEqual(len(frog_groups), 1, 'message_process: a new mail.channel should have been created')
        msg = frog_groups.message_ids[0]
        self.assertIn('<pre>\nPlease call me as soon as possible this afternoon!\n\n--\nSylvie\n</pre>', msg.body,
                      'message_process: plaintext incoming email incorrectly parsed')

    @mute_logger('openerp.addons.mail.models.mail_thread', 'openerp.models', 'openerp.addons.mail.models.mail_mail')
    def test_private_discussion(self):
        """ Testing private discussion between partners. """
        msg1_pids = [self.env.user.partner_id.id, self.partner_1.id]

        # Do: Raoul writes to Bert and Administrator, with a thread_model in context that should not be taken into account
        msg1 = self.env['mail.thread'].with_context({
            'thread_model': 'mail.channel'
        }).sudo(self.user_employee).message_post(partner_ids=msg1_pids, subtype='mail.mt_comment')

        # Test: message recipients
        msg = self.env['mail.message'].browse(msg1.id)
        self.assertEqual(msg.partner_ids, self.env.user.partner_id | self.partner_1,
                         'message_post: private discussion: incorrect recipients')
        self.assertEqual(msg.model, False,
                         'message_post: private discussion: context key "thread_model" not correctly ignored when having no res_id')
        # Test: message-id
        self.assertIn('openerp-private', msg.message_id, 'message_post: private discussion: message-id should contain the private keyword')

        # Do: Bert replies through mailgateway (is a customer)
        self.format_and_process(
            MAIL_TEMPLATE, to='not_important@mydomain.com', email_from='valid.lelitre@agrolait.com',
            extra='In-Reply-To: %s' % msg.message_id, msg_id='<test30.JavaMail.0@agrolait.com>')

        # Test: last mail_message created
        msg2 = self.env['mail.message'].search([], limit=1)
        # Test: message recipients
        self.assertEqual(msg2.author_id, self.partner_1,
                         'message_post: private discussion: wrong author through mailgatewya based on email')
        self.assertEqual(msg2.partner_ids, self.user_employee.partner_id | self.env.user.partner_id,
                         'message_post: private discussion: incorrect recipients when replying')

        # Do: Bert replies through chatter (is a customer)
        msg3 = self.env['mail.thread'].message_post(author_id=self.partner_1.id, parent_id=msg1.id, subtype='mail.mt_comment')

        # Test: message recipients
        msg = self.env['mail.message'].browse(msg3.id)
        self.assertEqual(msg.partner_ids, self.user_employee.partner_id | self.env.user.partner_id,
                         'message_post: private discussion: incorrect recipients when replying')
        self.assertEqual(msg.needaction_partner_ids, self.user_employee.partner_id | self.env.user.partner_id,
                         'message_post: private discussion: incorrect notified recipients when replying')

        # Do bert forward it to an alias
        msg = self.env['mail.message'].browse(msg1.id)
        # forward it to a new thread AND an existing thread
        for i, to in enumerate(['groups', 'public']):
            fw_msg_id = '<THIS.IS.A.FW.MESSAGE.%d@bert.fr>' % (i,)
            fw_message = MAIL_TEMPLATE.format(to='%s@example.com' % (to,),
                                              cc='',
                                              subject='FW: Re: 1',
                                              email_from='b.t@example.com',
                                              extra='References: %s' % msg.message_id,
                                              msg_id=fw_msg_id)
            self.env['mail.thread'].message_process(None, fw_message)

            msg_fw = self.env['mail.message'].search([('message_id', '=', fw_msg_id)])
            self.assertEqual(len(msg_fw), 1)

            self.assertEqual(msg_fw.model, 'mail.channel')
            self.assertFalse(msg_fw.parent_id)
