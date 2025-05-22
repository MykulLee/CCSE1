# ZAP Scanning Report

ZAP by [Checkmarx](https://checkmarx.com/).


## Summary of Alerts

| Risk Level | Number of Alerts |
| --- | --- |
| High | 0 |
| Medium | 2 |
| Low | 2 |
| Informational | 2 |




## Alerts

| Name | Risk Level | Number of Instances |
| --- | --- | --- |
| Absence of Anti-CSRF Tokens | Medium | 8 |
| Content Security Policy (CSP) Header Not Set | Medium | 7 |
| Permissions Policy Header Not Set | Low | 8 |
| Server Leaks Version Information via "Server" HTTP Response Header Field | Low | 8 |
| Modern Web Application | Informational | 8 |
| Non-Storable Content | Informational | 8 |




## Alert Detail



### [ Absence of Anti-CSRF Tokens ](https://www.zaproxy.org/docs/alerts/10202/)



##### Medium (Low)

### Description

No Anti-CSRF tokens were found in a HTML submission form.
A cross-site request forgery is an attack that involves forcing a victim to send an HTTP request to a target destination without their knowledge or intent in order to perform an action as the victim. The underlying cause is application functionality using predictable URL/form actions in a repeatable way. The nature of the attack is that CSRF exploits the trust that a web site has for a user. By contrast, cross-site scripting (XSS) exploits the trust that a user has for a web site. Like XSS, CSRF attacks are not necessarily cross-site, but they can be. Cross-site request forgery is also known as CSRF, XSRF, one-click attack, session riding, confused deputy, and sea surf.

CSRF attacks are effective in a number of situations, including:
    * The victim has an active session on the target site.
    * The victim is authenticated via HTTP auth on the target site.
    * The victim is on the same local network as the target site.

CSRF has primarily been used to perform an action against a target site using the victim's privileges, but recent techniques have been discovered to disclose information by gaining access to the response. The risk of information disclosure is dramatically increased when the target site is vulnerable to XSS, because XSS can be used as a platform for CSRF, allowing the attack to operate within the bounds of the same-origin policy.

* URL: http://host.docker.internal:8000
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token, _csrfToken] was found in the following HTML form: [Form 1: "language" "poster" "source" "title" ].`
* URL: http://host.docker.internal:8000/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token, _csrfToken] was found in the following HTML form: [Form 1: "language" "poster" "source" "title" ].`
* URL: http://host.docker.internal:8000/robots.txt
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token, _csrfToken] was found in the following HTML form: [Form 1: "language" "poster" "source" "title" ].`
* URL: http://host.docker.internal:8000/sitemap.xml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token, _csrfToken] was found in the following HTML form: [Form 1: "language" "poster" "source" "title" ].`
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/core/handlers/exception.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token, _csrfToken] was found in the following HTML form: [Form 1: "language" "poster" "source" "title" ].`
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/http/request.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token, _csrfToken] was found in the following HTML form: [Form 1: "language" "poster" "source" "title" ].`
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/middleware/common.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token, _csrfToken] was found in the following HTML form: [Form 1: "language" "poster" "source" "title" ].`
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/utils/deprecation.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token, _csrfToken] was found in the following HTML form: [Form 1: "language" "poster" "source" "title" ].`

Instances: 8

### Solution

Phase: Architecture and Design
Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid.
For example, use anti-CSRF packages such as the OWASP CSRFGuard.

Phase: Implementation
Ensure that your application is free of cross-site scripting issues, because most CSRF defenses can be bypassed using attacker-controlled script.

Phase: Architecture and Design
Generate a unique nonce for each form, place the nonce into the form, and verify the nonce upon receipt of the form. Be sure that the nonce is not predictable (CWE-330).
Note that this can be bypassed using XSS.

Identify especially dangerous operations. When the user performs a dangerous operation, send a separate confirmation request to ensure that the user intended to perform that operation.
Note that this can be bypassed using XSS.

Use the ESAPI Session Management control.
This control includes a component for CSRF.

Do not use the GET method for any request that triggers a state change.

