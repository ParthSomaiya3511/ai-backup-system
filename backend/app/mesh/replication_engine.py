import shutil

def replicate_file(

    source,

    destination

):

    shutil.copy2(

        source,

        destination

    )

    return True