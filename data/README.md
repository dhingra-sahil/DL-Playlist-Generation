# Data Sources

Folder to hold data. 

## allphishsets.json

JSON to be read into python `pd.DataFrame`. Example:

```shell

{
    'showdate':str,   # date of the concert
    'set':str,        # set of the show (1,2,3 or encore)
    'position':int,   # relative position in the show
    'songid':int,     # song id number
    'slug':str,       # song name
    'trans_mark':str, # song transition marker
    'gap':int,        # number of shows since the song last played
    'isjam':str,      # categorical - "jam" song
    'city':str,       # venue city
    'state':str,      # venue state
    'country':str,    # venue country
    'venueid':int,    # venue id number
    'tourid':int,     # which tour the show was part of
    'showlength':int  # number of songs in the show max(position)
}

         showdate set  position  songid                     slug trans_mark  gap  isjam              city state country  tourid  venueid  setlength                artist  times_played last_played       debut
0      2000-09-17   1         1     242                   guyute         ,     5      0          Columbia    MD     USA      50        9         16                 Phish         133.0  2023-08-02  1994-10-07
1      2000-09-17   1         2      45        back-on-the-train         ,     7      0          Columbia    MD     USA      50        9         16        Trey Anastasio         149.0  2023-10-06  1999-06-30
2      2000-09-17   1         3      48              bathtub-gin         ,     6      0          Columbia    MD     USA      50        9         16                 Phish         298.0  2023-10-10  1989-05-26
3      2000-09-17   1         4     341             limb-by-limb         ,     6      0          Columbia    MD     USA      50        9         16                 Phish         154.0  2023-07-26  1997-06-13
4      2000-09-17   1         5     591           the-moma-dance         ,     4      0          Columbia    MD     USA      50        9         16                 Phish         193.0  2023-10-06  1998-06-30
...           ...  ..       ...     ...                      ...        ...  ...    ...               ...   ...     ...     ...      ...        ...                   ...           ...         ...         ...
37548  2023-08-26   2        13    2656        everythings-right         ,     2      0  Saratoga Springs    NY     USA      61     1588         16        Trey Anastasio          51.0  2023-10-14  2017-07-14
37549  2023-08-26   2        14    2845  a-life-beyond-the-dream         ,     3      0  Saratoga Springs    NY     USA      61     1588         16  Ghosts of the Forest          26.0  2023-10-14  2019-06-19
37550  2023-08-26   2        15     202               first-tube               7      0  Saratoga Springs    NY     USA      61     1588         16        Trey Anastasio         125.0  2023-10-10  1999-09-09
37551  2023-08-26   e        16     440                   possum               3      0  Saratoga Springs    NY     USA      61     1588         16                 Phish         558.0  2023-10-11  1985-09-27
37552  1987-09-26   1         1     440                   possum               0      2        Burlington    VT     USA      61     1594          1                 Phish         558.0  2023-10-11  1985-09-27
```
