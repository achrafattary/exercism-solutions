from asyncio.windows_events import NULL


def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    return (coordinate[0],coordinate[1])


def compare_records(azara_record, rui_record):
    return convert_coordinate(azara_record[1]) == rui_record[1]

def create_record(azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """
    if compare_records(azara_record,rui_record) :
        return  azara_record + rui_record
    else :
        return "not a match"

    


def clean_up(combined_record_group):
    """

    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned". Excess coordinates and information removed.
    """
    txt = ""
    for e in combined_record_group :
        txt = txt+ "".join( ("(" ,','.join(map(str, (e[0],) + e[2:])),')\n'))
    return txt
        
