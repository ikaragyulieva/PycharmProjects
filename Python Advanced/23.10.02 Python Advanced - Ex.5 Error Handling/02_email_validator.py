class NameTooShortError(Exception):
    """Name must be more than 4 characters"""
    pass


class MustContainAtSymbolError(Exception):
    """Email must contain @"""
    pass


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""
    pass


email = input()
domains = ['.com', '.bg', '.org', '.net']
correct_domain = False

while email != 'End':

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    at_index = email.find('@')
    if at_index < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    for i in domains:
        if i in email:
           correct_domain = True

    if not correct_domain:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    email = input()

