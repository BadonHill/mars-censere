# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 17:30:50 2019

@author: matej
"""

# Module gonverning the attributes of the colonists


import logging
import random
import uuid

from config import Generator as thisApp

from .base import Base as Base
from .colonist import Colonist as Colonist

from .names import get_random_male_first_name
from .names import get_random_female_first_name
from .names import get_random_family_name

class Astronaut(Colonist, Base):
    
    def __repr__(self):
        r"""
Provide a friendly representation of the object.
"""
        return "<Astronaut(id=%s, '{} {}')>".format( self.id,
                self.first_name, self.family_name)

    def initialize(self, solday):

        self.id = str(uuid.uuid4())

        self.simulation = thisApp.simulation

        # might want to bias Astronaut sex beyond 50:50
        self.sex = random.choices( [ 'm', 'f'], [50, 50] )[0]

        if self.sex == 'm':
            self.first_name = get_random_male_first_name()

            # \TODO straight:homosexual:bisexual = 90:6:4 
            self.orientation = random.choices( [ 'f', 'm', 'mf' ], [ 60, 6, 4 ] )[0]

        else:
            self.first_name = get_random_female_first_name()

            self.orientation = random.choices( [ 'm', 'f', 'mf' ], [ 90, 6, 4 ] )[0]

        self.family_name = get_random_family_name()

        self.birth_location = 'Earth'

        # add dummy biological parents to make consanguinity 
        # easier (no special cases)
        # There is an assumption that astronauts are not 
        # related to any earlier astronaut
        biological_father = str(uuid.uuid4())
        biological_mother = str(uuid.uuid4())

        # earth age in earth days converted to sols, then backdated from now
        self.birth_solday =  solday - (
             int(random.choice( 
                thisApp.astronaut_age_range.split(",") ) ) * 365.25 * 1.02749125 )

        productivity = 100

