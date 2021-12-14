    def eppendorf_1_5_tip_height(vol, 
                                 r = 8.69/2, 
                                 depth = 2,
                                 min_height = 0.5):
        """
        Description
        -----------
        Volume tracker for a standard 1.5 mL screwcap eppendorf. Prevents the
        tip from going too deep and spilling the liquid.
        
        Assumes the eppendorf is cilindrical from 0.4 mL upwards (not 100% 
        accurate). For this section, the tip will enter exactly <depth> mm
        from the current liquid height (meassured from the bottom).
        
        For the conical part,
            - if the volume is between 0.3 and 0.4, the tip enters the liquid
              <depth> mm from the 0.3 mark (~15 mm)
            - if the volume is between 0.2 and 0.3, the tip enters the liquid
              <depth> mm from the 0.2 mark (~13 mm)
            - if the volume is between 0.1 and 0.2, the tip enters the liquid
              <depth> mm from the 0.1 mark (~9 mm)
            - if the volume is between 0.2 and 0.3, the tip enters the liquid
              at a fixed height of <min_height> mm
        
        Parameters
        ----------
        vol : float
            Current volume in uL.
        r : float, optional
            Top radius in mm. The default is 8.69/2.
        depth : float, optional
            How deep will the tip enter the liquid, in mm. The default is 2.

        min_height : float, optional
            Minimum height, for the tip to enter when volume is under 0.1 uL. 
            The default is 0.5 mm.
            
        Returns
        -------
        float
            Height in mm.
        """
        
        base_100 = 9 # mm
        base_200 = 13
        base_300 = 15
        base_400 = 18

        
        if (vol < 100):
            return min_height
        elif (vol < 200):
            return (base_100 - depth)
        elif (vol < 300):
            return (base_200 - depth)
        elif (vol < 400):
            return (base_300 - depth)
        else:        
            ## volume
            vol_from_base = (vol - 400) # from uL = mm^3
            print(vol)
            # now we do V = h * pi * r**2    (plus the base height)
            height = base_400 + vol_from_base/(3.14159*((r)**2)) - depth
            if (height >= min_height):
                return height
            else:
                return min_height