Phase: Implementation
Check the HTTP Referer header to see if the request originated from an expected page. This could break legitimate functionality, because users or proxies may have disabled sending the Referer for privacy reasons.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [ https://cwe.mitre.org/data/definitions/352.html ](https://cwe.mitre.org/data/definitions/352.html)


#### CWE Id: [ 352 ](https://cwe.mitre.org/data/definitions/352.html)


#### WASC Id: 9

#### Source ID: 3

### [ Content Security Policy (CSP) Header Not Set ](https://www.zaproxy.org/docs/alerts/10038/)



##### Medium (High)

### Description

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

* URL: http://host.docker.internal:8000
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://host.docker.internal:8000/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://host.docker.internal:8000/sitemap.xml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/core/handlers/exception.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/http/request.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/middleware/common.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/utils/deprecation.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: 7

### Solution

Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/Security/CSP/Introducing_Content_Security_Policy ](https://developer.mozilla.org/en-US/docs/Web/Security/CSP/Introducing_Content_Security_Policy)
* [ https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [ https://www.w3.org/TR/CSP/ ](https://www.w3.org/TR/CSP/)
* [ https://w3c.github.io/webappsec-csp/ ](https://w3c.github.io/webappsec-csp/)
* [ https://web.dev/articles/csp ](https://web.dev/articles/csp)
* [ https://caniuse.com/#feat=contentsecuritypolicy ](https://caniuse.com/#feat=contentsecuritypolicy)
* [ https://content-security-policy.com/ ](https://content-security-policy.com/)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Permissions Policy Header Not Set ](https://www.zaproxy.org/docs/alerts/10063/)



##### Low (Medium)

### Description

Permissions Policy Header is an added layer of security that helps to restrict from unauthorized access or usage of browser/client features by web resources. This policy ensures the user privacy by limiting or specifying the features of the browsers can be used by the web resources. Permissions Policy provides a set of standard HTTP headers that allow website owners to limit which features of browsers can be used by the page such as camera, microphone, location, full screen etc.

* URL: http://host.docker.internal:8000
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://host.docker.internal:8000/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://host.docker.internal:8000/robots.txt
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://host.docker.internal:8000/sitemap.xml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/core/handlers/exception.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/http/request.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/middleware/common.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/utils/deprecation.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: 8

### Solution

Ensure that your web server, application server, load balancer, etc. is configured to set the Permissions-Policy header.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Permissions-Policy ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Permissions-Policy)
* [ https://developer.chrome.com/blog/feature-policy/ ](https://developer.chrome.com/blog/feature-policy/)
* [ https://scotthelme.co.uk/a-new-security-header-feature-policy/ ](https://scotthelme.co.uk/a-new-security-header-feature-policy/)
* [ https://w3c.github.io/webappsec-feature-policy/ ](https://w3c.github.io/webappsec-feature-policy/)
* [ https://www.smashingmagazine.com/2018/12/feature-policy/ ](https://www.smashingmagazine.com/2018/12/feature-policy/)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Server Leaks Version Information via "Server" HTTP Response Header Field ](https://www.zaproxy.org/docs/alerts/10036/)



##### Low (High)

### Description

The web/application server is leaking version information via the "Server" HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

* URL: http://host.docker.internal:8000
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `WSGIServer/0.2 CPython/3.13.1`
  * Other Info: ``
* URL: http://host.docker.internal:8000/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `WSGIServer/0.2 CPython/3.13.1`
  * Other Info: ``
* URL: http://host.docker.internal:8000/robots.txt
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `WSGIServer/0.2 CPython/3.13.1`
  * Other Info: ``
* URL: http://host.docker.internal:8000/sitemap.xml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `WSGIServer/0.2 CPython/3.13.1`
  * Other Info: ``
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/core/handlers/exception.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `WSGIServer/0.2 CPython/3.13.1`
  * Other Info: ``
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/http/request.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `WSGIServer/0.2 CPython/3.13.1`
  * Other Info: ``
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/middleware/common.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `WSGIServer/0.2 CPython/3.13.1`
  * Other Info: ``
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/utils/deprecation.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `WSGIServer/0.2 CPython/3.13.1`
  * Other Info: ``

Instances: 8

### Solution

Ensure that your web server, application server, load balancer, etc. is configured to suppress the "Server" header or provide generic details.

### Reference


* [ https://httpd.apache.org/docs/current/mod/core.html#servertokens ](https://httpd.apache.org/docs/current/mod/core.html#servertokens)
* [ https://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff648552(v=pandp.10) ](https://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff648552(v=pandp.10))
* [ https://www.troyhunt.com/shhh-dont-let-your-response-headers/ ](https://www.troyhunt.com/shhh-dont-let-your-response-headers/)


#### CWE Id: [ 497 ](https://cwe.mitre.org/data/definitions/497.html)


#### WASC Id: 13

#### Source ID: 3

### [ Modern Web Application ](https://www.zaproxy.org/docs/alerts/10109/)



##### Informational (Medium)

### Description

The application appears to be a modern web application. If you need to explore it automatically then the Ajax Spider may well be more effective than the standard one.

* URL: http://host.docker.internal:8000
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<a href="#" onclick="return switchPastebinFriendly(this);">
    Switch to copy-and-paste view</a>`
  * Other Info: `Links have been found that do not have traditional href attributes, which is an indication that this is a modern web application.`
* URL: http://host.docker.internal:8000/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<a href="#" onclick="return switchPastebinFriendly(this);">
    Switch to copy-and-paste view</a>`
  * Other Info: `Links have been found that do not have traditional href attributes, which is an indication that this is a modern web application.`
* URL: http://host.docker.internal:8000/robots.txt
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<a href="#" onclick="return switchPastebinFriendly(this);">
    Switch to copy-and-paste view</a>`
  * Other Info: `Links have been found that do not have traditional href attributes, which is an indication that this is a modern web application.`
* URL: http://host.docker.internal:8000/sitemap.xml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<a href="#" onclick="return switchPastebinFriendly(this);">
    Switch to copy-and-paste view</a>`
  * Other Info: `Links have been found that do not have traditional href attributes, which is an indication that this is a modern web application.`
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/core/handlers/exception.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<a href="#" onclick="return switchPastebinFriendly(this);">
    Switch to copy-and-paste view</a>`
  * Other Info: `Links have been found that do not have traditional href attributes, which is an indication that this is a modern web application.`
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/http/request.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<a href="#" onclick="return switchPastebinFriendly(this);">
    Switch to copy-and-paste view</a>`
  * Other Info: `Links have been found that do not have traditional href attributes, which is an indication that this is a modern web application.`
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/middleware/common.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<a href="#" onclick="return switchPastebinFriendly(this);">
    Switch to copy-and-paste view</a>`
  * Other Info: `Links have been found that do not have traditional href attributes, which is an indication that this is a modern web application.`
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/utils/deprecation.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<a href="#" onclick="return switchPastebinFriendly(this);">
    Switch to copy-and-paste view</a>`
  * Other Info: `Links have been found that do not have traditional href attributes, which is an indication that this is a modern web application.`

Instances: 8

### Solution

This is an informational alert and so no changes are required.

### Reference




#### Source ID: 3

### [ Non-Storable Content ](https://www.zaproxy.org/docs/alerts/10049/)



##### Informational (Medium)

### Description

The response contents are not storable by caching components such as proxy servers. If the response does not contain sensitive, personal or user-specific information, it may benefit from being stored and cached, to improve performance.

* URL: http://host.docker.internal:8000
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `400`
  * Other Info: ``
* URL: http://host.docker.internal:8000/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `400`
  * Other Info: ``
* URL: http://host.docker.internal:8000/robots.txt
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `400`
  * Other Info: ``
* URL: http://host.docker.internal:8000/sitemap.xml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `400`
  * Other Info: ``
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/core/handlers/exception.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `400`
  * Other Info: ``
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/http/request.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `400`
  * Other Info: ``
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/middleware/common.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `400`
  * Other Info: ``
* URL: http://host.docker.internal:8000/Users/michaellee/.local/share/virtualenvs/cw2-WQhAPzPd/lib/python3.13/site-packages/django/utils/deprecation.py,
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `400`
  * Other Info: ``

Instances: 8

### Solution

The content may be marked as storable by ensuring that the following conditions are satisfied:
The request method must be understood by the cache and defined as being cacheable ("GET", "HEAD", and "POST" are currently defined as cacheable)
The response status code must be understood by the cache (one of the 1XX, 2XX, 3XX, 4XX, or 5XX response classes are generally understood)
The "no-store" cache directive must not appear in the request or response header fields
For caching by "shared" caches such as "proxy" caches, the "private" response directive must not appear in the response
For caching by "shared" caches such as "proxy" caches, the "Authorization" header field must not appear in the request, unless the response explicitly allows it (using one of the "must-revalidate", "public", or "s-maxage" Cache-Control response directives)
In addition to the conditions above, at least one of the following conditions must also be satisfied by the response:
It must contain an "Expires" header field
It must contain a "max-age" response directive
For "shared" caches such as "proxy" caches, it must contain a "s-maxage" response directive
It must contain a "Cache Control Extension" that allows it to be cached
It must have a status code that is defined as cacheable by default (200, 203, 204, 206, 300, 301, 404, 405, 410, 414, 501).

### Reference


* [ https://datatracker.ietf.org/doc/html/rfc7234 ](https://datatracker.ietf.org/doc/html/rfc7234)
* [ https://datatracker.ietf.org/doc/html/rfc7231 ](https://datatracker.ietf.org/doc/html/rfc7231)
* [ https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html ](https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html)


#### CWE Id: [ 524 ](https://cwe.mitre.org/data/definitions/524.html)


#### WASC Id: 13

#### Source ID: 3


