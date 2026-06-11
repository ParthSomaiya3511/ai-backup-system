groups = {

    "IT": [],

    "HR": [],

    "Finance": []

}

def add_device_to_group(

    group_name,

    device_id

):

    groups[
        group_name
    ].append(
        device_id
    )
    
    
def get_group_devices(
    group_name
):

    return groups.get(
        group_name,
        []
    )