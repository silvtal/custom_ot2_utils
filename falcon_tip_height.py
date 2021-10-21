def falcon_tip_height(vol, min_height = 0.5, r = 14.5/2, depth = 20):
    """
    Tracking volume function designed for Fisherbrand 
    15 mL Falcon tubes. Given a volume in mL, it returns
    the corresponding height (to be specified as well.bottom()[height])
    
    vol is in mL
    r is the radius in mm
    min_height is the minimum height in mm
    depth is how deep you want the tip to enter the liquid (mm)
    """

    if (vol < 2):
        return min_height

    else:        
        base = 27 # the height in mm from 0 to 2 mL is different
        # (that's why we substract 2 here:)
        vol2 = (vol - 2) * 1000 # from mL to mm**3

        # now we do V = h * pi * r**2    (plus the base height)
        height = base + vol2/(3.14159*((r)**2)) - depth

        if ((height >= min_height) or (vol < 2)):
            return height
        else:
            return min_height
