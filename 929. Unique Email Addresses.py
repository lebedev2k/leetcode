from typing import List
def numUniqueEmails(emails: List[str]) -> int:
    res = set()
    for email in emails:
        email = email.split("@")
        email[0] = email[0].split("+")[0]
        email[0] = email[0].replace(".", "")
        res.add(email[0]+'@'+email[1])
    return len(res)



assert numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]) == 2
assert numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]) == 3