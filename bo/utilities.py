

def format_tel(phone):
    if phone != "":
        phone = phone.replace("-", "")
        return format(int(phone[:-1]), ",").replace(",", "-") + phone[-1]
    else:
        return ""