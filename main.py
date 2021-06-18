import pandas as pd
import csv

df = pd.read_csv("final.csv")

del df["hyperlink"]
del df["temp_planet_date"]
del df["temp_planet_mass"]
del df["pl_letter"]
del df["pl_name"]
del df["pl_controvflag"]
del df["pl_pnum"]
del df["pl_orbper"]
del df["pl_orbpererr1"]
del df["pl_orbpererr2"]
del df["pl_orbperlim"]
del df["pl_orbsmax"]
del df["pl_orbsmaxerr1"]
del df["pl_orbsmaxerr2"]
del df["pl_orbsmaxlim"]
del df["pl_orbeccen"]
del df["pl_orbeccenerr1"]
del df["pl_orbeccenerr2"]
del df["pl_orbeccenlim"]
del df["pl_orbinclerr1"]
del df["pl_orbinclerr2"]
del df["pl_orbincllim"]
del df["pl_bmassj"]
del df["pl_bmassjerr1"]
del df["pl_bmassjerr2"]
del df["pl_bmassjlim"]
del df["pl_bmassprov"]
del df["pl_radj"]
del df["pl_radjerr1"]
del df["pl_radjerr2"]
del df["pl_radjlim"]
del df["pl_denserr1"]
del df["pl_denserr2"]
del df["pl_denslim"]
del df["pl_ttvflag"]
del df["pl_kepflag"]
del df["pl_k2flag"]
del df["pl_nnotes"]
del df["ra"]
del df["dec"]
del df["st_dist"]
del df["st_disterr1"]
del df["st_disterr2"]
del df["st_distlim"]
del df["gaia_dist"]
del df["gaia_disterr1"]
del df["gaia_disterr2"]
del df["gaia_distlim"]
del df["st_optmag"]
del df["st_optmagerr"]
del df["st_optmaglim"]
del df["st_optband"]
del df["gaia_gmag"]
del df["gaia_gmagerr"]
del df["gaia_gmaglim"]
del df["st_tefferr1"]
del df["st_tefferr2"]
del df["st_tefflim"]
del df["st_masserr1"]
del df["st_masserr2"]
del df["st_masslim"]
del df["st_raderr1"]
del df["st_raderr2"]
del df["st_radlim"]
del df["rowupdate"]
del df["pl_facility"]

df = df.rename({
                'pl_hostname': "solar_system_name", 
                'pl_discmethod': "planet_discovery_method", 
                'pl_orbincl': "planet_orbital_inclination", 
                'pl_dens': "planet_density", 
                'ra_str': "right_ascension", 
                'dec_str': "declination", 
                "st_teff": "host_temperature", 
                'st_mass': "host_mass", 
                'st_rad': "host_radius"
            }, axis='columns')

df.to_csv('main.csv') 