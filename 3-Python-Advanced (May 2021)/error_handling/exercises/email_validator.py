from error_handling.exercises.custom_exceptions import NameTooShort, MustContainAtSymbolError, InvalidDomainError
from error_handling.exercises.helpers import VALID_DOMAINS


def valid_email(email):
    try:
        name, domain = email.split('@')
    except ValueError:
        if '@' not in email:
            raise MustContainAtSymbolError("Email must contain @")

    try:
        domain_name, extension = email.split('.')
    except ValueError:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if extension not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if len(name) < 4:
        raise NameTooShort("Name must be more than 4 characters")


email = input()

while not email == "End":
    # TODO VALIDATE EMAIL
    if valid_email(email):
        print("Email is valid")
    email = input()

