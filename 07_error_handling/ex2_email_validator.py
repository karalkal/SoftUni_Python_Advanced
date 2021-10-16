class NameTooShortError(Exception):
    """Name must be more than 4 characters"""
    pass


class MustContainAtSymbolError(Exception):
    """Email must contain @"""
    pass


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""
    pass


while True:
    current_email = input()
    if current_email == "End":
        break

    try:  # first check if there is "@" at all
        position_of_at_sign = current_email.index("@")

        if position_of_at_sign < 4:  # then check its position - "@" cannot be before index 4
            raise NameTooShortError("Name must be more than 4 characters")

    except ValueError:
        raise MustContainAtSymbolError("Email must contain @") from None

    # find content of text after last dot
    split_email = current_email.split(".")
    top_level_domain = split_email[-1]
    if top_level_domain not in ["com", "bg", "org", "net"]:
        raise InvalidDomainError("InvalidDomainError - Domain must be one of the following: .com, .bg, .org, .net")

    # if no errors have been raised up to this point
    print("Email is valid")
