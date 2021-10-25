def parse(string):
    ip, mask = string.split("/")

    # calculate the ip number
    ip = [int(nb) for nb in ip.split(".")]
    ip_nb = int((ip[0]<<24) | (ip[1]<<16) | (ip[2]<<8) | (ip[3]))

    # calculate the mask number
    mask = int(mask)
    mask_nb = int("1"*mask + "0"*(32 - mask), 2)

    return ip_nb, mask_nb


def unparse(number):
    return (
        str((number>>24) & 255) + "." +
        str((number>>16) & 255) + "." +
        str((number>>8) & 255) + "." +
        str(number & 255)
    )


def network_address(ip_number, mask_number):
    return ip_number & mask_number

def wildcard_address(ip_mask):
    return ~ip_mask


def broadcast_address(ip_number, wildcard_number):
    return ip_number | wildcard_number


ip = parse(input())

print(unparse(network_address(ip[0], ip[1])))
print(unparse(broadcast_address(ip[0], wildcard_address(ip[1]))))